# Button: `tile/button`

Provide label and choose primary, secondary, or destructive. iconName uses a semantic icon identifier. Put action objects in attributes.actions.click as an array. Prefer one primary action in a group; use tile/link for navigation without an action payload. actions is an object in the working examples despite its text type in the property table.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `actions` | No | `lightning__textType` | Not listed |
| `iconName` | No | `lightning__iconName` | Not listed |
| `label` | Yes | `lightning__textType` | Not listed |
| `variant` | No | `lightning__textType` | `primary` |

## Allowed values

- `variant`: `primary`, `secondary`, `destructive`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/button",
  "attributes": {
    "label": "Review account",
    "variant": "secondary",
    "actions": {
      "click": [
        {
          "definition": "action/sendMessage",
          "attributes": {
            "content": "Show the account review options"
          }
        }
      ]
    }
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Button reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/button.html)
