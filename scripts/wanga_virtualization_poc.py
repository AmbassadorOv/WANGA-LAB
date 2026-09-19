#!/usr/bin/env python3
"""Minimal WANGA virtualization POC.

Builds a deterministic logical graph from atom records. This is a prototype
graph builder, not the physical WANGA computer and not an autonomous runtime.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "architecture" / "wanga_virtual_machine_poc.json"

def endpoint(atom_id: str) -> str:
    return "neural://" + hashlib.sha256(atom_id.encode("utf-8")).hexdigest()[:32]

def build_graph(atoms: list[dict]) -> dict:
    nodes = []
    edges = []
    for atom in atoms:
        aid = atom["atom_id"]
        node = dict(atom)
        node["neural_endpoint"] = endpoint(aid)
        nodes.append(node)
        for family in atom.get("family_membership", []):
            edges.append({"type": "MEMBER_OF", "source": aid, "target": family})
        for target in atom.get("cross_family_relations", []):
            edges.append({"type": "CROSS_FAMILY", "source": aid, "target": target})
        parent = atom.get("parent")
        if parent:
            edges.append({"type": "CHILD_OF", "source": aid, "target": parent})
    return {"schema_version": "0.1.0-poc", "nodes": nodes, "edges": edges}

def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    demo_atoms = [
        {
            "atom_id": "demo:provenance",
            "family_membership": ["evidence", "governance"],
            "parent": None,
            "cross_family_relations": ["demo:logic"],
            "evidence_state": "SPECIFIED",
            "verification_state": "TESTED",
        },
        {
            "atom_id": "demo:logic",
            "family_membership": ["reasoning", "verification"],
            "parent": "demo:provenance",
            "cross_family_relations": [],
            "evidence_state": "SPECIFIED",
            "verification_state": "TESTED",
        },
    ]
    graph = build_graph(demo_atoms)
    graph["machine"] = manifest["name"]
    print(json.dumps(graph, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
