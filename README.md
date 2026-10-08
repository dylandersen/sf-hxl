# Salesforce Headless Experience Layer skill

`$salesforce-hxl` helps create HXL widgets and connect them to Agentforce action output or Salesforce hosted MCP tools. The source is [skills/salesforce-hxl/SKILL.md](skills/salesforce-hxl/SKILL.md).

The entrypoint is 432 words; larger material is loaded selectively from local references. Coverage includes every published HXL guide/reference navigation topic: 21 guide pages, 25 reference pages, 22 beta components, 19 HXL Lightning types, and 23 supporting platform pages. The 2026-10-08 beta snapshot requires API 67.0+. References distill implementation facts and workflows with original examples; the skill does not require network access, the source checkout, or SSO for authoring.

Install with Python 3.10 or later:

```bash
python3 tools/install_skill.py
```

This creates `~/.codex/skills/salesforce-hxl` (or `$CODEX_HOME/skills/salesforce-hxl`) and refuses to overwrite an existing installation. Open a new Codex chat if the installed skill is not yet discovered.

Example invocation:

> Use $salesforce-hxl to create an account-summary widget for Agentforce, with typed revenue and a follow-up button, using the structured output in my DX project.

The skill's scaffold supports static, Agentforce, and MCP modes without Salesforce access. Its local checker validates source contracts and integration wiring. Apex implementation, Salesforce deployment validation, org configuration, OAuth, and native client rendering remain separate stages.

Repository checks:

```bash
python3 tools/check_bundle.py
python3 -m unittest discover -s tests -v
```

[Sources and coverage](skills/salesforce-hxl/references/sources.md) link every captured topic to an offline reference. [Provenance](skills/salesforce-hxl/references/provenance.json) stores URLs and source hashes. Check freshness selectively with `python3 tools/check_sources.py --contains hxl-widget-schema`; without the filter it checks all sources. HTML changes are review prompts, not automatic prose/schema updates.

Documentation scope is the entire HXL platform guide/reference tree and its needed implementation dependencies, not every Salesforce product manual. External Playground tutorials, Help/release-note pages, screenshots, and sample archives are not mirrored. Documented beta contradictions and surface limitations are preserved locally. Live org/client testing was not part of creating this repository.
