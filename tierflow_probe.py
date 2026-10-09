#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Probe an OpenAI-compatible relay endpoint: list models and check latency.

Sample usage:
    python tierflow_probe.py https://your-relay.example.com 5
"""

import os
import sys
import time
import urllib.request


def list_models(base_url, key):
    req = urllib.request.Request(
        base_url.rstrip("/") + "/v1/models",
        headers={"Authorization": f"Bearer {key}"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = resp.read().decode("utf-8", "replace")
    return data


def main():
    if len(sys.argv) < 3:
        print("usage: tierflow_probe.py <base_url> <n_checks>")
        return 1
    base_url = sys.argv[1]
    key = os.environ.get("RELAY_API_KEY", "")
    start = time.time()
    body = list_models(base_url, key)
    elapsed = time.time() - start
    print(f"{base_url} -> {len(body)} bytes in {elapsed:.2f}s")
    print(body[:200])
    return 0


if __name__ == "__main__":
    sys.exit(main())
