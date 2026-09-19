#!/usr/bin/env python3
"""Deterministic Vitruvius architecture and research composition engine."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "docs" / "AGI_RESEARCH_MODEL_ARCHITECTURE_V1.yml"
ASSETS = ROOT / "wanga-research-groups" / "RESEARCH_ASSET_INTEGRATION_REGISTRY_V1.json"
GROUPS = ROOT / "wanga-research-groups" / "AGENT_GROUP_REGISTRY.json"
MANIFEST = ROOT / "vitruvius" / "ARCHITECTURE_GRAPH_MANIFEST_V1.json"
INDEX = ROOT / "vitruvius" / "VITRUVIUS_INDEX.json"
QUEUE = ROOT / "vitruvius" / "VITRUVIUS_WORK_QUEUE.json"
GRAPH = ROOT / "vitruvius" / "ARCHITECTURE_GRAPH.json"
RELATIONSHIPS = ROOT / "vitruvius" / "ARCHITECTURE_RELATIONSHIP_REGISTRY.json"

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def build_index(assets: dict[str, Any], groups: dict[str, Any]) -> dict[str, Any]:
    nodes = [
        {"id": "AGI-CORE", "type": "cognitive_capability", "source": str(ARCH.relative_to(ROOT)), "status": "TARGET_ARCHITECTURE"},
        {"id": "RESEARCH", "type": "research", "source": str(ARCH.relative_to(ROOT)), "status": "TARGET_ARCHITECTURE"},
        {"id": "COLLABORATION", "type": "scientist_group", "source": str(ARCH.relative_to(ROOT)), "status": "TARGET_ARCHITECTURE"},
        {"id": "MODELS", "type": "model_agent", "source": str(ARCH.relative_to(ROOT)), "status": "TARGET_ARCHITECTURE"},
        {"id": "VITRUVIUS", "type": "artifact", "source": "vitruvius/VITRUVIUS_INDEX_SCHEMA_V1.json", "status": "TARGET_ARCHITECTURE"},
    ]
    edges = [
        {"from": "RESEARCH", "relation": "requires", "to": "AGI-CORE"},
        {"from": "RESEARCH", "relation": "organizes", "to": "COLLABORATION"},
        {"from": "COLLABORATION", "relation": "routes_to", "to": "MODELS"},
        {"from": "MODELS", "relation": "produces", "to": "VITRUVIUS"},
        {"from": "VITRUVIUS", "relation": "indexes", "to": "RESEARCH"},
        {"from": "VITRUVIUS", "relation": "indexes", "to": "COLLABORATION"},
        {"from": "VITRUVIUS", "relation": "indexes", "to": "MODELS"},
    ]
    for asset in assets.get("assets", []):
        aid = asset["id"]
        nodes.append({"id": aid, "type": "research", "source": asset["path"], "domain": asset.get("primary_group", ""), "status": asset.get("status", "UNCLASSIFIED")})
        edges.append({"from": "RESEARCH", "relation": "contains_asset", "to": aid})
        for group in [asset.get("primary_group"), *asset.get("secondary_groups", [])]:
            if group:
                edges.append({"from": aid, "relation": "connected_to_group", "to": group})
    for group in groups.get("groups", []):
        gid = group["id"]
        nodes.append({"id": gid, "type": "scientist_group", "source": group["path"], "status": "CONFIGURED"})
        edges.append({"from": "COLLABORATION", "relation": "contains_group", "to": gid})
    return {"version": "1.0.0", "generated_at": now(), "nodes": nodes, "edges": edges}

def build_architecture_graph(manifest: dict[str, Any], index: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    nodes = []
    relationships = []
    for architecture in manifest.get("architectures", []):
        nodes.append({
            "id": architecture["id"], "type": "architecture",
            "source": "vitruvius/ARCHITECTURE_GRAPH_MANIFEST_V1.json",
            "name": architecture["name"], "role": architecture["role"],
            "status": architecture["status"], "branch_patterns": architecture.get("branch_patterns", []),
        })
        for pattern in architecture.get("branch_patterns", []):
            nodes.append({
                "id": f"BRANCH-PATTERN:{architecture['id']}:{pattern}", "type": "branch",
                "source": "vitruvius/ARCHITECTURE_GRAPH_MANIFEST_V1.json",
                "name": pattern, "status": "DECLARED", "architecture_id": architecture["id"],
            })
    for relation in manifest.get("relationships", []):
        relationships.append({
            "id": relation["id"], "source": relation["source"], "target": relation["target"],
            "relation_types": relation["relation_types"], "discovered_by": "VITRUVIUS",
            "status": relation.get("status", "CANDIDATE"),
            "verification_status": "NOT_VERIFIED",
        })
    for node in index.get("nodes", []):
        nodes.append({
            "id": node["id"],
            "type": "research_asset" if node["type"] == "research" else "group",
            "source": node["source"], "name": node.get("id"),
            "status": node.get("status", "UNCLASSIFIED"),
        })
    graph = {"version": "1.0.0", "generated_at": now(), "authority": "VITRUVIUS", "nodes": nodes, "relationships": relationships}
    registry = {"version": "1.0.0", "generated_at": graph["generated_at"], "authority": "VITRUVIUS", "relationships": relationships}
    return graph, registry

def build_queue(index: dict[str, Any], graph: dict[str, Any]) -> dict[str, Any]:
    research = [n for n in index["nodes"] if n["type"] == "research" and n["id"] != "RESEARCH"]
    groups = {n["id"] for n in index["nodes"] if n["type"] == "scientist_group"}
    tasks = []
    for node in research:
        candidate_groups = [e["to"] for e in index["edges"] if e["from"] == node["id"] and e["relation"] == "connected_to_group" and e["to"] in groups]
        tasks.append({
            "task_id": f"VIT-{node['id']}",
            "objective": f"Classify and map research asset {node['id']} into perspective, collaboration, capability, model, evidence and verification requirements.",
            "parent_system": "VITRUVIUS", "owner_agent": "WANGA Work Manager",
            "inputs": [node["source"]], "expected_artifact": f"vitruvius/mappings/{node['id']}.json",
            "dependencies": [], "candidate_groups": candidate_groups,
            "acceptance_checks": [
                "Research question/domain is explicit or marked unresolved",
                "Required perspective is explicit",
                "Evidence requirements are explicit",
                "Model assignment is capability-driven, not vendor-driven",
                "Verification state is preserved",
            ],
            "risk_level": "MEDIUM", "status": "QUEUED",
        })
    for rel in graph["relationships"]:
        tasks.append({
            "task_id": f"REL-{rel['id']}",
            "objective": f"Evaluate and map relationship {rel['source']} -> {rel['target']} ({', '.join(rel['relation_types'])}).",
            "parent_system": "VITRUVIUS", "owner_agent": "WANGA Global Work Manager",
            "inputs": [rel["source"], rel["target"]],
            "expected_artifact": f"vitruvius/relationship-evaluations/{rel['id']}.json",
            "dependencies": [], "acceptance_checks": [
                "Both architecture nodes are registered",
                "Relationship type is explicit",
                "Source evidence or design reference is recorded",
                "Verification status is preserved independently of discovery",
            ],
            "risk_level": "MEDIUM", "status": "CANDIDATE",
        })
    return {"version": "1.0.0", "generated_at": now(), "queue_id": "Q-VITRUVIUS-001", "tasks": tasks}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if root != ROOT:
        raise SystemExit("refusing alternate root; run from the repository checkout")
    assets = load_json(ASSETS)
    groups = load_json(GROUPS)
    manifest = load_json(MANIFEST)
    index = build_index(assets, groups)
    graph, registry = build_architecture_graph(manifest, index)
    queue = build_queue(index, graph)
    if args.write:
        for path, payload in [(INDEX, index), (QUEUE, queue), (GRAPH, graph), (RELATIONSHIPS, registry)]:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "mode": "write" if args.write else "dry-run",
        "index_nodes": len(index["nodes"]),
        "index_edges": len(index["edges"]),
        "work_items": len(queue["tasks"]),
        "architecture_nodes": len([n for n in graph["nodes"] if n["type"] == "architecture"]),
        "architecture_relationships": len(graph["relationships"]),
        "branch_patterns": len([n for n in graph["nodes"] if n["type"] == "branch"]),
    }, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
