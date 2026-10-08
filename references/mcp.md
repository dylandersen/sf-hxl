# HXL through hosted MCP

Contents: supported surfaces; result contracts; Apex tools; resource wiring; clients; runtime checks. Read [org/deployment](org-deployment.md) for OAuth and activation.

## Surface and backing action

The HXL beta names ChatGPT, Claude, and Slackbot, using MCP Apps-compatible rendering. HXL does not currently render through Slackbot Block Kit. Client MCP Apps support is a prerequisite, not a promise that every MCP client renders UI.

The two-type pattern below applies to invocable actions exposed as custom hosted MCP tools, primarily Apex. It is not a universal envelope for every unrelated MCP result. Reuse an appropriate existing custom server; HXL does not require a separate Node proxy or a handcrafted HTML MCP app.

## Two Lightning type roles

Wrapper and payload are roles of object-based CLTs, not separate Salesforce categories:

```text
lightningTypes/accountSummaryOutputValues/schema.json
lightningTypes/accountSummaryResult/schema.json
lightningTypes/accountSummaryResult/renderer.json
```

Both schemas use `type: object`, `lightning:type: lightning__objectType`, `lightning:tags: ["mcp"]`, and `unevaluatedProperties: false`.

Payload:

```json
{
  "title": "Account summary output variables",
  "type": "object",
  "lightning:type": "lightning__objectType",
  "lightning:tags": ["mcp"],
  "unevaluatedProperties": false,
  "properties": {
    "summary": {"title": "Summary", "lightning:type": "@apexClassType/c__AccountSummaryResponse"}
  }
}
```

Result wrapper:

```json
{
  "title": "Account summary tool result",
  "type": "object",
  "lightning:type": "lightning__objectType",
  "lightning:tags": ["mcp"],
  "unevaluatedProperties": false,
  "properties": {
    "actionName": {"title": "Action", "lightning:type": "lightning__textType"},
    "isSuccess": {"title": "Success", "lightning:type": "lightning__booleanType"},
    "outputValues": {"title": "Output", "lightning:type": "c__accountSummaryOutputValues"}
  }
}
```

Only the wrapper gets a renderer. Its `renderer.componentOverrides.$` uses `@widget/c/accountSummary`, mapping `name` to `{!$attrs.outputValues.summary.name}`. Replace `summary` with the action's actual output variable. The widget contract remains flat. A CLT cannot reference itself: `outputValues` references the separate payload CLT.

## Invocable action

Use a `global` Apex class and a `global` method annotated `@InvocableMethod`; method input/output fields define the tool contract. The tool runs as the authenticated user; maintain sharing, CRUD/FLS checks, governor-limit safety, and existing business rules. Ensure actual `outputValues` matches the payload schema. Refresh tool configuration after input/output changes. Deploy the action before adding it as a tool.

Flows are another hosted MCP backing type, but the HXL worked integration is invocable/Apex. Verify actual envelope and rendering support before adapting other backing types. The scaffold does not generate or compile the business action.

## Configure server resources

In Setup **MCP Servers** under **API Catalog**, create/open the custom server. Use **Add Server Assets → Add Tools → Apex actions**, choose the invocable method, and save. Note the server URL. Setup does not currently expose HXL resource wiring; retrieve the server definition:

```bash
sf project retrieve start --metadata McpServerDefinition:accountSummaryServer --target-org TARGET
```

Edit `mcpServerDefinitions/accountSummaryServer.mcpServerDefinition-meta.xml`, preserving the retrieved tool identity and other fields. Add a resource alongside `tools`:

```xml
<resources>
  <resourceName>accountSummaryUi</resourceName>
  <resourceUri>ui://widget/lightningType/c__accountSummaryResult</resourceUri>
  <resourceTitle>Account Summary</resourceTitle>
  <description>Account details for this tool</description>
</resources>
```

Add `<uiResource>accountSummaryUi</uiResource>` inside the matching `tools` entry. It must exactly match `resourceName`. The URI references the wrapper CLT, not the payload or widget. Deploy the definition and activate the server in Setup. This fragment is not a complete server metadata document.

Production/developer custom URLs use `https://api.salesforce.com/platform/mcp/v1/custom/<serverName>`; sandbox/scratch inserts `sandbox/` before `custom/`. Prefer Setup's actual URL.

## Connect and verify clients

Claude: create a custom connector, give the server URL, choose your own OAuth client, and enter the ECA consumer key as client ID. The Salesforce snapshot permits a blank secret unless the authorization server requires one.

ChatGPT: the Salesforce snapshot describes **Settings → Apps → Create App**, user-defined OAuth registration, callback copied from advanced settings, ECA client ID and secret, and OIDC disabled. Salesforce says a secret is required even when the client labels it optional. Verify current official client instructions when actually configuring the live connection; these labels/settings can change.

Slackbot: configure **Manual OAuth**, the custom server URL, and the ECA consumer key as client ID. Use MCP Apps rendering; Block Kit is unsupported for HXL in this snapshot.

Authenticate into the correct org, invoke the specific tool, inspect its result envelope, and check displayed values/actions. Client caches can delay widget refresh. MCPJam, Postman, or MCP Inspector can isolate server failures; those tools alone do not prove native rendering in the final client.

Sources: [MCP workflow](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-channels.html), [Apex](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-apex.html), [server](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-server.html), [org access](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-setup-org.html), [clients](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-mcp-setup-client.html), [mapping](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-widget-example-mapping-mcp.html), [hosted Apex tools](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/invocable-actions.html), [Claude](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/claude.html), [ChatGPT](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/chatgpt.html).
