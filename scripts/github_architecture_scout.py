#!/usr/bin/env python3
"""Bounded public-GitHub architecture discovery.

Searches declared domains through the GitHub REST API, records repository
metadata and license evidence, and emits candidates for later human/agent
reading. It never copies source code and never modifies main.
"""

from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "docs" / "MASTER_PROJECT_INSTRUCTIONS_V1.md"
REGISTRY = ROOT / "docs" / "ARCHITECTURE_DISCOVERY_REGISTRY.json"

TRACKS = {
    "ARCH-01": [
        "agent orchestration workflow engine",
        "distributed workflow state machine",
        "AI control plane agent runtime",
        "multi agent task graph",
    ],
    "ARCH-02": [
        "AI agent memory planning routing",
        "multi agent evaluation tool use",
        "LLM model router context management",
        "agent handoff coordination",
    ],
    "ARCH-03": [
        "AI evaluation provenance observability",
        "AI verification security runtime",
        "machine learning audit infrastructure",
        "formal reasoning verification engine",
    ],
}

def github_json(url: str, token: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "WANGA-LAB-Architecture-Scout",
        },
    )
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)

def search(token: str, query: str) -> list[dict]:
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode({
        "q": query + " in:name,description",
        "sort": "stars",
        "order": "desc",
        "per_page": "10",
    })
    return github_json(url, token).get("items", [])

def main() -> None:
    if not MASTER.exists():
        raise SystemExit("Missing canonical master project instructions")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is required for controlled discovery")

    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    records = []

    for agent_id, queries in TRACKS.items():
        for query in queries:
            for item in search(token, query):
                license_name = None
                license_spdx = None
                lic = item.get("license") or {}
                if isinstance(lic, dict):
                    license_name = lic.get("name")
                    license_spdx = lic.get("spdx_id")
                records.append({
                    "record_id": f"{agent_id}:{item['full_name']}:{query}",
                    "agent_id": agent_id,
                    "repository": item["full_name"],
                    "repository_url": item.get("html_url"),
                    "commit_or_tag": None,
                    "license": license_name,
                    "license_spdx": license_spdx,
                    "discovery_query": query,
                    "discovered_at": now,
                    "architecture_domain": item.get("description"),
                    "status": "DISCOVERED",
                    "pattern": None,
                    "evidence_refs": [item.get("html_url")] if item.get("html_url") else [],
                    "adaptation_proposal": None,
                    "verification_status": "NOT_RUN",
                })

    dedup = {}
    for record in records:
        dedup[(record["agent_id"], record["repository"])] = record
    registry["generated_at"] = now
    registry["records"] = sorted(dedup.values(), key=lambda r: (r["agent_id"], r["repository"]))
    registry["status"] = "DISCOVERED_CANDIDATES"
    REGISTRY.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "OK",
        "agents": list(TRACKS),
        "candidate_records": len(registry["records"]),
        "license_evidence_required_before_adoption": True,
    }))

if __name__ == "__main__":
    main()
