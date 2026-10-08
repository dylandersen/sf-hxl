---
name: salesforce-hxl
description: Create, connect, deploy, and troubleshoot Salesforce Headless Experience Layer (HXL) JSON widgets, UiWidgetBundles, and Lightning type renderers for Agentforce or hosted MCP clients such as ChatGPT, Claude, and Slackbot. Use for HXL authoring and integration, including formulas, repeated content, interactive actions, and platform component selection.
---

# Salesforce HXL

Build source-based HXL experiences from the local references. This bundle distills the complete HXL guide and component-reference navigation plus implementation dependencies, captured 2026-10-08. Read selectively; use [sources](references/sources.md) for coverage and official URLs. No source checkout, SSO, or network is needed to author from this snapshot. HXL is beta, requiring API 67.0 or later.

## Choose the workflow

| Task | Read |
| --- | --- |
| Author bundles, bindings, formulas, conditions, or iteration | [Authoring](references/authoring.md) |
| Select exact components, properties, or surface differences | [Component index](references/components.md), then only the needed component files |
| Choose types, enums, action payloads, or table columns | [Type contracts](references/type-contracts.md) |
| Connect Agentforce output and follow-up buttons | [Agentforce](references/agentforce.md) |
| Expose invocable output on ChatGPT, Claude, or Slackbot | [MCP](references/mcp.md) |
| Set up, authenticate, deploy, retrieve, or package | [Org/deployment](references/org-deployment.md) |
| Preview, share, import, or use Agentforce Vibes | [Playground/Vibes](references/playground-vibes.md) |
| Diagnose rendering, binding, access, or channel problems | [Troubleshooting](references/troubleshooting.md) |

## Produce useful artifacts

Inspect existing DX package directories, API version, action output, and target surface. Preserve the user's names and design choices. For source-only work, produce bundles and exact remaining org configuration steps. Deploy/configure an org when within the user's request and an actual target is known.

For a new bundle, see the [scaffold helper](references/authoring.md#scaffold-helper). `scripts/scaffold.py` creates widget metadata, optional Agentforce/MCP type bundles, and a focused manifest from an attribute specification. It writes new files only and never contacts Salesforce. Adapt its composition to the requested experience; the helper does not prescribe the design.

Keep widget inputs flat. Place HXL `renderer.json` beside the Lightning type's schema, use `@widget/c/<widgetName>` for local widgets, and select direct or MCP `outputValues` mappings correctly. Widget references in `editor.json` or LWC channel folders are unsupported. Prefer documented beta components; Playground preview components need separate support verification.

Run `python3 scripts/validate.py <DX-project-or-source-directory>` on changed bundles. It checks local structure, documented component properties, binding names, and integration wiring; it does not compile Apex or prove runtime support. Run appropriate Salesforce validation and target-channel checks when authorized and available. Report local, deployment, and rendered-runtime results separately.

For beta changes or undocumented features, verify only the relevant official pages using provenance URLs. Preserve offline authoring for ordinary tasks. Handle [documentation inconsistencies](references/troubleshooting.md#documentation-inconsistencies) explicitly rather than guessing.
