# Text: `tile/text`

Plain text only: markup is removed. Use semantic heading/caption/code variants and status colors; isItalic/isStrikethrough and weight modify emphasis. For rich content choose markdown. Styling can differ across surfaces.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `color` | No | `lightning__textType` | `default` |
| `isItalic` | No | `lightning__booleanType` | `false` |
| `isStrikethrough` | No | `lightning__booleanType` | `false` |
| `text` | Yes | `lightning__multilineTextType` | Not listed |
| `variant` | No | `lightning__textType` | `body` |
| `weight` | No | `lightning__textType` | Not listed |

## Allowed values

- `variant`: `body`, `caption`, `code`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/text",
  "attributes": {
    "text": "Account overview",
    "variant": "h2"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Text reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/text.html)
