#!/usr/bin/env python3
"""Generate new HXL source files locally; never deploy or overwrite files."""
import argparse
import json
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

NAME = re.compile(r"[A-Za-z][A-Za-z0-9_]*\Z")
APEX = re.compile(r"@apexClassType/[A-Za-z][A-Za-z0-9_]*(?:\$[A-Za-z][A-Za-z0-9_]*)?\Z")
TYPES = {"lightning__textType", "lightning__multilineTextType", "lightning__urlType", "lightning__numberType", "lightning__integerType", "lightning__booleanType"}
NS = "http://soap.sforce.com/2006/04/metadata"
ET.register_namespace("", NS)

def load(path):
    return json.loads(Path(path).read_text(), parse_constant=lambda value: (_ for _ in ()).throw(ValueError("Non-finite JSON value: " + value)))

def encoded(data):
    return json.dumps(data, indent=2, allow_nan=False) + "\n"

def xml(tag, children):
    root = ET.Element("{" + NS + "}" + tag)
    for key, value in children:
        ET.SubElement(root, "{" + NS + "}" + key).text = value
    return ET.tostring(root, encoding="unicode", xml_declaration=True) + "\n"

def name(value, what):
    if not NAME.fullmatch(value):
        raise ValueError(what + " must be an API identifier, not a path")
    return value

def generate(args):
    widget = name(args.widget, "Widget name")
    base = name(args.type_name or widget, "Type name")
    payload_property = name(args.payload_property, "Payload property")
    if args.channel != "static" and (not args.apex_type or not APEX.fullmatch(args.apex_type)):
        raise ValueError("Agentforce/MCP requires --apex-type @apexClassType/c__ActualResponseClass")
    project = args.project.resolve()
    config_path = project / "sfdx-project.json"
    config = load(config_path) if config_path.exists() else {"packageDirectories": [{"path": "force-app", "default": True}], "sourceApiVersion": "67.0"}
    version = str(config.get("sourceApiVersion", "67.0"))
    if float(version) < 67:
        raise ValueError("HXL requires sourceApiVersion 67.0 or later; update the project explicitly")
    if args.source_dir:
        relative_source = Path(args.source_dir)
        if relative_source.is_absolute() or ".." in relative_source.parts:
            raise ValueError("--source-dir must stay inside the project")
    else:
        packages = config.get("packageDirectories", [])
        chosen = [p for p in packages if p.get("default")]
        if len(chosen) != 1:
            chosen = packages if len(packages) == 1 else []
        if len(chosen) != 1:
            raise ValueError("Specify --source-dir for a project with no unambiguous package directory")
        package = Path(chosen[0]["path"])
        if package.is_absolute() or ".." in package.parts:
            raise ValueError("Package directory must stay inside the project")
        relative_source = package if any((project / package / d).exists() for d in ("uiWidgets", "lightningTypes", "objects", "classes")) else package / "main/default"
    source = (project / relative_source).resolve()
    if not source.is_relative_to(project):
        raise ValueError("Source directory resolves outside the project")
    spec = load(args.spec)
    fields = spec.get("fields")
    if not isinstance(fields, list) or not fields:
        raise ValueError("Specification requires a nonempty fields array")
    properties, nodes, mappings = {}, [], {}
    for field in fields:
        key = name(field["name"], "Field name")
        if key in properties:
            raise ValueError("Duplicate field: " + key)
        typ = field["lightning:type"]
        if typ not in TYPES:
            raise ValueError("Starter does not support this field type: " + typ)
        title = field.get("title", key)
        if not isinstance(title, str):
            raise ValueError("Field title must be text")
        sample = field["sample"]
        if typ == "lightning__booleanType":
            valid = type(sample) is bool
        elif typ == "lightning__integerType":
            valid = type(sample) is int
        elif typ == "lightning__numberType":
            valid = type(sample) in (int, float)
        else:
            valid = isinstance(sample, str)
        if not valid:
            raise ValueError("Sample value has wrong type for " + key)
        data_path = field.get("dataPath", key)
        if not isinstance(data_path, str) or not all(NAME.fullmatch(p) for p in data_path.split(".")):
            raise ValueError("dataPath must be a dot-separated property path")
        properties[key] = {"title": title, "lightning:type": typ}
        if field.get("description"):
            properties[key]["description"] = field["description"]
        value = sample if args.channel == "static" else "{!$attrs." + key + "}"
        if typ == "lightning__urlType":
            node = {"definition": "tile/link", "attributes": {"href": value, "text": title}}
        elif typ == "lightning__booleanType":
            node = {"definition": "tile/text", "attributes": {"text": title + " enabled"}}
            node["meta"] = {"if": value}
        else:
            node = {"definition": "tile/text", "attributes": {"text": str(value) if args.channel == "static" else value}}
        if typ != "lightning__urlType":
            nodes.append({"definition": "tile/text", "attributes": {"text": title, "variant": "caption", "color": "muted"}})
        nodes.append(node)
        prefix = "outputValues." + payload_property + "." if args.channel == "mcp" else ""
        mappings[key] = "{!$attrs." + prefix + data_path + "}"
    title = spec.get("title", widget)
    description = spec.get("description", "HXL widget " + widget)
    if not isinstance(title, str) or not isinstance(description, str):
        raise ValueError("Specification title/description must be text")
    widget_dir = source / "uiWidgets" / widget
    composition = {"type": "lightning__agentforceWidget", "contentBody": {"widgetBody": {"definition": "tile/widget", "children": [{"definition": "tile/container", "children": [{"definition": "tile/column", "attributes": {"align": "stretch", "gap": "md"}, "children": nodes}]}]}}}
    schema = {"title": title + " inputs", "description": description, "type": "object", "properties": {"attributes": {"lightning:type": "lightning__objectType", "properties": properties}}}
    files = {
        widget_dir / (widget + ".json"): encoded(composition),
        widget_dir / "schema.json": encoded(schema),
        widget_dir / (widget + ".uiwidget-meta.xml"): xml("UiWidgetBundle", [("masterLabel", title), ("description", description), ("widgetType", "JSON")]),
    }
    clts = []
    if args.channel == "agentforce":
        clts = [base if args.type_name else base + "Response"]
        files[source / "lightningTypes" / clts[0] / "schema.json"] = encoded({"title": title + " response", "lightning:type": args.apex_type})
    elif args.channel == "mcp":
        clts = [base + "OutputValues", base + "Result"]
        common = {"type": "object", "lightning:type": "lightning__objectType", "unevaluatedProperties": False, "lightning:tags": ["mcp"]}
        files[source / "lightningTypes" / clts[0] / "schema.json"] = encoded({"title": title + " output variables", **common, "properties": {payload_property: {"title": "Output data", "lightning:type": args.apex_type}}})
        files[source / "lightningTypes" / clts[1] / "schema.json"] = encoded({"title": title + " result", **common, "properties": {"actionName": {"title": "Action", "lightning:type": "lightning__textType"}, "isSuccess": {"title": "Success", "lightning:type": "lightning__booleanType"}, "outputValues": {"title": "Output", "lightning:type": "c__" + clts[0]}}})
    if clts:
        files[source / "lightningTypes" / clts[-1] / "renderer.json"] = encoded({"renderer": {"componentOverrides": {"$": {"definition": "@widget/c/" + widget, "attributes": mappings}}}})
    package = ET.Element("{" + NS + "}Package")
    for kind, members in [("UiWidgetBundle", [widget]), ("LightningTypeBundle", clts)]:
        if not members:
            continue
        group = ET.SubElement(package, "{" + NS + "}types")
        for member in members:
            ET.SubElement(group, "{" + NS + "}members").text = member
        ET.SubElement(group, "{" + NS + "}name").text = kind
    ET.SubElement(package, "{" + NS + "}version").text = version
    files[project / "manifest" / ("hxl-" + widget + ".xml")] = ET.tostring(package, encoding="unicode", xml_declaration=True) + "\n"
    if not config_path.exists():
        files[config_path] = encoded(config)
    for path in files:
        if path.exists() or path.is_symlink():
            raise ValueError("Refusing to overwrite: " + str(path))
        if not path.resolve().is_relative_to(project):
            raise ValueError("Output resolves outside the project: " + str(path))
    written = []
    try:
        for path, content in files.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x") as handle:
                handle.write(content)
            written.append(path)
    except Exception:
        for path in reversed(written):
            path.unlink()
        raise
    print("Created " + str(len(files)) + " files beneath " + str(project))
    for path in written:
        print(path.relative_to(project))
    if args.apex_type and "$" in args.apex_type:
        print("Note: inner-class sample reference supplied; dedicated CLT guidance prefers top-level classes for new types.")
    if args.channel == "mcp":
        print("Remaining: deploy the actual Apex action, wire server resource to c__" + clts[-1] + ", activate, configure OAuth, test the client.")
    elif args.channel == "agentforce":
        print("Remaining: implement/verify actual Apex output, deploy, select CLT in action Output Rendering, test Agentforce.")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path)
    parser.add_argument("--widget", required=True)
    parser.add_argument("--channel", choices=["static", "agentforce", "mcp"], default="static")
    parser.add_argument("--apex-type")
    parser.add_argument("--type-name")
    parser.add_argument("--payload-property", default="summary")
    parser.add_argument("--source-dir")
    parser.add_argument("--spec", type=Path, default=Path(__file__).resolve().parents[1] / "assets/account-summary-spec.json")
    args = parser.parse_args()
    try:
        generate(args)
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, "Scaffold error: " + str(error) + "\n")

if __name__ == "__main__":
    main()
