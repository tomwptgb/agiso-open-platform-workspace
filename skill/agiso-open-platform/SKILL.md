---
name: agiso-open-platform
description: Use when working with Agiso Open Platform (open.agiso.com) docs, APIs, signatures, push callbacks, service selection, or generated client/integration code for ALDS, ACS, ACPR, Open, Print, Supplier, and related services.
---

# Agiso Open Platform Skill

Use this skill for requests involving Agiso platform integration, reverse-engineered Agiso docs, API request construction, callback verification, signature generation, client SDK generation, supplier integration, or service-specific troubleshooting.

This skill lives in the `agiso-open-platform-workspace` repository. The repository name changed, but the skill identifier and directory name remain `agiso-open-platform`.
The installable skill directory is self-contained and bundles a local `knowledge-base/` snapshot.

## What This Skill Covers

- Selecting the correct Agiso service and document set
- Locating API, push, FAQ, pricing, error code, and signing docs
- Building signed requests and verifying push callback signatures
- Generating integration code, client wrappers, and request examples
- Comparing similar Agiso services across marketplaces
- Using extracted route and API indexes to find hidden or cross-linked material

## First-Principles Model

Treat every Agiso task as a composition of a small set of primitives:

- **Service**: the business domain or marketplace namespace such as `alds`, `acs`, `open`, or `supplier`
- **Identity**: the AppId, AppSecret, token, clientId, or clientSecret required by the flow
- **Request**: endpoint path, HTTP method, parameters, and service gateway
- **Signature**: deterministic parameter canonicalization plus MD5
- **Response envelope**: success flag, error code, error message, and optional data
- **Callback**: push message or supplier-side receive endpoint that must verify signatures first
- **Failure surface**: validation errors, permission issues, stale tokens, undocumented fields, and cross-service differences

Every useful output from this skill should reduce uncertainty in at least one of these primitives.

## Activation Heuristics

Use this skill when the user asks to:

- integrate with `open.agiso.com` or `gw-api.agiso.com`
- identify which Agiso service covers a marketplace or workflow
- generate request code, SDKs, callback handlers, or signature helpers
- debug `IsSuccess=false`, `Error_Code`, or signature failures
- compare similar Agiso services such as `alds*` marketplace variants
- understand supplier-mode OAuth or purchase flows

## When To Read Additional Files

- Start with `references/first-principles.md` if the task is ambiguous, architectural, or spans multiple services
- For service selection and doc locations, read `references/service-map.md`
- For capabilities and document coverage, read `references/service-matrix.md`
- For common workflows, read `references/task-playbooks.md`
- For code generation or callback implementation, read `references/implementation-patterns.md`
- For stale-doc and evidence rules, read `references/freshness-and-limitations.md`
- For extracted site structure and reverse-engineered indexes, inspect `knowledge-base/extracted/crawl_summary.json`, `knowledge-base/extracted/route_map.json`, and `knowledge-base/extracted/api_docs_index.json`
- For canonical source docs, read the matching files under `knowledge-base/docs/<service>/`
- For deterministic signing, run `scripts/agiso_sign.py`
- For service discovery, run `scripts/lookup_service.py`
- For endpoint and topic search, run `scripts/search_docs.py`
- For request skeleton generation, run `scripts/build_request_stub.py`

## Workflow

1. Identify the target primitive set: service, identity, request, signature, callback, or failure.
2. If the service is unclear, use `scripts/lookup_service.py` and then confirm with `references/service-map.md`.
3. Open the matching service docs and the smallest additional references needed.
4. If the task involves live request construction or callback handling, confirm the signing flow from the service's `signDemo.md` and use `scripts/agiso_sign.py`.
5. If the task involves an endpoint, read the service's `api.md` and then the related `errorCode.md`, `faq.md`, `push.md`, or `model.md` if needed.
6. If the docs are incomplete or inconsistent, use `scripts/search_docs.py`, `knowledge-base/extracted/api_docs_index.json`, and `knowledge-base/raw_js/` to recover names, routes, or push topics.
7. When generating code, keep request signing, base URL, service prefix, and response envelope consistent with Agiso conventions.
8. When the user wants implementation output, prefer runnable code or stubs over prose-only summaries.

## Output Rules

- State which service you are using, because many Agiso services share patterns but differ in base paths and page coverage.
- Prefer existing extracted docs over guessing.
- Call out missing fields or undocumented behavior explicitly.
- When the same concept appears in multiple services, note whether it is shared or service-specific.
- For implementation help, produce runnable request examples with signature logic shown or delegated to `scripts/agiso_sign.py`.
- Separate documented facts from inferred patterns.
- If a task depends on possibly stale scraped docs, say so and identify the exact local source used.

## Agiso Conventions

- Most service APIs use a service-specific gateway such as `https://gw-api.agiso.com/<service>/`
- Agiso responses commonly include `IsSuccess`, `Error_Code`, `Error_Msg`, and optional `Data`
- Signature generation is typically: sort params by name, concatenate `key + value`, prepend and append `AppSecret`, then compute MD5
- Push callbacks typically require signature verification before business processing

## Boundaries

- This skill is a documentation and integration skill, not a source-of-truth for merchant business policy outside the extracted docs
- If the user asks for current production behavior and the local docs may be stale, say so explicitly and recommend verification against the live platform
- If the user needs undocumented endpoint behavior, mark the answer as an inference from extracted assets or examples rather than claiming certainty
