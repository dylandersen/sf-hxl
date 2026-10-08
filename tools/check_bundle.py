#!/usr/bin/env python3
"""Check offline documentation routes, coverage records, and serialized resources."""
import json
import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/salesforce-hxl"

def slug(text):
    text = re.sub(r"[`*_]", "", text).lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return re.sub(r"\s", "-", text)

def main():
    errors = []
    count = 0
    for file in SKILL.rglob("*.md"):
        source = file.read_text()
        # Fenced examples contain code, not navigation links.
        prose = re.sub(r"```.*?```", "", source, flags=re.S)
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
            if target.startswith(("https://", "http://", "mailto:")):
                continue
            path, _, anchor = target.partition("#")
            dest = (file.parent / unquote(path)).resolve() if path else file
            count += 1
            if not dest.is_relative_to(SKILL) or not dest.is_file():
                errors.append(f"{file.relative_to(ROOT)}: missing/escaping local link {target}")
            elif anchor:
                headings = {slug(line.lstrip("# ")) for line in dest.read_text().splitlines() if line.startswith("#")}
                if anchor not in headings:
                    errors.append(f"{file.relative_to(ROOT)}: missing anchor {target}")
    for file in SKILL.rglob("*.json"):
        try:
            json.loads(file.read_text())
        except ValueError as exc:
            errors.append(f"Invalid JSON {file}: {exc}")
    manifest = json.loads((SKILL / "references/provenance.json").read_text())
    expected = {"hxl-guide": 21, "hxl-reference": 25, "platform-dependency": 23, "navigation": 2}
    if manifest["coverage"] != expected:
        errors.append("Unexpected coverage totals")
    urls = set()
    for entry in manifest["sources"]:
        if entry["url"] in urls:
            errors.append("Duplicate source URL: " + entry["url"])
        urls.add(entry["url"])
        target = SKILL / entry["local_reference"].split("#")[0]
        if not target.is_file():
            errors.append("Source has no offline route: " + entry["url"])
        if not re.fullmatch(r"[a-f0-9]{64}", entry["raw_html_sha256"]):
            errors.append("Invalid source hash: " + entry["url"])
    catalog = json.loads((SKILL / "references/component-contracts.json").read_text())
    if len(catalog) != 22:
        errors.append("Expected all 22 platform beta components")
    for definition in catalog:
        if not (SKILL / "references/components" / (definition.split("/")[-1] + ".md")).is_file():
            errors.append("Missing component guide: " + definition)
    for item in errors:
        print("ERROR:", item)
    print(f"Checked {count} local links, {len(urls)} source routes, and {len(catalog)} component contracts")
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
