# Lightning type contracts for HXL

Contents: scalar/widget types; layout enumerations; icons; interactions; typed table values; CLT structure and changes; terminology.

## Scalar and object inputs

Widget attributes and component properties use Lightning type names; they are not HTML attribute types. Preserve JSON values of the corresponding shape. The linked base reference publishes the following facts (its broader input/editor surface support must not be mistaken for HXL support).

| Type | Value/constraints | Configurable keywords beyond title/description |
| --- | --- | --- |
| lightning__booleanType | Boolean | None listed |
| lightning__textType | String, up to 255 characters | minLength, maxLength |
| lightning__multilineTextType | Longer string | minLength, maxLength |
| lightning__markdownTextType | Markdown string | None listed |
| lightning__integerType | Whole number | minimum, maximum |
| lightning__numberType | Decimal number | minimum, maximum, multipleOf (documented default 1.0E-32) |
| lightning__urlType | URL string | lightning:allowedUrlSchemes, an array such as https/http/mailto |
| lightning__dateType | yyyy-mm-dd string | None listed |
| lightning__dateTimeStringType | ISO 8601 string | None listed |
| lightning__dateTimeType | Object with required dateTime and optional IANA timeZone | None listed |
| lightning__timeType | HH:MM:SS or HH:MM:SS.000Z | None listed |
| lightning__richTextType | Rich-text string, up to 100,000 characters | minLength/maxLength (minimum counts markup) |
| lightning__objectType | Typed properties object | Properties define nested Lightning type fields |
| lightning__listType | Collection; named by component property tables | Complete base schema not published in linked snapshot |

`title` is required in the base scalar reference's configurable keyword tables; description is optional. Rich text is not a way to insert arbitrary HTML into a tile/text composition. Prefer the HXL component's declared property type.

## Layout and display enumerations

The following HXL types are string enums. Component-specific defaults/allowed values can be narrower and take precedence.

| Type | Values | Default |
| --- | --- | --- |
| lightning__alignmentType | start, center, end, stretch | stretch |
| lightning__extentType | auto, xs, sm, md, lg, xl, full, stretch | auto |
| lightning__gapType | none, xs, sm, md, lg, xl | md |
| lightning__sizeType | xs, sm, md, lg, xl | md |
| lightning__orientationType | horizontal, vertical | horizontal |
| lightning__justifyType | start, center, end, between, around, evenly; aliases space-between, space-around, space-evenly | start |
| lightning__positionType | top, right, bottom, left | top |
| lightning__textalignType | left, center, right | left |
| lightning__severityType | info, success, warning, error | info |

## Icons

`lightning__iconName` is a semantic identifier mapped to native icons by each renderer, not an SLDS sprite path. The full documented enum is in [icon-names.json](icon-names.json). Select an identifier from it for an offline artifact; do not assume arbitrary Lucide or SLDS names are accepted.

## Interactions

`lightning__actionType` is an object with required `definition` and `attributes`. Published predefined action payloads:

| Definition | Required payload | Behavior |
| --- | --- | --- |
| action/openLink | attributes.url, string | Opens the URL synchronously in the user-gesture context |
| action/sendMessage | attributes.content, string | Sends a message to the host/agent for processing |

```json
{
  "definition": "tile/button",
  "attributes": {
    "label": "Review renewal",
    "variant": "secondary",
    "actions": {
      "click": [{
        "definition": "action/sendMessage",
        "attributes": {"content": "Review the renewal plan for this account"}
      }]
    }
  }
}
```

A sendMessage request goes to the agent, rather than being shown as a user-authored visible message; the agent can request confirmation according to its action rules. An action payload is not an authorization bypass.

`lightning__eventType` separately describes an event: required string definition (maximum 255 characters) and optional attributes object allowing event-specific properties. A custom event identifier does not itself establish a handler. The action type prose mentions local actions, but only openLink/sendMessage are fully specified; supply/verify an actual handler before using other definitions.

## Table types

Read [table](components/table.md) for component properties and surface limitations. `lightning__cellValueType` admits one string (up to 255 characters) or one number at a time. Each columnType is a discriminated object, not a Lightning schema reference embedded as the discriminator.

| HXL Lightning type | Required shape | Optional configuration |
| --- | --- | --- |
| lightning__dateColumnType | type: date | format date/datetime (date default); dateStyle/timeStyle full/long/medium/short (short default); timeStyle only with datetime |
| lightning__numberColumnType | type: number | format decimal/percent/currency (decimal default); currencyCode (USD default), currencyCodeKey, currencyDisplayAs symbol/narrowSymbol/code/name; minimumFractionDigits/maximumFractionDigits integers 0–20 |
| lightning__linkColumnType | type: link | urlKey points at the URL field, otherwise the cell value is both label and URL |
| lightning__picklistColumnType | type: picklist; nonempty options array | Each option uses lightning__picklistOptionType |
| lightning__picklistOptionType | label and value strings, each at most 255 characters | value is unique within the options array |

Dates accept ISO 8601 strings or Unix milliseconds; unparseable values display plain text. Numbers accept unformatted numeric values/strings; invalid numbers also fall back to text. currencyCodeKey selects a per-row ISO 4217 code, falling back to currencyCode. Picklists map canonical stored values to labels; unmatched values display raw text.

Example column definition (inside a table's columns array):

```json
{
  "key": "annualRevenue",
  "header": "Annual revenue",
  "align": "right",
  "isSortable": true,
  "columnType": {
    "type": "number",
    "format": "currency",
    "currencyCode": "USD",
    "maximumFractionDigits": 0
  }
}
```

Do not promise imperative table behaviors from declarative flags on Agentforce; see [table surface behavior](components/table.md#surface-behavior).

## Custom Lightning type contracts

Bundles live in `lightningTypes/<name>`. A schema has a title and a lightning:type. Apex schemas reference the fully qualified class and inherit @AuraEnabled fields. Object schemas explicitly declare lightning__objectType and typed properties, with optional required names; updating an object type generates a corresponding Apex class automatically.

Local metadata references use `c__<name>` even in an org with a registered namespace; widget references use `@widget/c/<name>`. Managed-package references use the actual package namespace. Custom labels can localize titles/descriptions with `{!$Label.c.<LabelName>}`; use actual existing label metadata and inspect the source syntax if incorporating it.

HXL renderers sit at the root, unlike LWC input/output overrides in application-specific directories. General CLT supports more application channels and LWC editor/collection overrides; those capabilities do not automatically apply to HXL widget rendering. [Agentforce](agentforce.md) and [MCP](mcp.md) provide the HXL configurations.

For an object type already used by an application, compatible edits are optional property additions, title/description edits, relaxing required names/length/numeric bounds, adding allowed URL schemes, or a multipleOf divisor of the previous step. Removing/renaming fields, changing lightning:type, adding required fields, or tightening validation can break existing references. Apex type changes have separate guidance in [Agentforce](agentforce.md#new-apex-data-types).

## Terminology

Attribute contract means the widget's accepted UI inputs. Data shape means the CLT/action output. Component means a single declarative layout/content node. Composition means the ordered component hierarchy. Root means tile/widget. Channel names the application; surface names its particular device/UI context. Wrapper and payload describe the two MCP object-type roles. These terms do not introduce additional metadata categories. Conditions and iteration are meta rendering behaviors; renderer attribute mapping connects data shape to UI inputs.

Sources: [HXL Lightning Types](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/hxl-lightning-types.html), [base types](https://developer.salesforce.com/docs/platform/lightning-types/references/lightning-types/lightning-types-reference.html), [object CLTs](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-object.html), [core CLTs](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-core.html), [HXL glossary](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widgets-glossary.html), [Lightning glossary](https://developer.salesforce.com/docs/platform/lightning-types/references/lightning-types/lightning-types-glossary.html).
