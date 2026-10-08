# Org setup and metadata deployment

## HXL prerequisites

Use API 67.0 or newer in the project and manifest, and a target org that actually supports the beta. In Setup, search **Headless Experience Layer Settings**, review the beta terms, and enable HXL. Install Salesforce CLI, create/open a DX project, and authorize the actual target. A Dev Hub is necessary only when creating scratch orgs. Author bundles locally; Setup's Lightning Types page cannot author/modify widget-referencing types in this snapshot.

```bash
sf org login web --alias hxl-dev
sf org display --target-org hxl-dev
```

Use the user's target alias; do not silently switch project/global defaults. Inspect returned identity without recording access tokens. The installed CLI's `--help` is the source for current command flags.

## MCP OAuth and access

The hosted MCP setup uses an **External Client App (ECA)**, not a Connected App. It requires admin-equivalent rights to register. Scratch-org Setup cannot create the ECA directly: package an ECA from a Dev Hub and install it into the scratch org. Vibes as a hosted MCP client is documented as an exception that does not require an ECA; this does not remove the ECA requirement for other clients.

In **External Client App Manager**, create an ECA with OAuth enabled. Configure the actual client callback, including exact scheme/path. Claude's documented callback is `https://claude.ai/api/mcp/auth_callback`; copy ChatGPT's actual callback from its advanced settings. Other clients use their provider's callback. Add scopes `mcp_api` and `refresh_token`; issue JWT-based access tokens for named users. Capture the consumer key for client ID and securely configure a secret when required by that client. Do not put keys, secrets, or tokens in generated repositories or share links.

The HXL/setup overview mentions PKCE, while the detailed ECA page gives different checkbox instructions. Confirm current client and org requirements before changing security switches; do not silently weaken an existing app's settings. See [inconsistencies](troubleshooting.md#documentation-inconsistencies). Additional production controls in the ECA docs are optional design choices: secret requirement for web clients, preauthorized permission sets, suitable IP restrictions, refresh-token validity/rotation, and single logout. They are not prerequisites for drafting local widget source.

ECA availability can take up to 30 minutes. MCP servers are disabled by default; enable only the required servers in Setup **MCP Servers** under API Catalog. Activation can take up to two minutes. For custom HXL wiring, also activate the specific custom server after deploying its resources. Before OAuth, ensure the default browser session targets the ECA's intended org; the guide recommends signing out of other orgs to avoid tenant confusion. Do not sign the user out without scope to manage those sessions.

## Manifest and order

Deploy supporting Apex before dependent CLTs, and widgets before widget-referencing CLTs, or include the dependencies in one package. Metadata API resolves their order within a single package. MCP payload and wrapper CLTs may be deployed together; deploy the server resource wiring after its referenced type exists.

Example focused manifest:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
  <types>
    <members>accountSummary</members>
    <name>UiWidgetBundle</name>
  </types>
  <types>
    <members>accountSummaryResponse</members>
    <name>LightningTypeBundle</name>
  </types>
  <version>67.0</version>
</Package>
```

Add actual Apex class members if they need deployment. An MCP package includes both `<base>OutputValues` and `<base>Result` as LightningTypeBundle members. Never use a blanket wildcard to expand a narrow widget request without reason.

## CLI operations

From the DX project, validate a development draft without applying it:

```bash
sf project deploy start --manifest manifest/hxl-accountSummary.xml --target-org TARGET --dry-run
```

`project deploy validate` is also available for validation-only production workflows; inspect its current help and use the test level appropriate to the org/source. Apex changes require meaningful tests under Salesforce deployment rules. A local JSON/XML check does not fulfill Apex testing.

Within authorized deployment scope:

```bash
sf project deploy start --manifest manifest/hxl-accountSummary.xml --target-org TARGET
sf project deploy report --job-id JOB_ID --target-org TARGET
sf project retrieve start --metadata UiWidgetBundle:accountSummary --target-org TARGET
sf project retrieve start --metadata LightningTypeBundle:accountSummaryResponse --target-org TARGET
```

Inspect final status and failures; a queued deployment is not completion. Retrieval can change local source, so preserve unrelated edits first. MCP server operations use `McpServerDefinition:<serverApiName>` and the source directory `mcpServerDefinitions`. The CLT core guide says LightningTypeBundle supports managed packaging from API 66.0; HXL UiWidgetBundle still requires 67.0+. The hosted MCP custom-server guide says ISV managed packages cannot currently directly include server configurations. Do not infer packaging support for every metadata dependency.

Deleting widget metadata requires a destructiveChanges deployment. Include only specifically requested members and verify remaining renderers/server resources; ordinary source authoring does not imply deletion.

After deployment, complete [Agentforce output selection](agentforce.md#configure-output-rendering) or [MCP tool resources and OAuth](mcp.md), then verify the actual rendered target.

Sources: [prerequisites](https://developer.salesforce.com/docs/platform/hxl/guide/prerequisites.html), [rich UI](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-rich-ui.html), [core CLTs](https://developer.salesforce.com/docs/platform/lightning-types/guide/lightning-types-core.html), [project commands](https://developer.salesforce.com/docs/platform/salesforce-cli-reference/guide/cli_reference_project.html), [ECA](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/create-external-client-app.html), [org login](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/log-into-org.html), [activation](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/activate-mcp-servers.html), [custom servers](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/custom-servers.html).
