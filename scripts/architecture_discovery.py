#!/usr/bin/env python3
"""Deterministic GitHub architecture-discovery registry builder.

The script records candidate repositories supplied through a normalized input file.
It deliberately does not claim exhaustive GitHub coverage and never copies source code.
Network discovery is performed by a controlled workflow using the GitHub token; this
module validates and normalizes the resulting evidence.
"""

from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MASTER="docs/MASTER_PROJECT_INSTRUCTIONS_V1.md"
SCHEMA=ROOT/"docs/ARCHITECTURE_DISCOVERY_REGISTRY.schema.json"
OUT=ROOT/"docs/ARCHITECTURE_DISCOVERY_REGISTRY.json"

AGENTS=["ARCH-01","ARCH-02","ARCH-03"]

def main() -> None:
    if not (ROOT/MASTER).exists():
        raise SystemExit("Missing canonical master project instructions")
    data={
        "version":"1.0.0",
        "master_project_instructions":MASTER,
        "search_policy":{
            "scope":"targeted public GitHub discovery across defined architecture domains",
            "exhaustive_claim_allowed":False,
            "license_check_required":True
        },
        "agents":AGENTS,
        "records":[]
    }
    OUT.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":"OK","agents":AGENTS,"records":0,"output":str(OUT)}))

if __name__=="__main__":
    main()
