#!/usr/bin/env python3
"""Check local HXL contracts; this is not a Salesforce compiler or runtime test."""
import argparse
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET

SKILL = Path(__file__).resolve().parents[1]
CATALOG = json.loads((SKILL / "references/component-contracts.json").read_text())
ICONS = set(json.loads((SKILL / "references/icon-names.json").read_text()))
NS = "{http://soap.sforce.com/2006/04/metadata}"
REF = re.compile(r"\$(\w+)(?:\.(\w+))?")
VAR = re.compile(r"\$[A-Za-z][A-Za-z0-9_]*\Z")


def unique(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("Duplicate JSON key: " + key)
        obj[key] = value
    return obj


def validate(path):
    root = Path(path).resolve()
    result = {"widgets": 0, "renderers": 0, "errors": [], "warnings": []}
    def error(where, message):
        result["errors"].append(str(where) + ": " + message)
    def warn(where, message):
        result["warnings"].append(str(where) + ": " + message)
    def read(file):
        try:
            return json.loads(file.read_text(), object_pairs_hook=unique, parse_constant=lambda v: (_ for _ in ()).throw(ValueError("Non-finite value: " + v)))
        except (OSError, ValueError) as exc:
            error(file, str(exc))
            return None
    def tokens(value, attrs, scope, where):
        if isinstance(value, str) and "{!" in value:
            for expr in re.findall(r"\{!([^{}]*)\}", value):
                for variable, field in REF.findall(expr):
                    if variable == "attrs":
                        if not field or field not in attrs:
                            error(where, "Binding names an undeclared widget attribute: " + field)
                    elif variable not in scope:
                        error(where, "Unbound expression variable: $" + variable)
        elif isinstance(value, list):
            for item in value:
                tokens(item, attrs, scope, where)
        elif isinstance(value, dict):
            for item in value.values():
                tokens(item, attrs, scope, where)
    def expression(value):
        return isinstance(value, str) and "{!" in value
    def table(attrs, where):
        columns = attrs.get("columns")
        if not isinstance(columns, list):
            return
        keys = set()
        for col in columns:
            if not isinstance(col, dict) or not isinstance(col.get("key"), str) or not isinstance(col.get("header"), str):
                error(where, "Table columns need key/header strings")
                continue
            if col["key"] in keys:
                error(where, "Duplicate table column key: " + col["key"])
            keys.add(col["key"])
            ct = col.get("columnType")
            if ct is None:
                continue
            if not isinstance(ct, dict) or ct.get("type") not in {"date", "number", "link", "picklist"}:
                error(where, "Unknown table columnType")
                continue
            if ct["type"] == "picklist":
                options = ct.get("options")
                if not isinstance(options, list) or not options:
                    error(where, "Picklist column needs nonempty options")
                else:
                    vals = set()
                    for option in options:
                        if not isinstance(option, dict) or any(not isinstance(option.get(k), str) or len(option[k]) > 255 for k in ("label", "value")):
                            error(where, "Picklist options require label/value strings <=255 characters")
                        elif option["value"] in vals:
                            error(where, "Duplicate picklist option value")
                        else:
                            vals.add(option["value"])
            if ct["type"] == "number":
                for digit in ("minimumFractionDigits", "maximumFractionDigits"):
                    if digit in ct and (type(ct[digit]) is not int or not 0 <= ct[digit] <= 20):
                        error(where, digit + " must be an integer from 0 to 20")
        rows = attrs.get("rows")
        if isinstance(rows, list):
            for row in rows:
                if not isinstance(row, dict):
                    error(where, "Table rows must be objects")
                elif keys - set(row):
                    warn(where, "Table row lacks column fields: " + ", ".join(sorted(keys - set(row))))
        pagination = attrs.get("pagination")
        if isinstance(pagination, dict) and (type(pagination.get("pageSize")) is not int or pagination["pageSize"] <= 0):
            error(where, "pagination.pageSize must be a positive integer")
    def node(value, attrs, scope, parent, where):
        if not isinstance(value, dict):
            error(where, "Component must be an object")
            return
        definition = value.get("definition")
        if definition != "tile/widget" and definition not in CATALOG:
            error(where, "Component is not in the bundled beta catalog: " + str(definition))
            return
        meta = value.get("meta", {})
        if not isinstance(meta, dict):
            error(where, "meta must be an object")
            meta = {}
        tokens(meta.get("forEach"), attrs, scope, where)
        inner_scope = set(scope)
        if "forEach" in meta:
            for key in ("forItem", "forIndex"):
                var = meta.get(key, "$Item" if key == "forItem" else None)
                if var is not None:
                    if not isinstance(var, str) or not VAR.fullmatch(var) or var == "$attrs":
                        error(where, key + " must be a $-prefixed non-reserved variable")
                    else:
                        inner_scope.add(var[1:])
        elif "forItem" in meta or "forIndex" in meta:
            error(where, "Item/index variables require forEach")
        if "if" in meta:
            if type(meta["if"]) is not bool and not expression(meta["if"]) and meta["if"] is not None:
                error(where, "meta.if needs a Boolean or Boolean expression")
            tokens(meta["if"], attrs, inner_scope, where)
        attributes = value.get("attributes", {})
        if not isinstance(attributes, dict):
            error(where, "attributes must be an object")
            attributes = {}
        if definition in CATALOG:
            contract = CATALOG[definition]
            for key, spec in contract["properties"].items():
                if spec["required"] and key not in attributes:
                    (warn if key in contract["soft_required"] else error)(where, "Missing documented attribute: " + key)
            for key, val in attributes.items():
                if key not in contract["properties"]:
                    error(where, "Unknown component attribute: " + key)
                    continue
                spec = contract["properties"][key]
                if expression(val) or key == "actions":
                    continue
                if "enum" in spec and val not in spec["enum"]:
                    error(where, "Invalid " + key + " value: " + str(val))
                typ = spec["lightning_type"]
                expected = {"lightning__booleanType": bool, "lightning__listType": list, "lightning__objectType": dict}
                if typ in expected and type(val) is not expected[typ]:
                    error(where, key + " has wrong literal value type")
                if typ == "lightning__numberType" and type(val) not in (int, float):
                    error(where, key + " must be numeric")
                if typ in {"lightning__textType", "lightning__multilineTextType", "lightning__urlType", "lightning__markdownTextType", "lightning__iconName"} and not isinstance(val, str):
                    error(where, key + " must be a string or binding expression")
                if typ == "lightning__iconName" and (not isinstance(val, str) or val not in ICONS):
                    error(where, "Unknown semantic icon: " + str(val))
        tokens(attributes, attrs, inner_scope, where)
        actions = attributes.get("actions")
        if actions is not None:
            if not isinstance(actions, dict):
                error(where, "actions must be an event-to-array object")
            else:
                for event, sequence in actions.items():
                    if not isinstance(sequence, list):
                        error(where, "actions." + event + " must be an array")
                        continue
                    for action in sequence:
                        if not isinstance(action, dict) or not isinstance(action.get("definition"), str) or not isinstance(action.get("attributes"), dict):
                            error(where, "Each action requires definition and attributes")
                            continue
                        key = {"action/openLink": "url", "action/sendMessage": "content"}.get(action["definition"])
                        if key and not isinstance(action["attributes"].get(key), str):
                            error(where, "Action requires string " + key)
                        if not key:
                            warn(where, "Custom action requires a verified host handler: " + action["definition"])
        if definition == "tile/accordionItem" and parent != "tile/accordion":
            error(where, "accordionItem must be directly inside accordion")
        if definition == "tile/listItem" and parent != "tile/list":
            error(where, "listItem must be inside list")
        if definition == "tile/table":
            table(attributes, where)
        children = value.get("children", [])
        if not isinstance(children, list):
            error(where, "children must be an array")
            return
        for index, child in enumerate(children):
            if definition == "tile/accordion" and isinstance(child, dict) and child.get("definition") != "tile/accordionItem":
                error(where, "accordion children must be accordionItem")
            if definition == "tile/list" and isinstance(child, dict) and child.get("definition") != "tile/listItem":
                error(where, "list children must be listItem")
            if definition == "tile/listItem" and isinstance(child, dict) and child.get("definition") not in {"tile/text", "tile/link", "tile/icon"}:
                error(where, "Unsupported listItem child")
            node(child, attrs, inner_scope, definition, str(where) + "/children/" + str(index))
    configs = list(root.rglob("sfdx-project.json"))
    if root.name == "sfdx-project.json":
        configs = [root]
    for config_path in configs:
        config = read(config_path)
        if isinstance(config, dict) and "sourceApiVersion" in config:
            try:
                if float(config["sourceApiVersion"]) < 67:
                    error(config_path, "HXL requires API 67.0+")
            except (ValueError, TypeError):
                error(config_path, "Invalid sourceApiVersion")
    widgets = {}
    for directory in sorted(p for p in root.rglob("*") if p.is_dir() and p.parent.name == "uiWidgets"):
        result["widgets"] += 1
        composition = read(directory / (directory.name + ".json"))
        attrs = {}
        schema_path = directory / "schema.json"
        if schema_path.exists():
            schema = read(schema_path)
            try:
                attrs = schema["properties"]["attributes"]["properties"]
                if not isinstance(attrs, dict):
                    raise TypeError()
            except (KeyError, TypeError):
                error(schema_path, "Widget schema needs properties.attributes.properties")
                attrs = {}
            for key, spec in attrs.items():
                if not isinstance(spec, dict) or not isinstance(spec.get("lightning:type"), str):
                    error(schema_path, "Attribute lacks lightning:type: " + key)
        widgets.setdefault(directory.name, []).append((directory, attrs))
        meta = directory / (directory.name + ".uiwidget-meta.xml")
        try:
            tree = ET.parse(meta).getroot()
            if tree.tag != NS + "UiWidgetBundle" or tree.findtext(NS + "widgetType") != "JSON":
                error(meta, "Expected UiWidgetBundle namespace and widgetType JSON")
        except (OSError, ET.ParseError) as exc:
            error(meta, str(exc))
        if isinstance(composition, dict):
            body = composition.get("contentBody", {}).get("widgetBody") if isinstance(composition.get("contentBody"), dict) else None
            if composition.get("type") != "lightning__agentforceWidget" or not isinstance(body, dict) or body.get("definition") != "tile/widget":
                error(directory, "Expected lightning__agentforceWidget with root tile/widget")
            elif isinstance(body, dict):
                node(body, attrs, set(), None, directory)
    types = {}
    for p in root.rglob("schema.json"):
        if p.parent.parent.name == "lightningTypes":
            schema = read(p)
            if isinstance(schema, dict):
                types.setdefault(p.parent.name, []).append((p.parent, schema))
    for renderer_path in root.rglob("*.json"):
        if renderer_path.name not in {"renderer.json", "editor.json"} or "lightningTypes" not in renderer_path.parts:
            continue
        data = read(renderer_path)
        if not isinstance(data, dict):
            continue
        widget_refs = []
        def walk(value):
            if isinstance(value, dict):
                if isinstance(value.get("definition"), str) and value["definition"].startswith("@widget/"):
                    widget_refs.append(value)
                for item in value.values():
                    walk(item)
            elif isinstance(value, list):
                for item in value:
                    walk(item)
        walk(data)
        if not widget_refs:
            continue
        result["renderers"] += 1
        renderer = data.get("renderer")
        overrides = renderer.get("componentOverrides") if isinstance(renderer, dict) else None
        root_override = overrides.get("$") if isinstance(overrides, dict) else None
        if not isinstance(root_override, dict) or not str(root_override.get("definition", "")).startswith("@widget/"):
            error(renderer_path, "HXL needs renderer.componentOverrides.$ with its widget definition")
        if renderer_path.name != "renderer.json" or renderer_path.parent.parent.name != "lightningTypes":
            error(renderer_path, "HXL renderer must be at the type root; editor references unsupported")
        for override in widget_refs:
            parts = override["definition"].split("/")
            if len(parts) != 3:
                error(renderer_path, "Invalid @widget/namespace/name reference")
                continue
            if parts[1] != "c":
                warn(renderer_path, "External/package widget cannot be checked locally: " + override["definition"])
                continue
            found = widgets.get(parts[2], [])
            if len(found) != 1:
                warn(renderer_path, "Local widget dependency missing or ambiguous: " + parts[2])
                continue
            widget_dir, attrs = found[0]
            mappings = override.get("attributes", {})
            if not isinstance(mappings, dict):
                error(renderer_path, "Renderer attributes must be an object")
                continue
            if not (widget_dir / "schema.json").exists():
                error(renderer_path, "Dynamic widget mapping requires widget schema.json")
            for key in mappings:
                if key not in attrs:
                    error(renderer_path, "Mapping target absent from widget contract: " + key)
            type_schema = read(renderer_path.parent / "schema.json")
            if isinstance(type_schema, dict) and ("mcp" in type_schema.get("lightning:tags", []) or "outputValues" in type_schema.get("properties", {})):
                if "mcp" not in type_schema.get("lightning:tags", []):
                    error(renderer_path, "MCP result wrapper needs the mcp tag")
                props = type_schema.get("properties", {})
                if not isinstance(props, dict) or not {"actionName", "isSuccess", "outputValues"} <= set(props):
                    error(renderer_path, "MCP renderer belongs on the result wrapper")
                    continue
                if type_schema.get("type") != "object" or type_schema.get("lightning:type") != "lightning__objectType" or type_schema.get("unevaluatedProperties") is not False:
                    error(renderer_path, "MCP wrapper needs object type and unevaluatedProperties false")
                for header, expected in [("actionName", "lightning__textType"), ("isSuccess", "lightning__booleanType")]:
                    if not isinstance(props.get(header), dict) or props[header].get("lightning:type") != expected:
                        error(renderer_path, "MCP wrapper has wrong " + header + " type")
                output_field = props.get("outputValues")
                output = output_field.get("lightning:type", "") if isinstance(output_field, dict) else ""
                payload_name = output.removeprefix("c__") if isinstance(output, str) else ""
                if payload_name == renderer_path.parent.name:
                    error(renderer_path, "MCP outputValues cannot self-reference")
                payloads = types.get(payload_name, [])
                if len(payloads) != 1:
                    warn(renderer_path, "MCP payload dependency missing/ambiguous: " + output)
                else:
                    payload_dir, payload = payloads[0]
                    if payload.get("type") != "object" or payload.get("lightning:type") != "lightning__objectType" or payload.get("unevaluatedProperties") is not False or "mcp" not in payload.get("lightning:tags", []):
                        error(payload_dir, "MCP payload needs object type, mcp tag, unevaluatedProperties false")
                    if (payload_dir / "renderer.json").exists():
                        error(payload_dir, "MCP payload must not have the widget renderer")
                    for field_spec in payload.get("properties", {}).values():
                        if isinstance(field_spec, dict) and str(field_spec.get("lightning:type", "")).startswith("@apexClassType/"):
                            warn(payload_dir, "Apex payload projection fields require Salesforce validation: " + field_spec["lightning:type"])
                    for value in mappings.values():
                        if isinstance(value, str):
                            for prop in re.findall(r"\$attrs\.outputValues\.(\w+)", value):
                                if prop not in payload.get("properties", {}):
                                    error(renderer_path, "MCP mapping references absent output variable: " + prop)
                for value in mappings.values():
                    if not isinstance(value, str) or "{!$attrs.outputValues." not in value:
                        error(renderer_path, "MCP mapping must traverse outputValues")
            elif isinstance(type_schema, dict) and str(type_schema.get("lightning:type", "")).startswith("@apexClassType/"):
                warn(renderer_path, "Apex projection fields require Salesforce validation: " + type_schema["lightning:type"])
    for file in root.rglob("*.mcpServerDefinition-meta.xml"):
        try:
            tree = ET.parse(file).getroot()
            resources = {}
            for resource in tree.findall(NS + "resources"):
                resource_name = resource.findtext(NS + "resourceName")
                if not resource_name or resource_name in resources:
                    error(file, "Resource names must be present and unique")
                resources[resource_name] = resource.findtext(NS + "resourceUri", "")
            for tool in tree.findall(NS + "tools"):
                target = tool.findtext(NS + "uiResource")
                if target is None:
                    continue
                if target not in resources:
                    error(file, "Tool uiResource has no matching resourceName: " + target)
                else:
                    uri = resources[target]
                    if not uri.startswith("ui://widget/lightningType/"):
                        error(file, "HXL resource must point to a Lightning type URI")
                    elif uri.split("/")[-1].startswith("c__"):
                        found = types.get(uri.split("/")[-1][3:], [])
                        if len(found) != 1:
                            warn(file, "Resource Lightning type missing/ambiguous locally")
                        elif "outputValues" not in found[0][1].get("properties", {}) or not (found[0][0] / "renderer.json").exists():
                            error(file, "Resource must point to the result wrapper with renderer")
        except (OSError, ET.ParseError) as exc:
            error(file, str(exc))
    if not result["widgets"] and not result["renderers"]:
        error(root, "No HXL widget bundles or widget renderers found")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = validate(args.path)
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Checked {report['widgets']} widgets and {report['renderers']} HXL renderers")
        for level in ("errors", "warnings"):
            for message in report[level]:
                print(level[:-1].upper() + ": " + message)
        print("Local checks " + ("failed" if report["errors"] else "passed") + "; Salesforce/runtime checks are separate.")
    raise SystemExit(1 if report["errors"] else 0)

if __name__ == "__main__":
    main()
