# Documentation sources and coverage

Snapshot: **2026-10-08**, HXL beta, API **67.0+**. This self-contained skill reconstructs the implementation-relevant contracts and workflows in local references, with original examples and helpers. It does not require the source site at runtime. Raw HTML, marketing navigation, screenshots, and sample archives are not copied into the skill.

Coverage: **21/21 HXL guide pages**, **25/25 HXL reference pages** (including all **22 component contracts** and **19 HXL Lightning types**), plus **23 supporting platform pages**. Two landing/navigation endpoints were also inspected. Duplicate glossary/landing topics are consolidated rather than loaded twice.

The scope is the complete HXL platform guide/reference tree, not all Salesforce product documentation. External Playground tutorials, release notes, Help articles, ZIP sample downloads, generic Apex manuals, and the rest of linked product manuals are pointers beyond this snapshot. Their HXL requirements are distilled locally where the HXL guide provides them. Screenshots are replaced by usable configuration steps. Every sampled HXL navigation topic routes below to local content.

[provenance.json](provenance.json) records official URLs, raw-source hashes, scope, capture date, and local routes. Repo maintenance checks source freshness independently from authoring; a dated offline snapshot is not a claim that the beta never changes.

## HXL developer guide

| Official page | Offline reference |
| --- | --- |
| [Build a Rich UI for Agentforce Action Output](https://developer.salesforce.com/docs/platform/hxl/guide/agentforce-action-output.html) | [Local guide](agentforce.md) |
| [Get Started](https://developer.salesforce.com/docs/platform/hxl/guide/get-started.html) | [Local guide](../SKILL.md) |
| [Create the Apex Invocable Action](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-apex.html) | [Local guide](mcp.md#invocable-action) |
| [Build a Rich UI for External Agents](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-channels.html) | [Local guide](mcp.md) |
| [Create a Custom MCP Server](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-server.html) | [Local guide](mcp.md#configure-server-resources) |
| [Connect Your MCP Client to Your Org](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-setup-client.html) | [Local guide](mcp.md#connect-and-verify-clients) |
| [Set Up Your Org for MCP Access](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-setup-org.html) | [Local guide](org-deployment.md#mcp-oauth-and-access) |
| [Release Notes](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-release-notes.html) | [Local guide](troubleshooting.md#documentation-inconsistencies) |
| [Learn About HXL](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-rich-ui.html) | [Local guide](authoring.md) |
| [Use Agentforce Vibes to Build Widgets](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-vibes.html) | [Local guide](playground-vibes.md#vibes-workflow) |
| [Composition File](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-composition.html) | [Local guide](authoring.md) |
| [Widget Configuration File](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-configuration.html) | [Local guide](authoring.md#bundle-files) |
| [Mapping a Hotel Card Widget for MCP](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-example-mapping-mcp.html) | [Local guide](mcp.md) |
| [Mapping a Hotel Card Widget for Agentforce](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-example-mapping.html) | [Local guide](agentforce.md) |
| [Widget Example](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-example.html) | [Local guide](authoring.md) |
| [Schema File](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-schema.html) | [Local guide](authoring.md#attribute-schema) |
| [Glossary](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widgets-glossary.html) | [Local guide](type-contracts.md#terminology) |
| [Use HXL Components](https://developer.salesforce.com/docs/platform/hxl/guide/playground-components.html) | [Local guide](playground-vibes.md#playground-authoring) |
| [Create Widgets](https://developer.salesforce.com/docs/platform/hxl/guide/playground-widgets.html) | [Local guide](playground-vibes.md#playground-authoring) |
| [Explore Widgets in HXL Playground](https://developer.salesforce.com/docs/platform/hxl/guide/playground.html) | [Local guide](playground-vibes.md) |
| [Prerequisites](https://developer.salesforce.com/docs/platform/hxl/guide/prerequisites.html) | [Local guide](org-deployment.md#hxl-prerequisites) |

## HXL reference

| Official page | Offline reference |
| --- | --- |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/about-hxl-components.html) | [Local guide](components.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/accordion.html) | [Local guide](components/accordion.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/accordionItem.html) | [Local guide](components/accordionItem.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/avatar.html) | [Local guide](components/avatar.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/badge.html) | [Local guide](components/badge.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/button.html) | [Local guide](components/button.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/callout.html) | [Local guide](components/callout.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/code.html) | [Local guide](components/code.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/column.html) | [Local guide](components/column.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/container.html) | [Local guide](components/container.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/hxl-lightning-types.html) | [Local guide](type-contracts.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/hxl-widgets-glossary.html) | [Local guide](type-contracts.md#terminology) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/icon.html) | [Local guide](components/icon.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/image.html) | [Local guide](components/image.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/link.html) | [Local guide](components/link.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/list.html) | [Local guide](components/list.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/listItem.html) | [Local guide](components/listItem.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/markdown.html) | [Local guide](components/markdown.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/progress.html) | [Local guide](components/progress.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/row.html) | [Local guide](components/row.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/separator.html) | [Local guide](components/separator.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/spacer.html) | [Local guide](components/spacer.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/spinner.html) | [Local guide](components/spinner.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/table.html) | [Local guide](components/table.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references/hxl-reference-about/text.html) | [Local guide](components/text.md) |

## Supporting platform implementation docs

| Official page | Offline reference |
| --- | --- |
| [Get Started](https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-get-started.html) | [Local guide](playground-vibes.md#vibes-workflow) |
| [Agentforce Vibes Overview](https://developer.salesforce.com/docs/platform/agentforcevibes/guide/afv-overview.html) | [Local guide](playground-vibes.md#vibes-workflow) |
| [Configure ChatGPT](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/chatgpt.html) | [Local guide](mcp.md#connect-and-verify-clients) |
| [Configure Claude](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/claude.html) | [Local guide](mcp.md#connect-and-verify-clients) |
| [Get Started](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/hosted-mcp-servers-overview.html) | [Local guide](mcp.md) |
| [Invocable Actions](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/invocable-actions.html) | [Local guide](mcp.md#invocable-action) |
| [Set Up Your Org](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/setup-overview.html) | [Local guide](org-deployment.md#mcp-oauth-and-access) |
| [Apex-Based Custom Lightning Types](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-apex.html) | [Local guide](agentforce.md#new-apex-data-types) |
| [Core Concepts of Custom Lightning Types](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-core.html) | [Local guide](type-contracts.md#custom-lightning-type-contracts) |
| [Object-Based Custom Lightning Types](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-object.html) | [Local guide](type-contracts.md#custom-lightning-type-contracts) |
| [Use Agentforce Vibes to Build Custom Lightning Types](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-skills.html) | [Local guide](playground-vibes.md#vibes-workflow) |
| [Get Started with Lightning Types](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types.html) | [Local guide](type-contracts.md) |
| [Lightning Types](https://developer.salesforce.com/docs/platform/lightning-types/references/lightning-types/lightning-types-glossary.html) | [Local guide](type-contracts.md#terminology) |
| [Lightning Types](https://developer.salesforce.com/docs/platform/lightning-types/references/lightning-types/lightning-types-reference.html) | [Local guide](type-contracts.md#scalar-and-object-inputs) |
| [project Commands](https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project.html) | [Local guide](org-deployment.md#cli-operations) |
| [Create an External Client App](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html) | [Local guide](org-deployment.md#mcp-oauth-and-access) |
| [Log Into Your Org](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/log-into-org.html) | [Local guide](org-deployment.md#mcp-oauth-and-access) |
| [Activate MCP Servers](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/activate-mcp-servers.html) | [Local guide](org-deployment.md#mcp-oauth-and-access) |
| [Build Custom MCP Servers](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/custom-servers.html) | [Local guide](mcp.md) |
| [Test MCP Clients](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/test-connection.html) | [Local guide](troubleshooting.md#diagnose-by-layer) |
| [Server Connection Failures](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/connection-issues.html) | [Local guide](troubleshooting.md#diagnose-by-layer) |
| [Authentication Issues](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/authentication-issues.html) | [Local guide](troubleshooting.md#diagnose-by-layer) |
| [Prompt Run Failures](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/execution-issues.html) | [Local guide](troubleshooting.md#diagnose-by-layer) |

## Navigation discovery

| Official page | Offline reference |
| --- | --- |
| [Headless Experience Layer](https://developer.salesforce.com/docs/platform/hxl/overview) | [Local guide](sources.md) |
| [Headless Experience Layer (HXL) Reference](https://developer.salesforce.com/docs/platform/hxl/references) | [Local guide](sources.md) |

## Source interpretation

The local authoring examples replace the source hotel scenario with an account-summary scenario. Source data shapes and metadata identifiers are preserved; prose is distilled rather than duplicated. Component property names, Lightning types, defaults, enum values, and surface caveats remain available locally. Source contradictions are explicitly listed in [troubleshooting](troubleshooting.md#documentation-inconsistencies). No live org deployment or client rendering was performed while creating this skill.
