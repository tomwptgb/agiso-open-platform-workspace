# Freshness And Limitations

This skill is built from local extracted artifacts and markdown docs, not a live contract with Agiso production systems.

## Source Hierarchy

Prefer sources in this order:

1. `../knowledge-base/docs/<service>/*.md`
2. `../knowledge-base/extracted/*.json`
3. `../knowledge-base/raw_js/*`

If a claim comes only from extracted JSON or frontend assets, state that it is inferred rather than explicitly documented.

## Freshness Risks

The local repository may lag behind the live site in:

- endpoint coverage
- parameter names
- pricing
- callback topics
- auth flow details

When current production accuracy matters, say which local file was used and recommend validating against the live platform.

## Documentation Gaps

Expect these gaps:

- missing response field details
- endpoint names present in extracted indexes but not fully documented in markdown
- service-specific variants that reuse names with slightly different behavior
- incomplete callback acknowledgement semantics

## Safe Behavior

- do not invent undocumented required parameters
- do not hide uncertainty behind generic prose
- do not collapse marketplace variants into a fake universal API
- do not assume all MD5 output should be upper or lower case unless the docs or examples show it
