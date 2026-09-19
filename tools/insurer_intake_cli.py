"""CLI adapter for machine-readable insurer intake."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from tools.insurer_pipeline import build_pipeline

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--active-limit", type=int)
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    records = data.get("records")
    if not isinstance(records, list):
        raise SystemExit("input must contain a records array")
    active_limit = args.active_limit
    if active_limit is None:
        active_limit = int(data.get("active_limit", 0))
    if active_limit < 0:
        raise SystemExit("active-limit must be non-negative")

    result = {
        "scenario": data.get("scenario", "UNSPECIFIED"),
        "active_limit": active_limit,
        "results": build_pipeline(records, active_limit),
    }
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
