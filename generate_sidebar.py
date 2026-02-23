#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ORDER_FILE = DOCS / "sidebar_order.yml"
SUMMARY_FILE = DOCS / "SUMMARY.md"
MKDOCS_FILE = ROOT / "mkdocs.yml"

order = []
for line in ORDER_FILE.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line.startswith("- "):
        order.append(line[2:].strip())


def title_from_file(md_name: str) -> str:
    text = (DOCS / md_name).read_text(encoding="utf-8")
    for ln in text.splitlines():
        if ln.startswith("# "):
            return ln[2:].strip()
    return md_name.replace(".md", "")

items = [(title_from_file(f), f) for f in order]

summary_lines = ["# Summary", ""]
for title, f in items:
    summary_lines.append(f"- [{title}](./{f})")
SUMMARY_FILE.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

mkdocs_lines = [
    "site_name: Frappe Framework - Zero to Hero",
    "theme:",
    "  name: material",
    "docs_dir: docs",
    "nav:",
]
for title, f in items:
    mkdocs_lines.append(f"  - '{title}': '{f}'")
MKDOCS_FILE.write_text("\n".join(mkdocs_lines) + "\n", encoding="utf-8")

print("Generated:")
print(f"- {SUMMARY_FILE.relative_to(ROOT)}")
print(f"- {MKDOCS_FILE.relative_to(ROOT)}")
