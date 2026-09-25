#!/usr/bin/env python3
"""Structure validation for the Pi³XI Canonical Spec (standard library only)."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "README.md",
    "GOVERNANCE.md",
    "LICENSE",
    "principles/coordinate-invariant.md",
    "principles/observation-first.md",
    "principles/responsibility-boundaries.md",
    "invariants/phase1-invariants.md",
    "invariants/metric-definitions.md",
    "runtime/canonical-record.md",
    "runtime/intent-event-observe-meta.md",
    "runtime/observation-interface.md",
    "contracts/references.md",
    "releases/spec-v1.0.md",
    "tools/validate_spec.py",
    ".github/workflows/spec-check.yml",
]

README_HEADINGS = [
    "Core Principles",
    "Canonical Invariants",
    "Runtime Model",
    "Governance",
]

H1_DIRS = ["principles", "invariants", "runtime"]

H1_RE = re.compile(r"^# \S", re.MULTILINE)


def main() -> int:
    failures = 0

    def report(ok: bool, message: str) -> None:
        nonlocal failures
        print(f"{'PASS' if ok else 'FAIL'}: {message}")
        if not ok:
            failures += 1

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        exists = path.is_file()
        report(exists, f"file exists: {rel}")
        if exists:
            report(path.stat().st_size > 0 and path.read_text(encoding="utf-8").strip() != "",
                   f"file non-empty: {rel}")

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    for heading in README_HEADINGS:
        pattern = re.compile(r"^#{1,6}\s+" + re.escape(heading) + r"\s*$", re.MULTILINE)
        report(bool(pattern.search(text)), f"README heading: {heading}")

    for rel in REQUIRED_FILES:
        if rel.split("/")[0] in H1_DIRS and rel.endswith(".md"):
            path = ROOT / rel
            content = path.read_text(encoding="utf-8") if path.is_file() else ""
            report(bool(H1_RE.search(content)), f"level-1 heading: {rel}")

    print()
    if failures:
        print(f"RESULT: FAIL ({failures} check(s) failed)")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
