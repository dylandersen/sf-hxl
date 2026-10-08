# List Item: `tile/listItem`

Place inside tile/list. Its child content uses tile/text, tile/link, and tile/icon. Spacing and markers belong to the parent list; this item has no attributes.

## Attribute contract

No component attributes are documented. Provide content through children.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
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
```

This fragment must be placed inside a list.

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official List Item reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/listItem.html)
