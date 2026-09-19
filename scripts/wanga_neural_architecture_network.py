#!/usr/bin/env python3
"""WANGA Neural Architecture Network Engine."""
from __future__ import annotations
import argparse, hashlib, json, os
from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class NeuralMessage:
    message_id: str
    source: str
    target: str
    kind: str
    payload: dict[str, Any]
    weight: float
    evidence_state: str = "UNVERIFIED"

@dataclass
class NodeState:
    node_id: str
    activation: float = 0.0
    confidence: float = 0.0
    inbox: int = 0
    outbox: int = 0

class NeuralArchitectureNetwork:
    def __init__(self, manifest):
        self.manifest = manifest
        self.nodes = {a["id"]: NodeState(a["id"]) for a in manifest.get("architectures", [])}
        self.edges = [e for e in manifest.get("relationships", [])
                      if e["source"] in self.nodes and e["target"] in self.nodes]

    @staticmethod
    def weight(source, target, relation):
        raw = hashlib.sha256(f"{source}|{target}|{relation}".encode()).digest()
        x = int.from_bytes(raw[:8], "big") / 2**64
        return round(0.25 + 0.75 * x, 6)

    def propagate(self, source, payload, kind="STATE_UPDATE"):
        if source not in self.nodes:
            raise KeyError(source)
        messages = []
        for edge in [e for e in self.edges if e["source"] == source]:
            relation = edge.get("relation_types", ["related"])[0]
            weight = self.weight(source, edge["target"], relation)
            message_id = hashlib.sha256(
                json.dumps([source, edge["target"], kind, payload, weight], sort_keys=True).encode()
            ).hexdigest()[:20]
            messages.append(NeuralMessage(message_id, source, edge["target"], kind, payload, weight))
            self.nodes[source].outbox += 1
            target = self.nodes[edge["target"]]
            target.inbox += 1
            target.activation = round(0.8 * target.activation + 0.2 * weight, 6)
            target.confidence = round(min(1.0, 0.8 * target.confidence + 0.2 * weight), 6)
        return messages

    def topology(self):
        return {"node_count": len(self.nodes), "edge_count": len(self.edges),
                "nodes": [asdict(x) for x in self.nodes.values()], "edges": self.edges}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="vitruvius/ARCHITECTURE_GRAPH_MANIFEST_V1.json")
    ap.add_argument("--source")
    ap.add_argument("--payload", default='{"event":"architecture_state"}')
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    manifest = json.load(open(args.manifest, encoding="utf-8"))
    net = NeuralArchitectureNetwork(manifest)
    result = {"engine": "WANGA_NEURAL_ARCHITECTURE_NETWORK", "topology": net.topology()}
    if args.source:
        result["messages"] = [asdict(m) for m in net.propagate(args.source, json.loads(args.payload))]
        result["topology_after_propagation"] = net.topology()
    if args.write:
        os.makedirs("vitruvius", exist_ok=True)
        with open("vitruvius/NEURAL_ARCHITECTURE_NETWORK_STATE.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
