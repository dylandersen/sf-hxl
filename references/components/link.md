# Link: `tile/link`

href supplies the destination; text defaults to the URL when omitted. underline controls hover/always/none; variant controls emphasis. Give links descriptive text. Use button for agent/business actions.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `href` | Yes | `lightning__urlType` | Not listed |
| `text` | No | `lightning__textType` | Not listed |
| `underline` | No | `lightning__textType` | `hover` |
| `variant` | No | `lightning__textType` | `primary` |

## Allowed values

- `underline`: `always`, `hover`, `none`.
- `variant`: `default`, `muted`, `primary`.

## Surface behavior

Agentforce ignores variant and underline. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/link",
  "attributes": {
    "href": "https://example.com/account",
    "text": "View account"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Link reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/link.html)
