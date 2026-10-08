# List Tile: `tile/list`

Direct children are tile/listItem, whose own children carry content. Marker is none, bullet, or number. The source recommends 1–10 items (a design recommendation, not a demonstrated platform limit). Multiple children within an item form a horizontal row.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `marker` | No | `lightning__textType` | `none` |

## Allowed values

- `marker`: `none`, `bullet`, `number`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/list",
  "attributes": {
    "marker": "bullet"
  },
  "children": [
    {
      "definition": "tile/listItem",
      "children": [
        {
          "definition": "tile/text",
          "attributes": {
            "text": "Renewal review"
          }
        }
      ]
    }
  ]
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official List Tile reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/list.html)
