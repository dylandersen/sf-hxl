# Integration boundaries and companion workflows

`sf-hxl` owns UiWidgetBundle authoring, the UI input contract, HXL renderer mapping, and HXL-specific integration checks. It can work from local data shapes without any other installed skill.

| Requested work | HXL responsibility | Optional companion capability |
| --- | --- | --- |
| New business action | Match its structured output to UI inputs | Apex/Flow authoring and business-rule tests |
| Native Agentforce experience | CLT projection, renderer, action Output Rendering | Agent/subagent setup, reasoning, and action tests |
| External MCP experience | Wrapper/payload types and resource URI/tool association | Hosted MCP administration and client OAuth setup |
| Data access | Preserve output types and identify required access | Schema discovery, SOQL, sharing, CRUD/FLS, permission sets |
| Deployment | HXL metadata names, focused manifest, dependency order | General Salesforce metadata deployment and test tooling |
| React application | An HXL widget is not a React application bundle | [sf-multiframework](https://github.com/dylandersen/sf-multiframework) |

Resolve the available companion by its actual installed name; Salesforce Skills Library names vary across releases. Examples in some environments include platform-apex-generate, agentforce-generate, platform-permission-set-generate, platform-metadata-deploy, platform-lightning-type-widget-coordinate, and platform-mcp-tool-widget-coordinate. Do not make those names hard dependencies or assume the skill implies extra org mutations.

Read a companion only when its workflow is part of the user's task. Preserve an existing action/provider rather than replacing it to fit the account-summary example. Do not infer mobile/Enhanced Chat HXL support from general LWC/CLT capabilities. The authoring, Agentforce, MCP, and deployment references provide the manual path when companion tooling is unavailable.
