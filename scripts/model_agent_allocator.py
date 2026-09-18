#!/usr/bin/env python3
"""Deterministic 5,000-slot Digital Model Agent allocator.

Slots are architectural identities. They are not live model connections.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "MODEL_FAMILY_REGISTRY.yml"
OUT = ROOT / "docs" / "MODEL_AGENT_ALLOCATION.json"

ENTRY_RE = re.compile(
    r"^\s*- id: ([^\n]+)\n"
    r"\s+target_slots: (\d+)\n"
    r"\s+general_role: ([^\n]+)\n"
    r"\s+private_roles: \[([^\]]*)\]",
    re.M,
)

def parse():
    raw = REGISTRY.read_text(encoding="utf-8")
    rows = []
    for family, count, general, private in ENTRY_RE.findall(raw):
        roles = [x.strip() for x in private.split(",") if x.strip()]
        rows.append((family, int(count), general.strip(), roles))
    return rows

def main():
    rows = parse()
    total = sum(count for _, count, _, _ in rows)
    if total != 5000:
        raise SystemExit(f"allocation target must equal 5000; got {total}")

    agents = []
    for family, count, general, private in rows:
        for index in range(1, count + 1):
            agents.append({
                "model_agent_id": f"dma-{family}-{index:04d}",
                "slot_status": "UNBOUND",
                "family": family,
                "provider": None,
                "model_id": None,
                "general_role": general,
                "private_roles": private,
                "adapter": "UNBOUND",
                "verification_status": "NOT_RUN",
                "provenance": ["docs/MODEL_FAMILY_REGISTRY.yml"],
                "ntm_interface": "BOUND_ON_VERIFICATION"
            })

    OUT.write_text(json.dumps({
        "version": 1,
        "target_model_slots": total,
        "allocated_slots": len(agents),
        "connected_slots": 0,
        "verified_slots": 0,
        "status": "SCAFFOLD_ONLY",
        "principle": "slot != live model; activation requires discovery and verification",
        "agents": agents
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(json.dumps({
        "target_model_slots": total,
        "allocated_slots": len(agents),
        "connected_slots": 0,
        "verified_slots": 0,
        "status": "SCAFFOLD_ONLY"
    }, indent=2))

if __name__ == "__main__":
    main()
