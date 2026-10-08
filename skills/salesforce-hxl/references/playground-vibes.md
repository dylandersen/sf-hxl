# Playground and Agentforce Vibes

## Playground authoring

The HXL Playground lets you edit component/widget JSON beside a native-surface preview. Use the Components catalog to search by name, inspect properties, and switch surfaces. Components carry Beta or Developer Preview badges; preview APIs can change and the guide recommends sandbox evaluation. The platform's 22 documented beta components are indexed [locally](components.md); additional Playground entries are not implicitly deployable platform contracts.

On the Widgets page, choose **New widget**, then a template or scratch composition. Edit the title to update the API name. **My Widgets** auto-save in browser local storage. Examples/prebuilt widgets are read-only: **Save** creates a personal copy. **Clone** creates an independent copy of either a personal widget or an example.

**Share** encodes the widget definition in a link, so recipients do not need the author's browser storage. Opening a share link imports it; same-name conflicts offer update, copy, open-existing, or cancel. **Delete** removes personal widgets permanently, while examples cannot be deleted. Copy JSON or keep a share link before deliberate deletion. Never put real confidential data or credentials in publicly shareable mock definitions.

Local storage is per origin/profile and can be cleared/evicted. A different machine, browser, profile, or incognito window does not share it. Copy composition JSON into source-controlled bundles; browser persistence is not a deployment or source backup.

The linked tutorial entry covers incremental examples such as hello world and formulas. It is an external Playground resource, not part of the HXL platform-doc navigation snapshot. Use local authoring examples for offline generation; live Playground previews require the site.

## Vibes workflow

Agentforce Vibes runs within the Salesforce VS Code Extension Pack, with a Salesforce DX project, CLI, authorized org, and configured AI provider. Git checkpoints and telemetry are additional extension features; Windows installation may require the documented Visual C++ runtime.

The official HXL workflow invokes `platform-widget-generate` to draft all three UiWidgetBundle files. Describe the desired UI inputs, including types and interactions. Existing local CLT schemas can provide data shape. The generator does not scan the org for widget discovery, recommend duplicates, or bulk-edit multiple widgets. Semantic component styling is used instead of pixels.

For Apex-backed work, establish the supporting Apex data class and generate a CLT first. The documented `platform-custom-lightning-type-generate` workflow can reference an existing org Apex class; missing Apex requires creating the supporting class separately. Then ask Vibes for a widget for that CLT. Review schema/composition/XML and root renderer mappings before deployment. Deploy Apex, widgets, then CLTs, or a dependency-complete package.

Vibe coding an MCP server is explicitly unsupported in the HXL Vibes guide snapshot. Use [MCP's manual metadata workflow](mcp.md) rather than promising automatic server creation. This skill's local scaffold supports metadata drafting independently of the Vibes extension and other skills.

Useful requests:

- Create an account-summary HXL widget with typed revenue, a status badge, and a follow-up button for an existing output CLT.
- Convert this existing widget into a repeated list; preserve the action data contract and provide empty-state handling.
- Connect this widget to an Apex invocable MCP tool using a wrapper/payload pair and show the remaining server-resource changes.

Sources: [Playground](https://developer.salesforce.com/docs/platform/hxl/guide/playground.html), [widgets](https://developer.salesforce.com/docs/platform/hxl/guide/playground-widgets.html), [components](https://developer.salesforce.com/docs/platform/hxl/guide/playground-components.html), [HXL Vibes](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-vibes.html), [Vibes installation](https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-get-started.html), [Vibes overview](https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-overview.html), [CLT Vibes](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-skills.html).
