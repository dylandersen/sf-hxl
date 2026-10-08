# Spinner: `tile/spinner`

Indeterminate loading needs an accessible label describing the operation. Use progress instead when completion is measurable. Pair a spinner with explanatory text in a row when useful.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `label` | Yes | `lightning__textType` | Not listed |
| `size` | No | `lightning__textType` | `md` |

## Allowed values

- `size`: `xs`, `sm`, `md`, `lg`, `xl`.

## Surface behavior

Agentforce renders xl at the lg size. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/spinner",
  "attributes": {
    "label": "Loading account summary",
    "size": "sm"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Spinner reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/spinner.html)
