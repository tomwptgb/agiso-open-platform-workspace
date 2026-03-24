#!/usr/bin/env python3
"""Resolve stable bundled and workspace knowledge-base paths for the Agiso skill."""

from __future__ import annotations

import os
from pathlib import Path


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def knowledge_base_root() -> Path:
    override = os.environ.get("AGISO_KNOWLEDGE_BASE_ROOT")
    if override:
        return Path(override).expanduser().resolve()

    bundled = skill_root() / "knowledge-base"
    if bundled.exists():
        return bundled

    return repo_root() / "knowledge-base"


def docs_root() -> Path:
    return knowledge_base_root() / "docs"


def extracted_root() -> Path:
    return knowledge_base_root() / "extracted"


def raw_js_root() -> Path:
    return knowledge_base_root() / "raw_js"
