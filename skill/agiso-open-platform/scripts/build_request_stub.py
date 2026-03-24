#!/usr/bin/env python3
"""Build Agiso request stubs for curl, Python, or Node.js."""

from __future__ import annotations

import argparse
import json

from data_paths import extracted_root


EXTRACTED = extracted_root()


def load_gateway(service: str) -> str:
    crawl = json.loads((EXTRACTED / "crawl_summary.json").read_text())
    gateways = crawl.get("gateway_api_urls", {})
    if service in gateways:
        return gateways[service]
    return gateways.get("other", "https://gw-api.agiso.com/{service_name}").replace("{service_name}", service)


def render_params(params: dict[str, str]) -> str:
    return ",\n    ".join(f'"{k}": "{v}"' for k, v in params.items())


def curl_stub(base_url: str, endpoint: str, params: dict[str, str]) -> str:
    form = " \\\n  ".join(f"--data-urlencode '{k}={v}'" for k, v in params.items())
    return (
        f"curl -X POST '{base_url.rstrip('/')}/{endpoint.lstrip('/')}' \\\n  "
        + form
        + " \\\n  --data-urlencode 'sign=<md5-signature>'"
    )


def python_stub(base_url: str, endpoint: str, params: dict[str, str]) -> str:
    body = render_params(params)
    return f"""import hashlib
import requests

APP_SECRET = \"replace-me\"
params = {{
    {body}
}}

payload = \"\".join(f\"{{k}}{{params[k]}}\" for k in sorted(params))
sign = hashlib.md5(f\"{{APP_SECRET}}{{payload}}{{APP_SECRET}}\".encode(\"utf-8\")).hexdigest()
params[\"sign\"] = sign

resp = requests.post(\"{base_url.rstrip('/')}/{endpoint.lstrip('/')}\", data=params, timeout=30)
print(resp.text)
"""


def node_stub(base_url: str, endpoint: str, params: dict[str, str]) -> str:
    body = render_params(params)
    return f"""import crypto from \"node:crypto\";

const APP_SECRET = \"replace-me\";
const params = {{
  {body}
}};

const payload = Object.keys(params)
  .sort()
  .map((key) => `${{key}}${{params[key]}}`)
  .join(\"\");
const sign = crypto
  .createHash(\"md5\")
  .update(`${{APP_SECRET}}${{payload}}${{APP_SECRET}}`, \"utf8\")
  .digest(\"hex\");

const form = new URLSearchParams({{ ...params, sign }});
const resp = await fetch(\"{base_url.rstrip('/')}/{endpoint.lstrip('/')}\", {{
  method: \"POST\",
  headers: {{ \"Content-Type\": \"application/x-www-form-urlencoded\" }},
  body: form,
}});

console.log(await resp.text());
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--service", required=True, help="Agiso service name")
    parser.add_argument("--endpoint", required=True, help="Endpoint path such as /Item/UpdateAdditional")
    parser.add_argument(
        "--lang",
        choices=("curl", "python", "node"),
        default="python",
        help="Stub output language",
    )
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        help="Request parameter in key=value form. May be passed multiple times.",
    )
    args = parser.parse_args()

    params: dict[str, str] = {}
    for item in args.param:
        if "=" not in item:
            raise SystemExit(f"invalid --param value: {item!r}")
        key, value = item.split("=", 1)
        params[key] = value

    base_url = load_gateway(args.service)
    if args.lang == "curl":
        print(curl_stub(base_url, args.endpoint, params))
    elif args.lang == "python":
        print(python_stub(base_url, args.endpoint, params))
    else:
        print(node_stub(base_url, args.endpoint, params))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
