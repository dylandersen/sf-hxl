# Accordion: `tile/accordion`

Group collapsible sections with direct tile/accordionItem children. Set isExpanded on an item to open it initially. Put richer section content inside a column.

## Attribute contract

No component attributes are documented. Provide content through children.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/accordion",
  "children": [
    {
      "definition": "tile/accordionItem",
      "attributes": {
        "title": "Account details"
      },
      "children": [
        {
          "definition": "tile/text",
          "attributes": {
            "text": "Regional account"
          }
        }
      ]
    }
  ]
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Accordion reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/accordion.html)
