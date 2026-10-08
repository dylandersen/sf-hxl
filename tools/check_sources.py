#!/usr/bin/env python3
"""Report official source changes without rewriting the curated offline references."""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contains", default="", help="Check only URLs containing this text")
    args = parser.parse_args()
    provenance = json.loads((ROOT / "skills/salesforce-hxl/references/provenance.json").read_text())
    records = [r for r in provenance["sources"] if args.contains in r["url"]]
    if not records:
        parser.error("No matching source URLs")
    def check(entry):
        try:
            request = urllib.request.Request(entry["url"], headers={"User-Agent": "HXL-skill-source-check/1.0"})
            with urllib.request.urlopen(request, timeout=30) as response:
                content = response.read()
            state = "unchanged" if hashlib.sha256(content).hexdigest() == entry["raw_html_sha256"] else "changed"
            return {"state": state, "url": entry["url"], "review_reference": entry["local_reference"]}
        except Exception as exc:
            return {"state": "unavailable", "url": entry["url"], "error": str(exc)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        reports = list(pool.map(check, records))
    print(json.dumps(reports, indent=2))
    print("HTML hash changes can include navigation/build changes; inspect affected content before editing facts.")
    raise SystemExit(1 if any(r["state"] != "unchanged" for r in reports) else 0)

if __name__ == "__main__":
    main()
