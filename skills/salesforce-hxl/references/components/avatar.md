# Avatar: `tile/avatar`

Provide src, initials, or iconName. An image takes priority; initials are the text fallback. Use a circle for a person, square for an object/organization, and rounded for a hybrid entity. Initials normally use two characters (the source allows up to three Unicode characters). Keep alt within 125 characters. Apply the raster/public-resource restrictions from image.md.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `alt` | No | `lightning__textType` | Not listed |
| `iconName` | No | `lightning__iconName` | Not listed |
| `initials` | No | `lightning__textType` | Not listed |
| `shape` | No | `lightning__textType` | `circle` |
| `size` | No | `lightning__textType` | `md` |
| `src` | No | `lightning__urlType` | Not listed |

## Allowed values

- `shape`: `circle`, `square`, `rounded`.
- `size`: `xs`, `sm`, `md`, `lg`, `xl`.

## Surface behavior

Agentforce maps xl to large; rounded falls back to square with custom CSS. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/avatar",
  "attributes": {
    "initials": "AC",
    "alt": "Account team"
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Avatar reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/avatar.html)
