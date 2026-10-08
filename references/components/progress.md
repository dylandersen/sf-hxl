# Progress: `tile/progress`

Read-only measurable progress: omit max for percentage values, or provide max for a target/quota. Label names the operation. shape selects a bar or ring; color conveys status with a textual alternative. Explicit size avoids inconsistent source examples.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `color` | No | `lightning__textType` | `default` |
| `label` | Yes | `lightning__textType` | Not listed |
| `max` | No | `lightning__numberType` | Not listed |
| `shape` | No | `lightning__textType` | `linear` |
| `size` | Yes | `lightning__sizeType` | Not listed |
| `value` | No | `lightning__numberType` | `0` |

## Allowed values

- `color`: `default`, `error`, `primary`, `success`, `warning`.
- `shape`: `linear`, `circular`.
- `size`: `xs`, `sm`, `md`, `lg`, `xl`.

## Surface behavior

Agentforce natively supports success color; error/warning rely on CSS overrides. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/progress",
  "attributes": {
    "label": "Onboarding",
    "value": 2,
    "max": 5,
    "size": "md"
  }
}
```

Required/default inconsistencies are described in [troubleshooting](../troubleshooting.md#documentation-inconsistencies).

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Progress reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/progress.html)
