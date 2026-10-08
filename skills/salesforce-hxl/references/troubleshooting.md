# Validation and troubleshooting

## Local validation

Run `python3 scripts/validate.py <project-or-source-dir>`. It checks the widget wrapper, required files, XML metadata, documented attributes/required inputs, bindings, scoped repetition, root widget renderers, local mapping targets, MCP wrapper/payload structure, and matching server resource names/URIs. The checker scans relevant HXL bundles only; it does not reject unrelated LWC renderer files merely for having a different format. It reports external dependencies it cannot inspect.

Local success is not Apex compilation, Salesforce schema validation, OAuth proof, or native rendering. Validate those stages when requested and available. Test empty/null data, long values, repeated items, typed table formatting, meaningful alt text, button payloads, and requested surfaces.

## Diagnose by layer

| Symptom | Inspect |
| --- | --- |
| UiWidgetBundle rejected | API 67.0+, beta enabled, exact filenames, `widgetType: JSON`, namespace |
| Widget absent | Root `tile/widget`, supported beta component, CLT reference, deployment dependencies |
| Dynamic fields empty | Widget `properties.attributes.properties`, token spelling, actual action output, renderer mapping |
| Conditional node absent | Boolean result, missing/null input, correct loop scope |
| Repeated values wrong | Collection type/data, `$` item/index variables, distinct nested scopes |
| Agentforce displays default output | Show in conversation, chosen CLT, reload, action/subagent availability, structured type |
| Agentforce table interactions absent | Sort/filter need imperative handlers; pagination requires data slicing |
| MCP returns text without UI | MCP Apps support, activated custom server, tool uiResource/resourceName match, wrapper CLT URI |
| MCP fields empty | Two object CLTs, tags/unevaluatedProperties, actual output variable beneath outputValues, wrapper renderer |
| Image absent | Public URL, Trusted URL/CSP, supported raster MIME, valid data payload/signature/size |
| Server unavailable | Correct production versus sandbox URL, activation delay, org API eligibility |
| OAuth fails | ECA rather than Connected App, exact redirect, scopes/JWT/client configuration, correct org browser session |
| Tool executes but errors | User permissions, feature activation, accessible records, parameter/output contract |
| Updated widget still stale | Client caching; retry fresh render and inspect returned tool/resource version |

Use a known standard server only when appropriate to isolate server versus auth problems; do not enable unrelated broad servers merely to troubleshoot. Compare a diagnostic client with the requested final surface. ECA registration may take 30 minutes and server activation two minutes, but elapsed time alone is not success.

## Surface differences

Read only relevant component files. Agentforce limitations are recorded for avatar, badge, code, link, progress, spinner, and table. The source pages list no known Slackbot/ChatGPT limitations for the documented components; this is a snapshot claim, not proof that every client version behaves identically. Claude is listed as supported overall, but the individual limitation sections do not separately document it. Mark untested channels honestly.

## Documentation inconsistencies

- Some composition prose mentions `tile/card` or `title/image`; the beta component catalog specifies `tile/container` and `tile/image`. Use the catalog's exact identifiers. The required root `tile/widget` is documented separately.
- The component landing page mentions `tile/listitem`; the dedicated API page and examples use case-sensitive `tile/listItem`.
- Column align/gap, row gap, and progress size are marked required in property tables, while examples omit them and rely on defaults. New output explicitly supplies them; the checker treats omissions as warnings to avoid claiming Salesforce rejects its own examples.
- Button's property table types `actions` as text, but action examples/type contracts use an event-to-array object. Use the documented object form.
- Avatar's property prose mentions SVG, but image's explicit supported MIME restrictions exclude vector/active content and avatar's usage inherits those restrictions. Use PNG/JPEG/GIF/WebP for portable output.
- HXL hotel samples reference an inner Apex class, while the dedicated Apex CLT guide requires top-level global classes with projection annotations. Prefer top-level types for new code; do not claim every existing inner-class sample fails without actual org evidence.
- HXL/org setup summaries recommend PKCE, while the detailed ECA instructions describe other checkbox settings. Verify current client-specific requirements before making live security changes.
- The base Lightning reference lists scalar/object contracts but not the full `lightning__listType` schema used in component tables. Preserve collection data and known property shapes without inventing undocumented schema keywords.

These discrepancies were observed in the 2026-10-08 snapshot. Relevant URLs are in [sources](sources.md); verify the affected contract for newer beta releases. The release-notes page delegates updates to Salesforce's Headless 360 release notes rather than embedding change entries.

Sources: [HXL release notes](https://developer.salesforce.com/docs/platform/hxl/guide/hxl-release-notes.html), [connection failures](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/connection-issues.html), [authentication](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/authentication-issues.html), [execution](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/execution-issues.html), [client testing](https://developer.salesforce.com/docs/platform/hosted-mcp-servers/guide/test-connection.html).
