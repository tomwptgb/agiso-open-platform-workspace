# Contributing

Thanks for contributing.

## Before You Start

- Read `README.md` for repository structure and licensing boundaries.
- Treat `knowledge-base/` as an evidence layer with provenance constraints.
- Keep changes scoped and explain why they are needed.

## Contribution Rules

- Prefer focused pull requests over broad rewrites.
- Do not commit secrets, tokens, or private customer data.
- Do not add third-party materials unless you are confident they can be redistributed.
- Keep skill instructions, references, and scripts consistent with each other.
- Update repository documentation when workflows or boundaries change.

## Skill Changes

When editing `skill/agiso-open-platform/`:

- keep `SKILL.md` concise and procedural
- move detailed material into `references/` instead of bloating `SKILL.md`
- add scripts only when deterministic reuse is materially better than prose
- keep `agents/openai.yaml` aligned with the skill's purpose

## Pull Request Checklist

- The change has a clear reason and scope.
- Repository docs still reflect reality.
- No secrets were added.
- Licensing or provenance implications were considered.
- `git status` is clean after the change is committed.
