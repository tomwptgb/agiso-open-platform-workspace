# Task Playbooks

Use these playbooks to turn Agiso documentation into reliable outputs.

## Build An API Call

1. Identify the service from the user request.
2. Read `../knowledge-base/docs/<service>/api.md`.
3. Extract request URL, method, required params, optional params, and response envelope.
4. Read `../knowledge-base/docs/<service>/signDemo.md`.
5. Build the signed request using `../scripts/agiso_sign.py` if deterministic signing is needed.
6. If auth or hosted app setup is involved, also read `../knowledge-base/docs/open/guide.md`.

## Verify A Push Callback

1. Read `../knowledge-base/docs/<service>/push.md`.
2. Read `../knowledge-base/docs/<service>/signDemo.md`.
3. Confirm which fields participate in signing.
4. Verify signature before parsing the business payload.
5. Return the minimal success body expected by the platform, if documented.

## Troubleshoot A Failed Request

1. Read `../knowledge-base/docs/<service>/errorCode.md`.
2. Compare the request to the matching section in `../knowledge-base/docs/<service>/api.md`.
3. Check signature input ordering and missing parameters.
4. If the docs are ambiguous, inspect `../knowledge-base/docs/<service>/faq.md`.
5. If still unclear, search `../knowledge-base/extracted/api_docs_index.json` and relevant files under `../knowledge-base/raw_js/`.

## Generate Client Code

1. Use the service gateway from `../knowledge-base/extracted/crawl_summary.json`.
2. Preserve the Agiso response envelope.
3. Isolate signing into a helper.
4. Expose endpoint-specific methods grouped by service.
5. Include examples for both successful response handling and `IsSuccess=false`.

## Compare Services

1. Start from `../knowledge-base/docs/README.md` and `../knowledge-base/extracted/route_map.json`.
2. Compare whether each service has `model.md`, `push.md`, and variant-specific endpoint coverage.
3. Call out shared patterns versus marketplace-specific behavior.
