# Install In AI Clients

[English](./INSTALL_SKILLS.md) | [简体中文](./INSTALL_SKILLS.zh-CN.md)

This repository contains one installable skill:

- skill name: `agiso-open-platform`
- repository path: `skill/agiso-open-platform/`
- primary entrypoint: `skill/agiso-open-platform/SKILL.md`

The installable directory already bundles the required `knowledge-base/` snapshot, so copying or zipping `skill/agiso-open-platform/` is sufficient.

## First-Principles Rule

This repository should only document stable facts that are specific to this project:

- which clients are intended to work
- where the skill lives in this repository
- the shortest installation path for each client
- which official guide to read when platform details change

This repository should not duplicate long, fast-changing platform manuals.

## Compatibility

Currently documented targets:

- `Codex`: installable and verified in this repository workflow
- `Claude Code`: supported by the official Claude Code Skills filesystem model
- `Claude`: supported through custom skill upload, subject to account capabilities and settings

## Install In Codex

Recommended path:

```bash
python3 /home/ubuntu/snap/codex/35/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo tomwptgb/agiso-open-platform-workspace \
  --path skill/agiso-open-platform
```

After installation, restart Codex.

Alternative local install:

```bash
mkdir -p "$HOME/skills"
cp -R /path/to/agiso-open-platform-workspace/skill/agiso-open-platform "$HOME/skills/"
```

Official references:

- OpenAI skills catalog: <https://github.com/openai/skills>

## Install In Claude Code

Claude Code discovers skills from the filesystem. The two common locations are:

- personal: `~/.claude/skills/agiso-open-platform/`
- project: `.claude/skills/agiso-open-platform/`

Personal install example:

```bash
mkdir -p ~/.claude/skills
cp -R /path/to/agiso-open-platform-workspace/skill/agiso-open-platform ~/.claude/skills/
```

Project install example:

```bash
mkdir -p .claude/skills
cp -R /path/to/agiso-open-platform-workspace/skill/agiso-open-platform .claude/skills/
```

Restart Claude Code after copying the skill.

Official references:

- Claude Code Skills docs: <https://docs.claude.com/en/docs/claude-code/skills>

## Install In Claude

Claude uses custom skill upload rather than filesystem discovery.

Minimum process:

1. Package `skill/agiso-open-platform/` as a ZIP archive.
2. In Claude, go to `Customize > Skills`.
3. Upload the ZIP file.
4. Enable the skill if needed.

Important prerequisites:

- Skills support must be available on your Claude plan
- code execution must be enabled
- for Team or Enterprise, organization settings may control access

Official references:

- Use Skills in Claude: <https://support.claude.com/en/articles/12512180-use-skills-in-claude>
- What are Skills?: <https://support.claude.com/en/articles/12512176-what-are-skills>

## What To Read First

If you only want the shortest path:

- Codex users: use the GitHub installer command above
- Claude Code users: copy the self-contained skill directory into `~/.claude/skills/`
- Claude users: upload the self-contained ZIP built from `skill/agiso-open-platform/`

## Maintenance Rule

When client install behavior changes, prefer updating only:

- the compatibility notes in this file
- the shortest project-specific install path
- the official reference links

Do not turn this repository into a fork of vendor documentation.
