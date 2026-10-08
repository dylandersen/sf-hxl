# Widget authoring

Contents: bundle files; composition; attribute schema; formulas; conditional/repeated content; actions; scaffold.

## Bundle files

Use the DX project's actual package directory. Conventional source layout:

```text
force-app/main/default/uiWidgets/accountSummary/
  accountSummary.json
  accountSummary.uiwidget-meta.xml
  schema.json
```

Composition and XML configuration are mandatory. The widget schema is optional for static content and required for runtime attribute mapping. A Lightning type schema models action data; a widget schema models UI inputs; the type's renderer maps between them.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<UiWidgetBundle xmlns="http://soap.sforce.com/2006/04/metadata">
  <masterLabel>Account Summary</masterLabel>
  <description>Account details in a conversation</description>
  <widgetType>JSON</widgetType>
</UiWidgetBundle>
```

`widgetType` must be `JSON`. Label/description are optional. Match filenames to the widget API name. Metadata is `UiWidgetBundle`, available from API 67.0.

## Composition

The outer `type` is `lightning__agentforceWidget` for every supported channel, including MCP. Root `contentBody.widgetBody.definition` must be `tile/widget`. Nested nodes have `definition`, optional `attributes`, ordered `children`, and optional `meta`.

```json
{
  "type": "lightning__agentforceWidget",
  "contentBody": {
    "widgetBody": {
      "definition": "tile/widget",
      "children": [{
        "definition": "tile/column",
        "attributes": {"align": "stretch", "gap": "md"},
        "children": [{
          "definition": "tile/text",
          "attributes": {"text": "{!$attrs.name}", "variant": "h2"}
        }]
      }]
    }
  }
}
```

Choose exact attributes from [components](components.md). Use semantic layout tokens rather than arbitrary pixel styling. Containers frame content; rows/columns arrange it. Supply image/icon alternatives, table captions, and spinner labels. This composition is declarative JSON, not HTML/CSS/JavaScript.

## Attribute schema

Declare UI inputs beneath `properties.attributes.properties`:

```json
{
  "title": "Account summary inputs",
  "type": "object",
  "properties": {
    "attributes": {
      "lightning:type": "lightning__objectType",
      "properties": {
        "name": {"title": "Account name", "lightning:type": "lightning__textType"},
        "annualRevenue": {"title": "Revenue", "lightning:type": "lightning__numberType"}
      }
    }
  }
}
```

Field keywords include `title`, `description`, and `lightning:type`. Preserve numeric/Boolean data rather than converting every value to text. Composition tokens reference these UI input names, not uncontracted fields in the action output. See [type contracts](type-contracts.md).

## Bindings and formulas

`{!$attrs.name}` references a widget input. Renderer expressions reference properties in the Lightning type's data shape. Static strings and typed literals can coexist with expressions. HXL formulas use Salesforce formula-engine syntax: arithmetic, comparisons, logical operations, and supported functions. For example, `{!$attrs.subtotal * $attrs.taxRate}` computes from numeric inputs. Do not substitute JavaScript or assume every Salesforce formula function is available; verify unfamiliar functions and the result type on the target surface.

External image resources must be available without authentication. For MCP rendering, add their domain as an org Trusted URL, which provisions MCP CSP settings. [Image](components/image.md) documents raster formats, data URLs, signatures, and limits.

## Conditions and repeated content

`meta.if` must resolve to a Boolean. Missing/null references hide the node and its descendants. Numbers, strings, and arrays are not Boolean substitutes.

```json
{
  "definition": "tile/text",
  "meta": {
    "forEach": "{!$attrs.items}",
    "forItem": "$entry",
    "forIndex": "$entryIndex",
    "if": "{!$entry.isAvailable}"
  },
  "attributes": {"text": "{!$entry.name}"}
}
```

`forEach` references a collection; `forItem` defaults to `$Item`. Explicit item/index variables begin with `$`. Nested loops introduce scopes. Conditions referencing the current item filter per item; a condition referencing only `$attrs.showItems` gates the whole collection. Declare/map real collection data. The component docs name `lightning__listType`, but the linked base type reference does not publish its full schema in this snapshot. Do not invent list validation keywords.

## Actions

Button actions are arrays under `attributes.actions.click`. Predefined definitions are `action/openLink` with `attributes.url`, and `action/sendMessage` with `attributes.content`. See [interaction contracts](type-contracts.md#interactions). A message is processed by the host agent, not a direct Apex call; the corresponding follow-up action must be available to that agent.

## Scaffold helper

Only Python's standard library is required. Resolve script/spec paths relative to this skill folder:

```bash
python3 scripts/scaffold.py --project /tmp/hxl-demo --widget accountSummary \
  --channel agentforce --apex-type '@apexClassType/c__AccountSummaryResponse' \
  --spec assets/account-summary-spec.json
python3 scripts/validate.py /tmp/hxl-demo
```

`--channel static` generates literal sample values without a CLT. `agentforce` creates one Apex-backed CLT and direct mappings. `mcp` creates two object-based CLTs and nested mappings; use `--payload-property <actualInvocableOutputName>` (default `summary`). Agentforce/MCP require an existing or planned `--apex-type`; no Apex is generated or compiled.

Use `--source-dir` for the package path and `--type-name` for the CLT name. Existing `sfdx-project.json` is read, never overwritten; effective API version must be 67.0+. Fields accept `name`, `title`, `lightning:type`, `sample`, and optional dot-separated `dataPath` inside the Apex output object. Starter field types are text, multiline text, URL, number, integer, Boolean. Expand other documented contracts manually. Duplicate names, path traversal, and overwrites are rejected. A unique focused manifest is created under `manifest/`.

Sources: [composition](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-composition.html), [configuration](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-configuration.html), [schema](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-schema.html), [rich UI](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-rich-ui.html), [Agentforce mapping](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-example-mapping.html), [MCP mapping](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-example-mapping-mcp.html).
