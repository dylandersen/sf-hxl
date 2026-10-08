# Code: `tile/code`

Put preformatted source in code, using escaped newlines and literal indentation. language is an optional label. For an inline technical identifier use text variant code; for formatted prose use markdown.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `code` | Yes | `lightning__multilineTextType` | Not listed |
| `language` | No | `lightning__textType` | Not listed |

## Surface behavior

Agentforce ignores language and displays monospace content without syntax highlighting. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/code",
  "attributes": {
    "code": "SELECT Id, Name FROM Account LIMIT 5",
    "language": "sql"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Code reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/code.html)
