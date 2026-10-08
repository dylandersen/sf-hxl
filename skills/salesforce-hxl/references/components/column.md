# Column: `tile/column`

Arrange children vertically; align controls their horizontal axis and gap spaces them. Width tokens may map to fixed extents or a 12-column grid: xs=3, sm=4, md=6, lg=8, xl=9. full fills the line; stretch shares remaining row space. Explicit align/gap avoid inconsistent source examples.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `align` | Yes | `lightning__alignmentType` | Not listed |
| `gap` | Yes | `lightning__gapType` | Not listed |
| `width` | No | `lightning__extentType` | Not listed |

## Allowed values

- `align`: `start`, `center`, `end`, `stretch`.
- `gap`: `none`, `xs`, `sm`, `md`, `lg`, `xl`.
- `width`: `auto`, `xs`, `sm`, `md`, `lg`, `xl`, `full`, `stretch`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/column",
  "attributes": {
    "align": "stretch",
    "gap": "md"
  },
  "children": []
}
```

Required/default inconsistencies are described in [troubleshooting](../troubleshooting.md#documentation-inconsistencies).

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Column reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/column.html)
