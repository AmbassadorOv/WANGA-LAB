#!/usr/bin/env python3
"""Scalable recursive branch fabric for the global WANGA neural topology."""
from __future__ import annotations
import argparse, hashlib, json, os
from dataclasses import dataclass
from typing import Iterator

@dataclass(frozen=True)
class BranchNode:
    node_id: str
    parent_id: str | None
    seed_branch: str
    depth: int
    ordinal: int
    kind: str
    neural_endpoint: str

def stable_id(*parts: object) -> str:
    return hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()[:24]

def branch_node(seed: str, parent: str | None, depth: int, ordinal: int, kind: str) -> BranchNode:
    node_id = "BRANCH-" + stable_id(seed, parent or "ROOT", depth, ordinal, kind)
    return BranchNode(node_id, parent, seed, depth, ordinal, kind, "NEURAL-ENDPOINT-" + stable_id(node_id))

def iter_nodes(seed_branches: list[str], fanout: int, micro_fanout: int) -> Iterator[BranchNode]:
    for seed in seed_branches:
        root = branch_node(seed, None, 0, 0, "SEED")
        yield root
        for i in range(fanout):
            child = branch_node(seed, root.node_id, 1, i, "RECURSIVE")
            yield child
            for j in range(micro_fanout):
                yield branch_node(seed, child.node_id, 2, j, "MICRO")

def counts(seed_count: int, fanout: int, micro_fanout: int) -> dict[str,int]:
    recursive=seed_count*fanout
    micro=recursive*micro_fanout
    return {"seed":seed_count,"recursive":recursive,"micro":micro,"total":seed_count+recursive+micro}

def sample(nodes: Iterator[BranchNode], limit: int) -> list[dict]:
    out=[]
    for i,node in enumerate(nodes):
        if i>=limit: break
        out.append(node.__dict__)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",default="vitruvius/GITHUB_BRANCH_FABRIC_MANIFEST_V1.json")
    ap.add_argument("--sample",type=int,default=32)
    ap.add_argument("--write",action="store_true")
    ap.add_argument("--output",default="vitruvius/GITHUB_BRANCH_FABRIC_STATE.json")
    args=ap.parse_args()
    manifest=json.load(open(args.manifest,encoding="utf-8"))
    seeds=manifest["seed_branches"]
    fanout=manifest["expansion"]["children_per_seed_branch"]
    micro=manifest["expansion"]["micro_children_per_expanded_branch"]
    state={"engine":"VITRUVIUS_BRANCH_FABRIC","logical_only":True,"counts":counts(len(seeds),fanout,micro),"neural_binding":"one neural endpoint per logical branch node","global_fold":"WANGA Neural Architecture Network","sample":sample(iter_nodes(seeds,fanout,micro),args.sample)}
    if args.write:
        os.makedirs(os.path.dirname(args.output),exist_ok=True)
        json.dump(state,open(args.output,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print(json.dumps(state,indent=2,ensure_ascii=False))
if __name__=="__main__":
    main()
