#!/usr/bin/env python3
"""Install this self-contained skill without overwriting an existing skill."""
import argparse
import os
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skills-dir", type=Path, default=Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "skills")
    args = parser.parse_args()
    folder = args.skills_dir.expanduser().resolve()
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / "sf-hxl"
    if dest.exists() or dest.is_symlink():
        parser.error("Skill already exists; review changes before replacing it: " + str(dest))
    staging = Path(tempfile.mkdtemp(prefix=".hxl-install-", dir=folder))
    try:
        copied = staging / "sf-hxl"
        copied.mkdir()
        for name in ("SKILL.md", "LICENSE", "agents", "assets", "references", "scripts"):
            source = ROOT / name
            if source.is_dir():
                shutil.copytree(source, copied / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            else:
                shutil.copy2(source, copied / name)
        copied.rename(dest)
    finally:
        shutil.rmtree(staging)
    print("Installed " + str(dest))

if __name__ == "__main__":
    main()
