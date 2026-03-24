# Security Policy

## Scope

This repository primarily contains documentation assets, extraction tooling, and a Codex skill.

## Reporting A Vulnerability

Do not open a public issue for a suspected vulnerability that could expose secrets, credentials, or private infrastructure details.

Instead:

1. contact the maintainer privately through GitHub
2. include enough detail to reproduce the issue
3. allow reasonable time for triage before public disclosure

## Sensitive Data Rules

- never commit tokens, cookies, passwords, or API secrets
- never commit private merchant or customer data
- scrub examples before publishing
