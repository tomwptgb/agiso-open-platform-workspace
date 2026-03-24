#!/usr/bin/env python3
"""Generate Agiso-style MD5 signatures from request parameters."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def load_params(args: argparse.Namespace) -> dict[str, str]:
    params: dict[str, str] = {}

    if args.params_file:
        data = json.loads(Path(args.params_file).read_text())
        if not isinstance(data, dict):
            raise SystemExit("params file must contain a JSON object")
        for key, value in data.items():
            if value is not None:
                params[str(key)] = str(value)

    for item in args.param:
        if "=" not in item:
            raise SystemExit(f"invalid --param value: {item!r}")
        key, value = item.split("=", 1)
        if key == "sign":
            continue
        params[key] = value

    params.pop("sign", None)
    return params


def agiso_sign(secret: str, params: dict[str, str]) -> tuple[str, str]:
    ordered = sorted(params.items(), key=lambda item: item[0])
    payload = "".join(f"{key}{value}" for key, value in ordered)
    digest = hashlib.md5(f"{secret}{payload}{secret}".encode("utf-8")).hexdigest()
    return payload, digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--secret", required=True, help="Agiso AppSecret")
    parser.add_argument(
        "--param",
        action="append",
        default=[],
        help="Request parameter in key=value form. May be provided multiple times.",
    )
    parser.add_argument(
        "--params-file",
        help="Path to a JSON object containing request parameters.",
    )
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="Output the MD5 digest in uppercase.",
    )
    args = parser.parse_args()

    params = load_params(args)
    payload, digest = agiso_sign(args.secret, params)
    if args.uppercase:
        digest = digest.upper()

    json.dump(
        {
            "sorted_params": sorted(params.items(), key=lambda item: item[0]),
            "payload": payload,
            "sign": digest,
        },
        sys.stdout,
        ensure_ascii=False,
        indent=2,
    )
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
