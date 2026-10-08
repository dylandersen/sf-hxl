# Container: `tile/container`

Frame related children with a padded rounded region. Use a row/column inside for layout. borderless removes the border; use a bare row/column when no frame is needed. Variants convey neutral emphasis or semantic state.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `borderless` | No | `lightning__booleanType` | `false` |
| `variant` | No | `lightning__textType` | `default` |

## Allowed values

- `variant`: `default`, `emphasis`, `info`, `warning`, `error`, `success`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/container",
  "attributes": {
    "variant": "emphasis"
  },
  "children": []
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Container reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/container.html)
