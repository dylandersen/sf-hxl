import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/salesforce-hxl"
module_spec = importlib.util.spec_from_file_location("hxl_validate", SKILL / "scripts/validate.py")
validator = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(validator)

class HXLTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "project"

    def scaffold(self, channel="mcp", extra=(), project=None):
        return subprocess.run([sys.executable, str(SKILL / "scripts/scaffold.py"), "--project", str(project or self.project), "--widget", "caseSummary", "--channel", channel, "--apex-type", "@apexClassType/c__CaseSummaryResponse", *extra], capture_output=True, text=True)

    def generated(self, channel="mcp"):
        call = self.scaffold(channel)
        self.assertEqual(call.returncode, 0, call.stderr)
        return self.project / "force-app/main/default"

    def modify(self, path, change):
        value = json.loads(path.read_text())
        change(value)
        path.write_text(json.dumps(value))

    def fails(self, contains):
        report = validator.validate(self.project)
        self.assertTrue(any(contains in issue for issue in report["errors"]), report)

    def test_all_scaffold_modes(self):
        for channel in ("static", "agentforce", "mcp"):
            with self.subTest(channel=channel):
                project = Path(self.temp.name) / channel
                call = self.scaffold(channel, project=project)
                self.assertEqual(call.returncode, 0, call.stderr)
                report = validator.validate(project)
                self.assertFalse(report["errors"], report)
                self.assertEqual(report["widgets"], 1)
                self.assertEqual(report["renderers"], 0 if channel == "static" else 1)

    def test_real_payload_variable(self):
        call = self.scaffold(extra=("--payload-property", "caseInfo"))
        self.assertEqual(call.returncode, 0, call.stderr)
        report = validator.validate(self.project)
        self.assertFalse(report["errors"], report)
        base = self.project / "force-app/main/default/lightningTypes"
        payload = json.loads((base / "caseSummaryOutputValues/schema.json").read_text())
        self.assertEqual(set(payload["properties"]), {"caseInfo"})
        renderer = json.loads((base / "caseSummaryResult/renderer.json").read_text())
        self.assertTrue(all("outputValues.caseInfo." in value for value in renderer["renderer"]["componentOverrides"]["$"]["attributes"].values()))

    def test_no_overwrite_or_partial_updates(self):
        self.generated()
        before = {str(p): p.read_bytes() for p in self.project.rglob("*") if p.is_file()}
        call = self.scaffold()
        self.assertNotEqual(call.returncode, 0)
        after = {str(p): p.read_bytes() for p in self.project.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_preserve_existing_project_and_source_directory(self):
        self.project.mkdir()
        content = '{"packageDirectories":[{"path":"src","default":true}],"sourceApiVersion":"67.0","namespace":"custom"}\n'
        (self.project / "sfdx-project.json").write_text(content)
        call = self.scaffold(extra=("--source-dir", "src/metadata"))
        self.assertEqual(call.returncode, 0, call.stderr)
        self.assertEqual((self.project / "sfdx-project.json").read_text(), content)
        self.assertTrue((self.project / "src/metadata/uiWidgets/caseSummary").is_dir())
        self.assertFalse(validator.validate(self.project)["errors"])

    def test_old_api_fails_before_writes(self):
        self.project.mkdir()
        (self.project / "sfdx-project.json").write_text('{"sourceApiVersion":"66.0"}')
        call = self.scaffold()
        self.assertNotEqual(call.returncode, 0)
        self.assertFalse((self.project / "force-app").exists())

    def test_path_escape_fails_before_writes(self):
        call = self.scaffold(extra=("--source-dir", "../escape"))
        self.assertNotEqual(call.returncode, 0)
        self.assertFalse(self.project.exists())

    def test_wrong_root_rejected(self):
        src = self.generated()
        self.modify(src / "uiWidgets/caseSummary/caseSummary.json", lambda v: v["contentBody"]["widgetBody"].update(definition="tile/container"))
        self.fails("root tile/widget")

    def test_undeclared_binding_rejected(self):
        src = self.generated()
        def change(v):
            v["contentBody"]["widgetBody"]["children"].append({"definition": "tile/text", "attributes": {"text": "{!$attrs.typo}"}})
        self.modify(src / "uiWidgets/caseSummary/caseSummary.json", change)
        self.fails("undeclared widget attribute")

    def test_scope_is_checked(self):
        src = self.generated()
        def change(v):
            v["contentBody"]["widgetBody"]["children"].append({"definition": "tile/text", "attributes": {"text": "{!$entry.name}"}})
        self.modify(src / "uiWidgets/caseSummary/caseSummary.json", change)
        self.fails("Unbound expression variable")

    def test_scoped_iteration_and_boolean_condition(self):
        src = self.generated()
        schema = src / "uiWidgets/caseSummary/schema.json"
        self.modify(schema, lambda v: v["properties"]["attributes"]["properties"].update(items={"title": "Items", "lightning:type": "lightning__listType"}))
        def change(v):
            v["contentBody"]["widgetBody"]["children"].append({"definition": "tile/text", "meta": {"forEach": "{!$attrs.items}", "forItem": "$entry", "if": "{!$entry.active}"}, "attributes": {"text": "{!$entry.name}"}})
        self.modify(src / "uiWidgets/caseSummary/caseSummary.json", change)
        self.assertFalse(validator.validate(self.project)["errors"])

    def test_renderer_outer_shape_rejected(self):
        src = self.generated()
        self.modify(src / "lightningTypes/caseSummaryResult/renderer.json", lambda v: v.update(wrong=v.pop("renderer")))
        self.fails("renderer.componentOverrides.$")

    def test_direct_mcp_mapping_rejected(self):
        src = self.generated()
        self.modify(src / "lightningTypes/caseSummaryResult/renderer.json", lambda v: v["renderer"]["componentOverrides"]["$"]["attributes"].update(name="{!$attrs.name}"))
        self.fails("must traverse outputValues")

    def test_wrong_invocable_output_variable_rejected(self):
        src = self.generated()
        self.modify(src / "lightningTypes/caseSummaryResult/renderer.json", lambda v: v["renderer"]["componentOverrides"]["$"]["attributes"].update(name="{!$attrs.outputValues.wrongVariable.name}"))
        self.fails("absent output variable")

    def test_payload_renderer_rejected(self):
        src = self.generated()
        wrapper = src / "lightningTypes/caseSummaryResult/renderer.json"
        (src / "lightningTypes/caseSummaryOutputValues/renderer.json").write_bytes(wrapper.read_bytes())
        self.fails("payload must not have")

    def test_mcp_tag_required(self):
        src = self.generated()
        self.modify(src / "lightningTypes/caseSummaryResult/schema.json", lambda v: v.pop("lightning:tags"))
        self.fails("needs the mcp tag")

    def test_required_alt_rejected(self):
        src = self.generated()
        def change(v):
            v["contentBody"]["widgetBody"]["children"].append({"definition": "tile/image", "attributes": {"src": "https://example.com/image.png"}})
        self.modify(src / "uiWidgets/caseSummary/caseSummary.json", change)
        self.fails("Missing documented attribute: alt")

    def test_action_object_shape(self):
        src = self.generated()
        def change(v):
            v["contentBody"]["widgetBody"]["children"].append({"definition": "tile/button", "attributes": {"label": "Review", "actions": {"click": [{"definition": "action/sendMessage", "attributes": {}}]}}})
        self.modify(src / "uiWidgets/caseSummary/caseSummary.json", change)
        self.fails("Action requires string content")

    def test_resource_name_must_match(self):
        src = self.generated()
        directory = src / "mcpServerDefinitions"
        directory.mkdir()
        (directory / "server.mcpServerDefinition-meta.xml").write_text('<McpServerDefinition xmlns="http://soap.sforce.com/2006/04/metadata"><resources><resourceName>correct</resourceName><resourceUri>ui://widget/lightningType/c__caseSummaryResult</resourceUri></resources><tools><uiResource>typo</uiResource></tools></McpServerDefinition>')
        self.fails("no matching resourceName")

    def test_resource_points_to_wrapper(self):
        src = self.generated()
        directory = src / "mcpServerDefinitions"
        directory.mkdir()
        (directory / "server.mcpServerDefinition-meta.xml").write_text('<McpServerDefinition xmlns="http://soap.sforce.com/2006/04/metadata"><resources><resourceName>ui</resourceName><resourceUri>ui://widget/lightningType/c__caseSummaryOutputValues</resourceUri></resources><tools><uiResource>ui</uiResource></tools></McpServerDefinition>')
        self.fails("must point to the result wrapper")

    def test_duplicate_json_key_rejected(self):
        src = self.generated()
        (src / "uiWidgets/caseSummary/caseSummary.json").write_text('{"type":"one","type":"two"}')
        self.fails("Duplicate JSON key")

    def test_installer_is_self_contained_and_no_overwrite(self):
        dest = Path(self.temp.name) / "installed"
        args = [sys.executable, str(ROOT / "tools/install_skill.py"), "--skills-dir", str(dest)]
        first = subprocess.run(args, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        call = subprocess.run([sys.executable, str(dest / "salesforce-hxl/scripts/scaffold.py"), "--project", str(self.project), "--widget", "installedWidget"], capture_output=True, text=True)
        self.assertEqual(call.returncode, 0, call.stderr)
        second = subprocess.run(args, capture_output=True, text=True)
        self.assertNotEqual(second.returncode, 0)

if __name__ == "__main__":
    unittest.main()
