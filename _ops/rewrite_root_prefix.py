#!/usr/bin/env python3
"""Rewrite /wensite-previews/ absolute paths to / for custom-domain root serve."""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules", "_ops", "scrapes", "reference", "screenshots", "assets"}
EXTS = {".html", ".js", ".css", ".json", ".md"}
OLD = "/wensite-previews/"
NEW = "/"

def main() -> None:
    n_files = n_hits = 0
    for p in ROOT.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in EXTS:
            continue
        if any(part in SKIP for part in p.parts):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        if OLD not in text:
            continue
        count = text.count(OLD)
        p.write_text(text.replace(OLD, NEW), encoding="utf-8")
        n_files += 1
        n_hits += count
        print(f"{count:4d}  {p.relative_to(ROOT)}")
    print(f"done: {n_hits} replacements in {n_files} files")

if __name__ == "__main__":
    main()
