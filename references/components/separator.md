# Separator: `tile/separator`

Use horizontal inside columns and vertical inside rows. The visible divider inherits its length from the parent. Use spacer when separation should be invisible.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `orientation` | No | `lightning__textType` | `horizontal` |

## Allowed values

- `orientation`: `horizontal`, `vertical`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/separator",
  "attributes": {
    "orientation": "horizontal"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Separator reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/separator.html)
