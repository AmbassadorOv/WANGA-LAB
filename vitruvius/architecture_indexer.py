#!/usr/bin/env python3
"""Vitruvius architecture indexer.

Reads repository seed/scan inputs and produces a deterministic architecture-book
record. Provider/model-assisted extraction can be attached behind the same
normalized output contract; no model output is promoted to VERIFIED by this tool.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
FAMILY_FILE = ROOT / "data" / "family_roots.json"
BOOK_FILE = ROOT / "data" / "architecture_book.json"


@dataclass
class RepoObservation:
    repository: str
    default_branch: str
    source: str
    family: str
    wanga_target: str
    status: str = "OBSERVED"
    evidence_state: str = "UNVERIFIED"
    architecture_properties: list[str] | None = None
    license_status: str = "REQUIRES_REVIEW"

    def __post_init__(self) -> None:
        if self.architecture_properties is None:
            self.architecture_properties = []


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def classify(text: str, families: list[dict[str, Any]]) -> tuple[str, list[str]]:
    haystack = text.lower()
    rules = [
        ("NEURAL", ["neural", "transformer", "foundation model", "llm", "reinforcement", "neuro-symbolic"]),
        ("LOGIC", ["formal", "theorem", "prover", "reasoning", "symbolic", "constraint"]),
        ("GOVERNANCE", ["governance", "policy", "safety", "control plane", "compliance"]),
        ("MEMORY", ["memory", "knowledge graph", "vector database", "lineage", "provenance", "registry"]),
        ("ORCHESTRATION", ["orchestration", "agent framework", "multi-agent", "workflow", "runtime"]),
        ("SYSTEMS", ["distributed", "system architecture", "cloud", "compute", "scheduler"]),
    ]
    for family_id, keywords in rules:
        if any(k in haystack for k in keywords):
            return family_id, [k for k in keywords if k in haystack]
    return "SYSTEMS", []


def github_search(query: str, token: str | None) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode({"q": query, "per_page": 10})
    req = urllib.request.Request(
        f"https://api.github.com/search/repositories?{params}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "WANGA-Vitruvius-Indexer",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)
    return payload.get("items", [])


def scan(families: list[dict[str, Any]], queries: list[str], token: str | None) -> list[RepoObservation]:
    result: dict[str, RepoObservation] = {}

    for query in queries:
        for repo in github_search(query, token):
            full_name = repo.get("full_name")
            if not full_name or full_name in result:
                continue
            family, props = classify(
                " ".join(
                    [
                        full_name,
                        repo.get("name", ""),
                        repo.get("description", "") or "",
                        query,
                    ]
                ),
                families,
            )
            targets = next((x["wanga_targets"] for x in families if x["id"] == family), [])
            target = targets[0] if targets else "VITRUVIUS"
            result[full_name] = RepoObservation(
                repository=full_name,
                default_branch=repo.get("default_branch") or "UNKNOWN",
                source="GITHUB_SEARCH",
                family=family,
                wanga_target=target,
                architecture_properties=props,
            )

    return list(result.values())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", action="append", dest="queries")
    parser.add_argument("--output", default=str(BOOK_FILE))
    parser.add_argument("--token-env", default="GITHUB_TOKEN")
    args = parser.parse_args()

    families_doc = load_json(FAMILY_FILE)
    families = families_doc["families"]

    queries = args.queries or [
        "neural network architecture",
        "formal reasoning theorem proving",
        "distributed systems architecture",
        "AI governance policy architecture",
        "knowledge graph vector database memory",
        "workflow orchestration agents",
    ]

    token = os.environ.get(args.token_env)
    try:
        observations = scan(families, queries, token)
    except Exception as exc:
        print(f"Vitruvius scan failed: {exc}", file=sys.stderr)
        return 2

    output = {
        "version": "0.1.0",
        "generated_state": "OBSERVED_SCAN",
        "evidence_rule": "MODEL_OR_SEARCH_OUTPUT_IS_NOT_VERIFIED_EVIDENCE",
        "entries": [asdict(x) for x in sorted(observations, key=lambda r: r.repository.lower())],
    }

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(observations)} architecture observations to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
