#!/usr/bin/env python3
"""Sync the workspace knowledge base into the installable skill bundle."""

from __future__ import annotations

import shutil
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def copy_tree(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)

    for child in target.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    for child in source.iterdir():
        destination = target / child.name
        if child.is_dir():
            shutil.copytree(child, destination)
        else:
            shutil.copy2(child, destination)


def main() -> int:
    source = repo_root() / "knowledge-base"
    target = skill_root() / "knowledge-base"

    if not source.exists():
        raise SystemExit(f"workspace knowledge base not found: {source}")

    copy_tree(source, target)
    print(f"synced {source} -> {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
