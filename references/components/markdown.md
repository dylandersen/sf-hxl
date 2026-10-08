# Markdown: `tile/markdown`

Use source for CommonMark/GFM formatted content, escaping newlines in JSON. Task-list checkboxes are unsupported. Inline HTML may be stripped; do not rely on it. Use code for source listings and text for plain text.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `source` | Yes | `lightning__markdownTextType` | Not listed |

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/markdown",
  "attributes": {
    "source": "## Account review\n\nReview the renewal plan."
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Markdown reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/markdown.html)
