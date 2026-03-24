# agiso-open-platform-workspace

`agiso-open-platform-workspace` is a single repository with two explicit boundaries.

## knowledge-base

`knowledge-base/` is the source-of-evidence layer. It stores raw frontend assets, extracted indexes, generated markdown docs, and the extraction pipeline.

- inputs: `raw_js/`
- generated knowledge: `docs/`, `extracted/`
- producer: `extract_docs.py`

## skill

`skill/agiso-open-platform/` is the Codex-facing consumption layer inside this workspace repository. The repository name is `agiso-open-platform-workspace`; the skill name remains `agiso-open-platform`. It does not own the Agiso facts. It owns task framing, references, and small scripts that read from `knowledge-base/`.

## Decision Rule

Keep this as one repository while changes regularly cross the producer-consumer boundary.
Only split into two repositories after the knowledge-base has a stable published contract and the skill can consume versioned snapshots without coordinated commits.

## Path Contract

Skill scripts resolve the knowledge base from one of these sources:

1. `AGISO_KNOWLEDGE_BASE_ROOT`
2. `<repo>/knowledge-base`

That replaces the previous implicit relative-path coupling.
