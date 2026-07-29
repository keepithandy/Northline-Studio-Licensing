#!/usr/bin/env python3
"""Check local Markdown links without rewriting policy documents."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PREFIXES = ("http://", "https://", "mailto:", "#")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", 1)[0].strip()
    if not target or target.startswith(EXCLUDED_PREFIXES):
        return None
    target = unquote(target).split(" ", 1)[0]
    return (source.parent / target).resolve()


def main() -> int:
    failures: list[str] = []
    for source in sorted(ROOT.rglob("*.md")):
        if ".git" in source.parts:
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK_RE.finditer(line):
                target = local_target(source, match.group(1))
                if target is not None and not target.exists():
                    failures.append(
                        f"{source.relative_to(ROOT)}:{line_number}: missing local target {match.group(1)!r}"
                    )
    if failures:
        print("Local Markdown link check failed:")
        print("\n".join(failures))
        return 1
    print("Local Markdown links passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
