#!/usr/bin/env python3
"""Search Agiso extracted indexes and markdown docs for endpoints, topics, and keywords."""

from __future__ import annotations

import argparse
import json

from data_paths import docs_root, extracted_root, knowledge_base_root
EXTRACTED = extracted_root()
DOCS = docs_root()
KNOWLEDGE_BASE = knowledge_base_root()


def search_api_index(query: str):
    data = json.loads((EXTRACTED / "api_docs_index.json").read_text())
    results = []
    for item in data:
        haystack = " ".join(str(item.get(k, "")) for k in ("title", "url", "method", "type", "file")).lower()
        if query in haystack:
            results.append(item)
    return results


def search_markdown(query: str):
    results = []
    for path in DOCS.rglob("*.md"):
        text = path.read_text(errors="replace")
        lower = text.lower()
        if query not in lower:
            continue
        index = lower.index(query)
        start = max(0, index - 120)
        end = min(len(text), index + 220)
        snippet = text[start:end].replace("\n", " ")
        results.append({"file": str(path.relative_to(KNOWLEDGE_BASE)), "snippet": snippet})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Keyword, endpoint fragment, or topic")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    query = args.query.lower()
    output = {
        "api_index": search_api_index(query)[: args.limit],
        "markdown": search_markdown(query)[: args.limit],
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
