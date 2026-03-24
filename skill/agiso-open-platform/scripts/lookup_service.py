#!/usr/bin/env python3
"""Lookup Agiso services by keyword and print recommended docs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from data_paths import docs_root, extracted_root


EXTRACTED = extracted_root()
DOCS = docs_root()


def load_json(path: Path):
    return json.loads(path.read_text())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Service, marketplace, or workflow keyword")
    args = parser.parse_args()

    query = args.query.lower()
    crawl = load_json(EXTRACTED / "crawl_summary.json")
    route_map = load_json(EXTRACTED / "route_map.json")

    rows = []
    for service in crawl["services"]:
        desc = crawl["service_descriptions"].get(service, "")
        routes = route_map["services"].get(service, [])
        haystack = " ".join(
            [service, desc]
            + [route["path"] for route in routes]
            + [route["title"] for route in routes]
        ).lower()
        score = 0
        if query in service.lower():
            score += 4
        if query in desc.lower():
            score += 3
        if query in haystack:
            score += 1
        if score:
            docs = sorted(p.name for p in (DOCS / service).glob("*.md")) if (DOCS / service).exists() else []
            rows.append(
                {
                    "service": service,
                    "description": desc,
                    "score": score,
                    "docs": docs,
                    "routes": routes[:8],
                }
            )

    rows.sort(key=lambda item: (-item["score"], item["service"]))
    print(json.dumps(rows, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
