# Spacer: `tile/spacer`

Invisible fixed-size space, or fill to absorb available main-axis space. In a row it acts horizontally; in a column vertically. Prefer parent gap for regular spacing between every sibling.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `size` | No | `lightning__textType` | `md` |

## Allowed values

- `size`: `xs`, `sm`, `md`, `lg`, `xl`, `fill`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/spacer",
  "attributes": {
    "size": "fill"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Spacer reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/spacer.html)
