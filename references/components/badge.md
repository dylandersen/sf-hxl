# Badge: `tile/badge`

Short status/category labels are display-only. Use a button/link for interaction. Semantic status variants should communicate actual status; outline is quieter than primary.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `label` | Yes | `lightning__textType` | Not listed |
| `variant` | No | `lightning__textType` | `secondary` |

## Allowed values

- `variant`: `error`, `info`, `outline`, `primary`, `secondary`, `success`, `warning`.

## Surface behavior

Agentforce needs SLDS styling hooks for semantic colors; otherwise status badges can remain gray. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/badge",
  "attributes": {
    "label": "Active",
    "variant": "success"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Badge reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/badge.html)
