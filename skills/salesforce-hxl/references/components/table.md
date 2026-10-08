# Table: `tile/table`

Supply caption, columns, and rows. Each column has key/header and optional align, columnType, isSortable, isFilterable. Row keys match column keys; missing keys display empty cells. Typed columns support dates, links, numbers, and picklists. pagination.pageSize divides rows; sort uses key/direction. Filters use text search, picklist choices, number ranges, or date ranges according to type. Numeric values should remain numeric/unformatted. See type-contracts.md for column object contracts.

## Attribute contract

| Attribute | Required in source table | Lightning type | Source table default |
| --- | --- | --- | --- |
| `appearance` | No | `lightning__textType` | `default` |
| `caption` | Yes | `lightning__textType` | Not listed |
| `columns` | Yes | `lightning__listType` | Not listed |
| `isStickyHeader` | No | `lightning__booleanType` | `false` |
| `pagination` | No | `lightning__objectType` | Not listed |
| `rows` | Yes | `lightning__listType` | Not listed |
| `size` | No | `lightning__textType` | `md` |
| `sort` | No | `lightning__objectType` | Not listed |

## Allowed values

- `appearance`: `default`, `bordered`, `striped`.
- `size`: `sm`, `md`.

## Surface behavior

Agentforce sorting/filtering need imperative handlers; pagination needs manual row slicing, not a built-in control. The source also records no known Slackbot/ChatGPT limitations; it does not separately enumerate Claude limitations. These statements are documentation coverage, not a runtime test.

## Composition example

```json
{
  "definition": "tile/table",
  "attributes": {
    "caption": "Accounts due for review",
    "columns": [
      {
        "key": "name",
        "header": "Account"
      },
      {
        "key": "revenue",
        "header": "Revenue",
        "align": "right",
        "columnType": {
          "type": "number",
          "format": "currency",
          "currencyCode": "USD"
        }
      }
    ],
    "rows": [
      {
        "name": "Acme",
        "revenue": 125000
      }
    ]
  }
}
```

[Type contracts](../type-contracts.md) · [Component index](../components.md) · [Official Table reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/table.html)
