# sf-hxl

🧩 **Salesforce Headless Experience Layer skill** — by Dylan Andersen · **v1.0**

An agent skill that teaches your AI coding agent to build, connect, and deploy **HXL widgets on the Salesforce Agentforce 360 Platform** (`UiWidgetBundle`) — JSON composition, typed data bindings, formulas, interactive actions, Agentforce output rendering, and hosted MCP integration for ChatGPT, Claude, and Slackbot — plus a 100-point rubric for reviewing its output.

> Format and skill conventions inspired by [sf-multiframework](https://github.com/dylandersen/sf-multiframework). Built from official [Salesforce documentation](references/sources.md): every HXL guide and reference topic, plus the Lightning Types and hosted MCP contracts needed to wire the experience. Documentation is distilled into local references, so authoring works without browsing the source site. Works with coding agents and IDEs that support agent skills.

## Install

```bash
npx skills add dylandersen/sf-hxl --global
```

For a direct Codex installation from a local checkout:

```bash
python3 tools/install_skill.py
```

The Python installer targets `$CODEX_HOME/skills/sf-hxl` or `~/.codex/skills/sf-hxl` and preserves existing installations. Open a new chat if your agent has not discovered the newly installed skill.

## When to use it

Your agent should reach for this skill whenever you ask it to scaffold, build, review, connect, or deploy a Salesforce HXL / `UiWidgetBundle` experience — for example “build an HXL account-summary card,” “render this Agentforce action as a widget,” or “connect my Apex invocable tool to a widget in Claude.”

Invoke it directly in Codex with `$sf-hxl`. Use [sf-multiframework](https://github.com/dylandersen/sf-multiframework) for React apps deployed as `UIBundle`; HXL widgets are a separate declarative metadata model.

## What's inside

- **[SKILL.md](SKILL.md)** — the core authoring rules, workflow routing, and integration boundaries.
- **[references/](references/)** — deep dives: composition, formulas, conditions and repetition, all 22 documented beta components, 19 HXL Lightning types, Agentforce, MCP resources/OAuth, deployment, Playground/Vibes, troubleshooting, and a [100-point review rubric](references/scoring-rubric.md).
- **[assets/](assets/)** — a typed account-summary specification to adapt into generated widgets.
- **[scripts/](scripts/)** — offline scaffolding for static, Agentforce, and MCP modes, plus source-contract validation.
- **[tools/](tools/)** and **[tests/](tests/)** — installation, documentation/link checks, source-freshness checks, and regression tests for the helpers.

## Compatibility

Targets Salesforce **HXL Beta**, API **v67.0+**, using a Salesforce DX project and an org with **Headless Experience Layer** enabled. The official snapshot covers Agentforce Employee agents in Lightning Experience and MCP Apps-compatible experiences in ChatGPT, Claude, and Slackbot. HXL does not currently render through Slackbot Block Kit.

Documentation snapshot: **October 8, 2026** — **21 guide pages + 25 reference pages + 23 supporting platform pages**. The complete HXL platform navigation is covered; external Playground tutorials, Help/release-note pages, and the rest of unrelated Salesforce manuals are not mirrored. See [sources and coverage](references/sources.md).

Python **3.10+** runs the bundled helpers without third-party packages. Salesforce CLI and an authorized target org are needed for deployment. Local checks do not compile Apex or verify live native rendering.

## What's New in v1.0

- **Complete HXL reference coverage**: all published guide/reference navigation topics distilled into selectively loaded local files, with source URLs and hashes.
- **Correct channel wiring**: direct Agentforce output mappings and separate MCP result-wrapper/payload CLTs, with a renderer at the type root.
- **Offline scaffolding**: generate widget composition, schema, metadata XML, optional CLTs, and a focused deployment manifest without contacting Salesforce.
- **Useful validation**: catch undeclared bindings, scope errors, malformed actions, incorrect MCP mappings, and mismatched server resources.
- **Surface-specific guidance**: preserve Agentforce table limitations, image/CSP requirements, and documented beta inconsistencies.
- **Evidence-based review**: a 100-point HXL rubric that separates source quality from deployment and runtime evidence.

## Cross-Skill Workflow

```text
Apex / structured actions       ─┐
Agentforce / hosted MCP tools   ─┤→  sf-hxl  →  metadata deployment
Permissions / OAuth setup      ─┘              + target-channel verification
```

Companion skills are optional. `sf-hxl` owns the widget composition, UI contract, renderer mapping, and HXL integration checks; the backing business action, agent reasoning, and org access remain their own implementation tasks. See [integration boundaries](references/companion-workflows.md) and [CREDITS.md](CREDITS.md).

## Validation

```bash
python3 tools/check_bundle.py
python3 -m unittest discover -s tests -v
```

The helpers passed **21 regression tests** and an independent offline case-widget generation check. **195 local documentation links** and **71 source routes** pass the repository checks. No live Salesforce deployment or client-rendering test is claimed.

Check a source for drift with `python3 tools/check_sources.py --contains hxl-widget-schema`. Source HTML changes prompt a content review; they do not automatically rewrite the curated references.

## License

MIT — see [LICENSE](LICENSE). Salesforce documentation remains attributed to Salesforce; this repository supplies distilled guidance, original examples, and helper code.
