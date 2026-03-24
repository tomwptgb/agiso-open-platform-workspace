#!/usr/bin/env python3
"""Resolve stable repository and knowledge-base paths for the Agiso skill."""

from __future__ import annotations

import os
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def knowledge_base_root() -> Path:
    override = os.environ.get("AGISO_KNOWLEDGE_BASE_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return repo_root() / "knowledge-base"


def docs_root() -> Path:
    return knowledge_base_root() / "docs"


def extracted_root() -> Path:
    return knowledge_base_root() / "extracted"


def raw_js_root() -> Path:
    return knowledge_base_root() / "raw_js"
