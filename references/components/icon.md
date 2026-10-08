# Icon: `tile/icon`

Use a semantic name from the icon enumeration. Supply alt for informative icons (prefer under 125 characters); an empty/omitted alt is decorative. Pair with a text node in a centered row when a visible label is needed.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `alt` | No | `lightning__textType` | Not listed |
| `color` | No | `lightning__textType` | `default` |
| `name` | Yes | `lightning__iconName` | Not listed |
| `size` | No | `lightning__textType` | `md` |

## Allowed values

- `color`: `default`, `error`, `muted`, `primary`, `success`, `warning`.
- `size`: `xs`, `sm`, `md`, `lg`, `xl`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/icon",
  "attributes": {
    "name": "briefcase",
    "alt": "Business account"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Icon reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/icon.html)
