# Implementation Patterns

Use these patterns when generating code from the Agiso docs.

## Request Builder Pattern

Every client should isolate these steps:

1. create a parameter map without `sign`
2. normalize values to strings
3. sort keys lexicographically
4. concatenate `key + value`
5. wrap with secret and compute MD5
6. add `sign`
7. send the request to the service gateway plus endpoint path
8. parse the standard response envelope

## Callback Handler Pattern

For push or supplier callbacks:

1. parse query string and form/body fields
2. rebuild the parameter set used for signing
3. verify the signature before business logic
4. reject or log failed signatures
5. process payload only after verification
6. return the minimal acknowledgement expected by the platform

## SDK Shape

If generating an SDK:

- group methods by service, not by raw endpoint alphabetically
- expose one signing helper used by all write methods
- preserve the raw endpoint path in method comments or metadata
- return the full Agiso response envelope unless the user explicitly wants unwrapped data
- include error helpers for `IsSuccess=false`

## Troubleshooting Pattern

When a request fails:

1. verify service selection
2. verify gateway URL
3. verify required params
4. verify token or credential type
5. verify signing parameter set and order
6. compare `Error_Code` against `errorCode.md`
7. search `faq.md` for workflow-specific caveats

## Supplier Pattern

Supplier flows differ from standard platform API usage:

- use `clientId` and `clientSecret`
- include an authorization redirect flow
- exchange `code` for token
- validate `access_token`
- deduplicate purchase requests using business keys such as `tid`, `oid`, and `type`

Use `../../../knowledge-base/docs/supplier/demo.md` as the local pattern source.
