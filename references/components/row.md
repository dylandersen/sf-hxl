# Row: `tile/row`

Arrange children horizontally; gap spaces them, align controls the cross-axis, justify distributes width, and isWrapped defaults true. Place columns inside a row for multi-column layouts; stretch lets a column consume remaining width.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `align` | No | `lightning__alignmentType` | `center` |
| `gap` | Yes | `lightning__gapType` | Not listed |
| `isWrapped` | No | `lightning__booleanType` | `true` |
| `justify` | No | `lightning__textType` | `start` |

## Allowed values

- `align`: `start`, `center`, `end`, `stretch`.
- `gap`: `none`, `xs`, `sm`, `md`, `lg`, `xl`.
- `justify`: `start`, `center`, `end`, `between`, `around`, `evenly`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/row",
  "attributes": {
    "gap": "sm",
    "align": "center",
    "justify": "between"
  },
  "children": []
}
```

Required/default inconsistencies are described in [troubleshooting](../troubleshooting.md#documentation-inconsistencies).

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Row reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/row.html)
