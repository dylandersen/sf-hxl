# HXL review rubric

Use this when reviewing a widget, integration, or PR, or when the user asks for a scored assessment. The rubric organizes evidence; it does not turn ordinary authoring into a mandatory certification workflow. Total: **100 points across six categories**.

## Scoring with honest evidence

Score only the requested scope. Mark unrelated items N/A and normalize earned points over applicable points. Record unverified applicable items separately; award verified points only, and report evidence coverage alongside the score. For example, a source-only draft can earn strong source quality without claiming deployed/runtime points. A 90-point source review is not proof of native rendering or permission to deploy.

| Score | Interpretation within the assessed scope |
| --- | --- |
| 90–100 | Strong implementation; resolve any unverified integration evidence before release |
| 75–89 | Useful draft; address specific weaknesses |
| 60–74 | Focused revision needed |
| Below 60 | Major contract or integration gaps |

## Bundle correctness — 20 points

| Evidence | Points |
| --- | --- |
| Correct package path, API name, matching JSON/XML filenames | 4 |
| lightning__agentforceWidget composition and tile/widget root | 5 |
| UiWidgetBundle XML namespace and widgetType JSON | 4 |
| Dynamic widget schema under properties.attributes.properties | 5 |
| Effective API version 67.0+ in project/manifest | 2 |

## Data contracts and mapping — 25 points

| Evidence | Points |
| --- | --- |
| UI inputs preserve the actual typed output and requested fields | 5 |
| Root renderer points to the right widget with matching mapping keys | 5 |
| Direct Agentforce mapping OR MCP wrapper/payload structure matches the chosen channel | 8 |
| Formula, conditional, and iteration scopes/types work for real input cases | 5 |
| Namespace references and supporting class/type dependencies are correct | 2 |

For MCP, the eight-point item includes separate object CLTs, mcp tags, unevaluatedProperties false, correct outputValues reference, and renderer on the wrapper. For Agentforce it includes the projected Apex type and direct output mapping. Do not award both routes when only one is requested.

## Surface and accessibility — 15 points

| Evidence | Points |
| --- | --- |
| Components and attributes are documented or explicitly verified for the target surface | 5 |
| Semantic layout, appropriate content density, empty/long-value behavior | 4 |
| Image/icon alternatives, table captions, and loading labels as applicable | 4 |
| Known channel differences are handled without false parity claims | 2 |

## Interactions — 10 points

| Evidence | Points |
| --- | --- |
| Correct event-to-action-array shape and typed action payloads | 4 |
| Follow-up message identifies its intended record/task or navigation uses the intended URL | 3 |
| Requested interaction routes to the correct host/agent capability | 3 |

Mark this category N/A if the requested widget has no interaction. Buttons do not establish availability of backing business actions by themselves.

## Org and channel wiring — 15 points

| Evidence | Points |
| --- | --- |
| Required HXL availability and org feature state verified | 3 |
| Agentforce output selection/subagent wiring OR MCP resource/tool/activation wiring verified | 6 |
| User access, relevant OAuth, and public-image Trusted URL/CSP behavior verified | 4 |
| Dependency-complete deployment manifest/order | 2 |

Source-only tasks can assess the planned manifest and required wiring, but live org evidence remains unverified. Do not require unrelated OAuth setup for a local static widget or native Agentforce-only work.

## Validation and delivery — 15 points

| Evidence | Points |
| --- | --- |
| Local contract checks pass with meaningful warnings addressed or disclosed | 4 |
| Salesforce validates the actual metadata/Apex with appropriate tests when in scope | 4 |
| Actual target renders matching data and requested actions | 5 |
| Changed paths, remaining steps, and untested stages are clearly reported | 2 |

## Report template

```text
Assessed scope: source / Agentforce / MCP clients / requested surfaces
Bundle correctness        __ / applicable __
Data contracts & mapping  __ / applicable __
Surface & accessibility   __ / applicable __
Interactions              __ / applicable __
Org & channel wiring      __ / applicable __
Validation & delivery     __ / applicable __
Verified score: earned / applicable × 100
Evidence coverage: verified / applicable points
Unverified items: ...
Concrete fixes: ...
```

Regardless of score, unresolved failures in the requested contract remain failures: an incorrect root, missing dynamic input contract, invalid output mapping, missing tool resource, or inaccessible required data cannot be described as a working integration. Use [troubleshooting](troubleshooting.md) to resolve demonstrated issues and [sources](sources.md) for beta contract changes.
