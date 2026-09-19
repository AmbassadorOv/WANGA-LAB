#!/usr/bin/env python3
"""Vitruvius Fractal Recursive Network Engine.

Builds a recursive family-of-families graph from discovered GitHub artifacts and
folds every accepted local branch network into one global neural topology.
"""
from __future__ import annotations
import argparse, hashlib, json, os
from pathlib import PurePosixPath

def stable_id(*parts):
    return hashlib.sha256("|".join(parts).encode()).hexdigest()[:20]

def family_path(path):
    parts=[p for p in PurePosixPath(path).parts if p not in (".","")]
    if not parts: return ["ROOT"]
    return ["ROOT"] + parts

def build(report):
    nodes, edges = {}, []
    def add(node_id, kind, label, level, parent=None, **extra):
        if node_id not in nodes:
            nodes[node_id]={"id":node_id,"kind":kind,"label":label,"level":level,**extra}
        if parent and (parent,node_id) not in {(e["source"],e["target"]) for e in edges}:
            edges.append({"source":parent,"target":node_id,"relation":"CONTAINS"})
    add("GITHUB-GLOBAL","GLOBAL","GitHub Global Neural Topology",0)
    for c in report.get("candidates",[]):
        repo=c["repo"]; path=c["path"]
        repo_id="REPO-"+stable_id(repo)
        add(repo_id,"REPOSITORY",repo,1,"GITHUB-GLOBAL")
        parent=repo_id
        for level,part in enumerate(family_path(path)[1:],2):
            fid="FAMILY-"+stable_id(repo, *family_path(path)[:level-1])
            add(fid,"FAMILY",part,level,parent)
            parent=fid
        artifact="ARTIFACT-"+stable_id(repo,path)
        add(artifact,"ARTIFACT",path,level+1,parent,architectures=c.get("architectures",[]),score=c.get("score",0))
        edges.append({"source":artifact,"target":"GITHUB-GLOBAL","relation":"FEEDS_GLOBAL_NETWORK"})
    # Fold integration branches into the same topology.
    for i in report.get("integrations",[]):
        bid="BRANCH-"+stable_id(i.get("branch",""))
        add(bid,"INTEGRATION_BRANCH",i.get("branch",""),2,"GITHUB-GLOBAL")
        target="ARCH-"+stable_id(i.get("architecture",""))
        add(target,"ARCHITECTURE",i.get("architecture",""),1,"GITHUB-GLOBAL")
        edges.append({"source":bid,"target":target,"relation":"MAPS_TO"})
    return {"engine":"VITRUVIUS_FRACTAL_RECURSIVE_NETWORK","nodes":list(nodes.values()),"edges":edges,
            "node_count":len(nodes),"edge_count":len(edges),
            "recursive_rule":"repository -> branch -> family -> subfamily -> artifact -> architecture -> global neural network"}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--report",default="vitruvius/CONNECTOR_DISCOVERY_REPORT.json")
    ap.add_argument("--output",default="vitruvius/GITHUB_FRACTAL_NEURAL_NETWORK.json")
    args=ap.parse_args()
    report=json.load(open(args.report,encoding="utf-8"))
    graph=build(report)
    os.makedirs(os.path.dirname(args.output),exist_ok=True)
    json.dump(graph,open(args.output,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print(json.dumps({"node_count":graph["node_count"],"edge_count":graph["edge_count"],"output":args.output},indent=2))

if __name__=="__main__": main()
