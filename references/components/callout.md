# Callout: `tile/callout`

Use title plus description for a simple emphasized message; use children for richer content. iconAlt describes a meaningful status icon; omitted/empty alternatives make it decorative. Callouts accept nested components.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `description` | No | `lightning__textType` | Not listed |
| `iconAlt` | No | `lightning__textType` | Not listed |
| `title` | Yes | `lightning__textType` | Not listed |
| `variant` | No | `lightning__textType` | `default` |

## Allowed values

- `variant`: `default`, `error`, `info`, `note`, `success`, `tip`, `warning`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/callout",
  "attributes": {
    "title": "Review scheduled",
    "description": "Next meeting is on Friday",
    "variant": "info"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Callout reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/callout.html)
