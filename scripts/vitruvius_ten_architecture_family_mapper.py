#!/usr/bin/env python3
"""Map the ten canonical ASCII architecture files into family, descendant and governance layers."""
import argparse,json,hashlib,os
def hid(*x): return hashlib.sha256("|".join(x).encode()).hexdigest()[:24]
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--manifest",default="vitruvius/TEN_ARCHITECTURE_FAMILY_GOVERNANCE_MAP_V1.json")
    ap.add_argument("--output",default="vitruvius/TEN_ARCHITECTURE_NEURAL_GOVERNANCE_GRAPH_V1.json")
    a=ap.parse_args()
    m=json.load(open(a.manifest,encoding="utf-8"))
    nodes=[]; edges=[]
    root="WANGA-GLOBAL-NEURAL-NETWORK"
    for b in m["architecture_bindings"]:
        source_id="ARCH-SOURCE-"+hid(b["source"])
        nodes.append({"id":source_id,"kind":"ARCHITECTURE_SOURCE","source":b["source"],"root_family":b["root"]})
        for child in b["children"]:
            cid="ARCH-CHILD-"+hid(b["source"],child)
            endpoint="NEURAL-ENDPOINT-"+hid(cid)
            nodes.append({"id":cid,"kind":"ARCHITECTURE_CHILD","label":child,"source":b["source"],"root_family":b["root"],"governance":b["governance"],"neural_endpoint":endpoint})
            edges.extend([
              {"source":source_id,"target":cid,"relation":"ROOTS"},
              *[{"source":cid,"target":"GOV-"+g,"relation":"GOVERNED_BY"} for g in b["governance"]],
              {"source":cid,"target":endpoint,"relation":"WRAPPED_BY_NEURAL_ENDPOINT"},
              {"source":endpoint,"target":root,"relation":"FOLDS_INTO_GLOBAL_NETWORK"}
            ])
    for g,children in m["governance"].items():
        gid="GOV-"+g
        nodes.append({"id":gid,"kind":"GOVERNANCE_LAYER","label":g,"children":children})
    out={"engine":"VITRUVIUS_TEN_ARCHITECTURE_FAMILY_MAPPER","root_network":root,"source_file_count":len(m["source_files"]),"architecture_source_nodes":sum(n["kind"]=="ARCHITECTURE_SOURCE" for n in nodes),"architecture_child_nodes":sum(n["kind"]=="ARCHITECTURE_CHILD" for n in nodes),"governance_nodes":sum(n["kind"]=="GOVERNANCE_LAYER" for n in nodes),"neural_endpoints":sum(n["kind"]=="ARCHITECTURE_CHILD" for n in nodes),"nodes":nodes,"edges":edges}
    os.makedirs(os.path.dirname(a.output),exist_ok=True);json.dump(out,open(a.output,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print(json.dumps({k:out[k] for k in ["source_file_count","architecture_source_nodes","architecture_child_nodes","governance_nodes","neural_endpoints"]},indent=2))
if __name__=="__main__": main()
