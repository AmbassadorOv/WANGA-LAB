#!/usr/bin/env python3
"""Vitruvius branch-architecture census and bounded expansion planner."""

from __future__ import annotations

import json
import os
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "vitruvius" / "ARCHITECTURE_BRANCH_CAPACITY.json"

OFFICES = [
    "evidence-provenance",
    "verification-audit",
    "ai-drift-forensics",
    "architecture-intelligence-vitruvius",
    "model-fabric-models",
    "digital-agents",
    "compute-infrastructure",
    "industrial-execution",
    "finance-banking-insurance",
    "organizations-operations",
    "policy-authorization-risk",
    "integration-deployment",
    "standards-interoperability",
    "global-branch-managers",
    "algorithmic-neural-governance",
]
SLOTS_PER_OFFICE = 1500
TARGET_TOTAL = len(OFFICES) * SLOTS_PER_OFFICE

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

def github_get(path: str, token: str) -> Any:
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "WANGA-Vitruvius",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)

def discover_branches(repo: str, token: str) -> list[dict[str, Any]]:
    owner, name = repo.split("/", 1)
    page = 1
    branches: list[dict[str, Any]] = []
    while True:
        data = github_get(
            f"/repos/{owner}/{name}/branches?per_page=100&page={page}",
            token,
        )
        if not data:
            break
        branches.extend(data)
        if len(data) < 100:
            break
        page += 1
    return branches

def canonical_family(branch_name: str) -> str | None:
    n = branch_name.lower()
    rules = [
        (r"(vitruvius|architecture)", "architecture-intelligence-vitruvius"),
        (r"(drift|forensic)", "ai-drift-forensics"),
        (r"(evidence|provenance)", "evidence-provenance"),
        (r"(verify|audit)", "verification-audit"),
        (r"(neural|algorithmic|ntm|rational)", "algorithmic-neural-governance"),
        (r"(compute|gpu|virtual-gpu|runtime)", "compute-infrastructure"),
        (r"(model|fabric)", "model-fabric-models"),
        (r"(agent|orchestrat)", "digital-agents"),
        (r"(industrial)", "industrial-execution"),
        (r"(finance|bank|insurance|insurer)", "finance-banking-insurance"),
        (r"(organization|operations)", "organizations-operations"),
        (r"(policy|governance|authorization|risk)", "policy-authorization-risk"),
        (r"(integration|deploy)", "integration-deployment"),
        (r"(standard|interop)", "standards-interoperability"),
        (r"(branch|lineage|family|registry)", "global-branch-managers"),
    ]
    for pattern, office in rules:
        if re.search(pattern, n):
            return office
    return None

def main() -> int:
    repo = os.environ.get("GITHUB_REPOSITORY", "AmbassadorOv/WANGA-LAB")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required for branch discovery")

    branches = discover_branches(repo, token)
    mapped = []
    unknown = []
    office_counts = {office: 0 for office in OFFICES}

    for b in branches:
        name = b["name"]
        office = canonical_family(name)
        row = {"name": name, "sha": b.get("commit", {}).get("sha"), "office_candidate": office}
        if office:
            office_counts[office] += 1
            mapped.append(row)
        else:
            unknown.append(row)

    capacity = {
        office: {
            "target_slots": SLOTS_PER_OFFICE,
            "observed_branches": office_counts[office],
            "remaining_target_slots": max(0, SLOTS_PER_OFFICE - office_counts[office]),
        }
        for office in OFFICES
    }

    result = {
        "schema_version": "1.0.0",
        "generated_at": now(),
        "repository": repo,
        "architect": "Vitruvius",
        "target_model": {
            "offices": len(OFFICES),
            "slots_per_office": SLOTS_PER_OFFICE,
            "target_total": TARGET_TOTAL,
        },
        "discovery": {
            "branches_observed": len(branches),
            "branches_mapped_to_office": len(mapped),
            "branches_unresolved": len(unknown),
        },
        "office_capacity": capacity,
        "expansion_policy": {
            "mode": "PLAN_ONLY",
            "arbitrary_branch_creation": False,
            "materialize_only_with": [
                "explicit architecture target",
                "lineage identity",
                "evidence reference",
                "verification acceptance",
            ],
            "checkpoint": "repository-registry-plus-generated-artifact",
        },
        "mapped_branches": mapped,
        "unresolved_branches": unknown,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "architect": "Vitruvius",
        "branches_observed": len(branches),
        "mapped": len(mapped),
        "unresolved": len(unknown),
        "target_total": TARGET_TOTAL,
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
