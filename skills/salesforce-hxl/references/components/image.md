# Image: `tile/image`

Always provide alt (empty only for decoration) and src. External resources must be public; MCP needs the domain as a Trusted URL. Raster MIME formats: PNG, JPEG, GIF, WebP. SVG, BMP, active/non-image/omitted media types are excluded. Data URLs must be data:<mediatype>;base64,<payload>, match the declared MIME magic bytes, decode to at most 8 MiB, and contain no unresolved expressions in MIME/payload slots. data: is not supported for link href. Size preserves aspect ratio; full fills parent width, auto keeps intrinsic dimensions.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `alt` | Yes | `lightning__textType` | Not listed |
| `size` | No | `lightning__textType` | `auto` |
| `src` | Yes | `lightning__urlType` | Not listed |

## Allowed values

- `size`: `auto`, `sm`, `md`, `lg`, `full`.

## Surface behavior

The source records no known Agentforce limitations for this component. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/image",
  "attributes": {
    "src": "https://example.com/account.png",
    "alt": "Account logo",
    "size": "sm"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Image reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/image.html)
