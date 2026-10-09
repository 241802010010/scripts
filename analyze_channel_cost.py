#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A small tool that reads a usage dump and computes per-model call counts
and token statistics.
"""

import json
import sys
import collections


def load_records(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def summarize(records):
    per_model = collections.Counter()
    total_in = 0
    total_out = 0
    for r in records:
        per_model[r.get("model", "?")] += 1
        total_in += r.get("input_tokens", 0)
        total_out += r.get("output_tokens", 0)
    return per_model, total_in, total_out


def main():
    if len(sys.argv) < 2:
        print("usage: analyze_channel_cost.py <records.json>")
        return 1
    records = load_records(sys.argv[1])
    per_model, total_in, total_out = summarize(records)
    print("calls per model:", dict(per_model))
    print("total input tokens:", total_in)
    print("total output tokens:", total_out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
