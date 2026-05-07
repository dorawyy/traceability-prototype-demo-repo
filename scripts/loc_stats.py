#!/usr/bin/env python3
"""
Count Kotlin files under frontend/ and TypeScript files under backend/,
plus lines of code (physical lines per file).
"""

from __future__ import annotations

import sys
from pathlib import Path

# Directory names to skip when walking source trees
SKIP_DIR_NAMES = {
    "node_modules",
    "dist",
    "build",
    ".git",
    ".gradle",
    ".idea",
    "__pycache__",
    ".cxx",
    "generated",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def iter_files(root: Path, suffix: str) -> list[Path]:
    if not root.is_dir():
        return []
    out: list[Path] = []
    for path in root.rglob(f"*{suffix}"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        out.append(path)
    return sorted(out)


def line_count(path: Path) -> int:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"warning: could not read {path}: {e}", file=sys.stderr)
        return 0
    if not text:
        return 0
    return text.count("\n") + (1 if not text.endswith("\n") else 0)


def main() -> None:
    root = repo_root()
    frontend = root / "frontend"
    backend = root / "backend"

    kotlin_files = iter_files(frontend, ".kt")
    ts_files = iter_files(backend, ".ts")

    kotlin_loc = sum(line_count(p) for p in kotlin_files)
    ts_loc = sum(line_count(p) for p in ts_files)

    print("LOC statistics (repository source)")
    print(f"  root: {root}")
    print()
    print(f"  frontend/ (Kotlin)")
    print(f"    files: {len(kotlin_files)}")
    print(f"    lines: {kotlin_loc}")
    print()
    print(f"  backend/ (TypeScript)")
    print(f"    files: {len(ts_files)}")
    print(f"    lines: {ts_loc}")
    print()
    print(f"  total .kt + .ts files: {len(kotlin_files) + len(ts_files)}")
    print(f"  total lines: {kotlin_loc + ts_loc}")


if __name__ == "__main__":
    main()
