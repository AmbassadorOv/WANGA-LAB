#!/usr/bin/env python3
"""Fold the three-family branch tree into one global neural network map."""
import argparse,json,os
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--tree",default="vitruvius/THREE_FAMILY_BRANCH_TREE_V1.json")
    ap.add_argument("--fabric",default="vitruvius/GITHUB_BRANCH_FABRIC_MANIFEST_V1.json")
    ap.add_argument("--output",default="vitruvius/GLOBAL_GITHUB_NEURAL_NETWORK_MAP_V1.json")
    a=ap.parse_args()
    tree=json.load(open(a.tree,encoding="utf-8")); fabric=json.load(open(a.fabric,encoding="utf-8"))
    edges=[]
    for n in tree["nodes"]:
        edges += [
          {"source":n["branch_id"],"target":n["family_id"],"relation":"BRANCH_TO_FAMILY"},
          {"source":n["branch_id"],"target":n["subfamily_id"],"relation":"BRANCH_TO_SUBFAMILY"},
          {"source":n["branch_id"],"target":n["neural_endpoint"],"relation":"BRANCH_TO_NEURAL_ENDPOINT"},
          {"source":n["neural_endpoint"],"target":"WANGA-GLOBAL-NEURAL-NETWORK","relation":"NEURAL_ENDPOINT_TO_GLOBAL"}
        ]
    out={
      "engine":"VITRUVIUS_GLOBAL_GITHUB_NEURAL_NETWORK",
      "source_branch_count":tree["branch_count"],
      "logical_branch_fabric_nodes":fabric["expansion"]["generated_branch_nodes"],
      "top_level_families":tree["families"],
      "subfamilies":tree["subfamilies"],
      "global_node":"WANGA-GLOBAL-NEURAL-NETWORK",
      "edge_rules":["BRANCH_TO_FAMILY","BRANCH_TO_SUBFAMILY","BRANCH_TO_NEURAL_ENDPOINT","NEURAL_ENDPOINT_TO_GLOBAL"],
      "edge_count_materialized_for_discovered_branches":len(edges),
      "edges":edges
    }
    os.makedirs(os.path.dirname(a.output),exist_ok=True)
    json.dump(out,open(a.output,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print(json.dumps({k:out[k] for k in ["source_branch_count","logical_branch_fabric_nodes","top_level_families","subfamilies","edge_count_materialized_for_discovered_branches"]},indent=2,ensure_ascii=False))
if __name__=="__main__": main()
