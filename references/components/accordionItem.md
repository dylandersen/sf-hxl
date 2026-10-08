# Accordion Item: `tile/accordionItem`

Use only as a direct child of tile/accordion. Supply a title; subtitle adds a preview line. iconAlt explains a meaningful header icon; omit it for a decorative icon. isExpanded controls the initial section state.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `iconAlt` | No | `lightning__textType` | Not listed |
| `iconName` | No | `lightning__iconName` | Not listed |
| `isExpanded` | No | `lightning__booleanType` | `false` |
| `subtitle` | No | `lightning__textType` | Not listed |
| `title` | Yes | `lightning__textType` | Not listed |

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/accordionItem",
  "attributes": {
    "title": "Account details",
    "isExpanded": true
  }
}
```

This fragment must be placed inside an accordion.

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Accordion Item reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/accordionItem.html)
