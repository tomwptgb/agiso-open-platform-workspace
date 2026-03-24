# agiso-open-platform-workspace

[English](./README.md) | [简体中文](./README.zh-CN.md)

Open-source workspace for an Agiso Open Platform integration skill and its local evidence base.

Installation guides:

- [Install in AI clients](./INSTALL_SKILLS.md)
- [安装到 AI 客户端](./INSTALL_SKILLS.zh-CN.md)

This repository is organized around two boundaries:

- `knowledge-base/`: extracted source material, derived indexes, and the pipeline used to regenerate them
- `skill/agiso-open-platform/`: the Codex-facing skill, references, and helper scripts that consume the local knowledge base

## What This Repository Is For

Use this repository when you need a local, inspectable workspace for:

- exploring Agiso Open Platform service coverage
- reading extracted Agiso API and callback documentation
- generating signed request examples and callback handlers
- packaging the workflow as a reusable Codex skill

## Repository Layout

```text
.
├── knowledge-base/
│   ├── docs/
│   ├── extracted/
│   ├── raw_js/
│   └── extract_docs.py
├── skill/
│   ├── README.md
│   └── agiso-open-platform/
│       ├── SKILL.md
│       ├── agents/
│       ├── references/
│       └── scripts/
└── README.md
```

## Quick Start

1. Inspect the skill entrypoint at `skill/agiso-open-platform/SKILL.md`.
2. Read `skill/agiso-open-platform/references/service-map.md` if you need to map a business workflow to the right Agiso service.
3. Use the helper scripts in `skill/agiso-open-platform/scripts/` for deterministic tasks such as signing, doc search, or service lookup.
4. Treat `knowledge-base/` as the local evidence layer that the skill reads from.
5. If you want to install this skill into Codex, Claude Code, or Claude, start with `INSTALL_SKILLS.md`.

## Skill And Path Contract

The repository name is `agiso-open-platform-workspace`.
The skill identifier and directory name remain `agiso-open-platform`.

Skill scripts resolve the knowledge base from one of these sources:

1. `AGISO_KNOWLEDGE_BASE_ROOT`
2. `<repo>/knowledge-base`

That removes the previous implicit relative-path coupling and makes the skill portable across clones.

## Open Source Scope

The original code, repository documentation, and skill materials in this repository are released under the MIT License. See `LICENSE`.

Important boundary:

- `knowledge-base/docs/`, `knowledge-base/extracted/`, and `knowledge-base/raw_js/` contain third-party or derived materials sourced from Agiso public properties.
- Those materials are not automatically covered by the repository's MIT license unless the upstream rights holder allows it.
- If you plan to redistribute this repository publicly, review the provenance and rights for those materials first.

See `THIRD_PARTY_NOTICES.md` for the exact scope and limitations.

## Contributing

Please read `CONTRIBUTING.md` before opening pull requests.
Repository health files are provided for public collaboration:

- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `SUPPORT.md`

## Maintainer Guidance

Before publishing changes publicly:

1. Verify there are no secrets or private credentials in the working tree or commit history.
2. Re-check whether third-party Agiso materials are safe to redistribute.
3. Keep the skill instructions aligned with bundled scripts and references.
4. Keep `git status` clean before tagging or pushing.
