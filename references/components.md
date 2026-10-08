# HXL component index

The platform reference publishes these 22 beta components. `tile/widget` is the separately documented composition root. Read only the individual contracts you need. Additional Playground developer-preview components require live support verification before deployment.

| Definition | Use | Local reference |
| --- | --- | --- |
| `tile/accordion` | Group collapsible sections with direct tile/accordionItem children | [accordion](components/accordion.md) |
| `tile/accordionItem` | Use only as a direct child of tile/accordion | [accordionItem](components/accordionItem.md) |
| `tile/avatar` | Provide src, initials, or iconName | [avatar](components/avatar.md) |
| `tile/badge` | Short status/category labels are display-only | [badge](components/badge.md) |
| `tile/button` | Provide label and choose primary, secondary, or destructive | [button](components/button.md) |
| `tile/callout` | Use title plus description for a simple emphasized message; use children for richer content | [callout](components/callout.md) |
| `tile/code` | Put preformatted source in code, using escaped newlines and literal indentation | [code](components/code.md) |
| `tile/column` | Arrange children vertically; align controls their horizontal axis and gap spaces them | [column](components/column.md) |
| `tile/container` | Frame related children with a padded rounded region | [container](components/container.md) |
| `tile/icon` | Use a semantic name from the icon enumeration | [icon](components/icon.md) |
| `tile/image` | Always provide alt (empty only for decoration) and src | [image](components/image.md) |
| `tile/link` | href supplies the destination; text defaults to the URL when omitted | [link](components/link.md) |
| `tile/list` | Direct children are tile/listItem, whose own children carry content | [list](components/list.md) |
| `tile/listItem` | Place inside tile/list | [listItem](components/listItem.md) |
| `tile/markdown` | Use source for CommonMark/GFM formatted content, escaping newlines in JSON | [markdown](components/markdown.md) |
| `tile/progress` | Read-only measurable progress: omit max for percentage values, or provide max for a target/quota | [progress](components/progress.md) |
| `tile/row` | Arrange children horizontally; gap spaces them, align controls the cross-axis, justify distributes width, and isWrapped defaults true | [row](components/row.md) |
| `tile/separator` | Use horizontal inside columns and vertical inside rows | [separator](components/separator.md) |
| `tile/spacer` | Invisible fixed-size space, or fill to absorb available main-axis space | [spacer](components/spacer.md) |
| `tile/spinner` | Indeterminate loading needs an accessible label describing the operation | [spinner](components/spinner.md) |
| `tile/table` | Supply caption, columns, and rows | [table](components/table.md) |
| `tile/text` | Plain text only: markup is removed | [text](components/text.md) |

Property/type/default facts are also stored in [component-contracts.json](component-contracts.json) for the local validator. The source tables and examples disagree on a few defaults; see [troubleshooting](troubleshooting.md#documentation-inconsistencies). Collection cells, actions, layout enums, and icons are defined in [type contracts](type-contracts.md).

Source: [HXL Components](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/about-hxl-components.html).
