#!/usr/bin/env python3
"""Fold the scalable branch fabric into the single WANGA neural topology."""
from __future__ import annotations
import argparse, json, os, hashlib

def endpoint_id(branch_id: str) -> str:
    return "NEURAL-ENDPOINT-" + hashlib.sha256(branch_id.encode()).hexdigest()[:24]

def build(fabric: dict, architecture_manifest: dict) -> dict:
    counts=fabric["counts"]
    architecture_ids=[a["id"] for a in architecture_manifest.get("architectures",[])]
    sample=fabric.get("sample",[])
    sampled_edges=[]
    for node in sample:
        sampled_edges.append({
            "source": node["node_id"],
            "target": endpoint_id(node["node_id"]),
            "relation":"BRANCH_TO_NEURAL_ENDPOINT"
        })
    return {
        "engine":"WANGA_NEURAL_BRANCH_FOLDING",
        "global_network":"WANGA_NEURAL_ARCHITECTURE_NETWORK",
        "logical_branch_nodes":counts["total"],
        "neural_endpoint_nodes":counts["total"],
        "architecture_node_count":len(architecture_ids),
        "architecture_nodes":architecture_ids,
        "parametric_relations":[
            {"relation":"BRANCH_TO_NEURAL_ENDPOINT","cardinality":"1:1","count":counts["total"]},
            {"relation":"NEURAL_ENDPOINT_TO_GLOBAL_NETWORK","cardinality":"N:1","count":counts["total"]},
            {"relation":"NEURAL_ENDPOINT_TO_ARCHITECTURE","cardinality":"N:M","rule":"route by seed branch / architecture classification"}
        ],
        "materialization":"logical",
        "sample_edges":sampled_edges
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--fabric",default="vitruvius/GITHUB_BRANCH_FABRIC_STATE.json")
    ap.add_argument("--architecture",default="vitruvius/ARCHITECTURE_GRAPH_MANIFEST_V1.json")
    ap.add_argument("--output",default="vitruvius/NEURAL_BRANCH_FOLD_STATE.json")
    args=ap.parse_args()
    fabric=json.load(open(args.fabric,encoding="utf-8"))
    architecture=json.load(open(args.architecture,encoding="utf-8"))
    result=build(fabric,architecture)
    os.makedirs(os.path.dirname(args.output),exist_ok=True)
    json.dump(result,open(args.output,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
