#!/usr/bin/env python3
"""Vitruvius Three-Family Branch Tree.

Classifies every discovered WANGA-LAB branch into three top-level families,
then recursively wraps each branch with subfamily, role, neural endpoint and
global-network bindings.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re

FAMILIES={
 "COMPUTATIONAL_NEURAL":{"keywords":["neural","ntm","architecture","runtime","compiler","gpu","model-fabric","work-manager","autonomous","vitruvius","wanga-computer","ark-sl","ark/","poc-autonomous"]},
 "EVIDENCE_GOVERNANCE":{"keywords":["drift","evidence","governance","governance/","control-plane","insurance","insurer","verification","audit","whitepaper","epistemic"]},
 "PUBLICATION_RESEARCH":{"keywords":["publication","profile","research","copernicus","wanga-x","system-100","homepage","composition","standard","static-blog"]}
}
def stable(*p): return hashlib.sha256("|".join(map(str,p)).encode()).hexdigest()[:24]
def family(name):
    n=name.lower()
    scores={k:sum(1 for w in v["keywords"] if w in n) for k,v in FAMILIES.items()}
    best=max(scores,key=scores.get)
    return best if scores[best] else "PUBLICATION_RESEARCH"
def subfamily(name,fam):
    n=name.lower()
    if fam=="COMPUTATIONAL_NEURAL":
        if any(x in n for x in ["neural","ntm","poc-autonomous"]): return "NEURAL_COMPUTATION"
        if any(x in n for x in ["runtime","compiler","gpu","ark"]): return "RUNTIME_FABRIC"
        return "ARCHITECTURE_SYSTEMS"
    if fam=="EVIDENCE_GOVERNANCE":
        if any(x in n for x in ["drift","evidence","whitepaper","epistemic"]): return "EVIDENCE_DRIFT"
        if any(x in n for x in ["governance","control-plane","standard"]): return "GOVERNANCE_CONTROL"
        return "ASSURANCE_SERVICES"
    if any(x in n for x in ["publication","profile","homepage","static-blog"]): return "PUBLICATION"
    return "RESEARCH_COMPOSITION"
def classify(branches):
    nodes=[]
    for b in branches:
        fam=family(b["name"]); sub=subfamily(b["name"],fam)
        branch_id="BRANCH-"+stable(b["name"],b["sha"])
        family_id="FAMILY-"+stable(fam)
        sub_id="SUBFAMILY-"+stable(fam,sub)
        neural="NEURAL-ENDPOINT-"+stable(branch_id)
        nodes.append({
          "branch_id":branch_id,"branch":b["name"],"commit_sha":b["sha"],
          "family":fam,"subfamily":sub,"family_id":family_id,"subfamily_id":sub_id,
          "neural_endpoint":neural,
          "global_network":"WANGA-GLOBAL-NEURAL-NETWORK",
          "relations":["BELONGS_TO_FAMILY","BELONGS_TO_SUBFAMILY","WRAPPED_BY_NEURAL_ENDPOINT","FOLDS_INTO_GLOBAL_NETWORK"]
        })
    return nodes
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",default="vitruvius/BRANCH_DISCOVERY_SNAPSHOT_V1.json")
    ap.add_argument("--output",default="vitruvius/THREE_FAMILY_BRANCH_TREE_V1.json")
    args=ap.parse_args()
    data=json.load(open(args.input,encoding="utf-8"))
    nodes=classify(data["branches"])
    summary={f:sum(1 for n in nodes if n["family"]==f) for f in FAMILIES}
    sub={s:sum(1 for n in nodes if n["subfamily"]==s) for s in sorted(set(n["subfamily"] for n in nodes))}
    out={"engine":"VITRUVIAN_THREE_FAMILY_BRANCH_TREE","branch_count":len(nodes),"families":summary,"subfamilies":sub,"nodes":nodes}
    os.makedirs(os.path.dirname(args.output),exist_ok=True)
    json.dump(out,open(args.output,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print(json.dumps({"branch_count":len(nodes),"families":summary,"subfamilies":sub},indent=2,ensure_ascii=False))
if __name__=="__main__": main()
