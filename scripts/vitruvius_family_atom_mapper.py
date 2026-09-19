#!/usr/bin/env python3
"""Extract family atoms from ten canonical architecture sources and fold them into one neural graph."""
from __future__ import annotations
import argparse,json,hashlib,os,re
from pathlib import Path

def hid(*x): return hashlib.sha256("|".join(x).encode()).hexdigest()[:24]
def norm(s): return re.sub(r"\s+"," ",s.strip().lower())
def atomize_source(text, atoms):
    n=norm(text); found=[]
    for key,variants,families,governance in atoms:
        hits=sum(n.count(norm(v)) for v in variants)
        if hits: found.append((key,hits,families,governance))
    return found
def split_children(label):
    parts=re.split(r"\s*(?:/|&|→|↔|,|\+)\s*",label)
    return [x.strip() for x in parts if x.strip() and len(x.strip())>2]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--ontology",default="vitruvius/FAMILY_ATOM_GOVERNANCE_ONTOLOGY_V1.json")
    ap.add_argument("--output",default="vitruvius/TEN_ARCHITECTURE_FAMILY_ATOM_NEURAL_GRAPH_V1.json")
    args=ap.parse_args()
    m=json.load(open(args.ontology,encoding="utf-8"))
    nodes=[]; edges=[]; atom_seen={}; root="WANGA-GLOBAL-NEURAL-NETWORK"
    for src in m["source_files"]:
        p=Path(src)
        if not p.exists(): continue
        sid="SOURCE-"+hid(src)
        nodes.append({"id":sid,"kind":"ARCHITECTURE_SOURCE","source":src})
        text=p.read_text(encoding="utf-8",errors="replace")
        for key,hits,fams,gov in atomize_source(text,m["atoms"]):
            aid="ATOM-"+key
            if aid not in atom_seen:
                endpoint="NEURAL-ATOM-ENDPOINT-"+hid(key)
                atom_seen[aid]={"id":aid,"kind":"FAMILY_ATOM","atom":key,"families":fams,"governance":gov,"neural_endpoint":endpoint,"global_network":root}
                nodes.append(atom_seen[aid])
                for fam in fams: edges.append({"source":aid,"target":"FAMILY-"+fam,"relation":"BELONGS_TO_FAMILY"})
                for g in gov: edges.append({"source":aid,"target":"GOV-"+g,"relation":"GOVERNED_BY"})
                edges.append({"source":aid,"target":endpoint,"relation":"WRAPPED_BY_NEURAL_ENDPOINT"})
                edges.append({"source":endpoint,"target":root,"relation":"FOLDS_INTO_GLOBAL_NETWORK"})
            edges.append({"source":sid,"target":aid,"relation":"CONTAINS_ATOM","evidence_hits":hits})
            label=key.replace("_"," ")
            for child in split_children(label):
                if child.lower()!=label.lower():
                    cid="SUBATOM-"+hid(key,child)
                    nodes.append({"id":cid,"kind":"FAMILY_SUBATOM","label":child,"parent_atom":aid})
                    edges.append({"source":aid,"target":cid,"relation":"RECURSIVE_ATOMIC_DECOMPOSITION"})
    for fam in m["root_families"]:
        nodes.append({"id":"FAMILY-"+fam,"kind":"FAMILY_ROOT","label":fam})
    for g in m["governance_layers"]:
        nodes.append({"id":"GOV-"+g,"kind":"GOVERNANCE_LAYER","label":g,"members":m["governance_layers"][g]})
    cross=[a for a in atom_seen.values() if len(a["families"])>=2]
    for atom in cross:
        fams=atom["families"]
        for i in range(len(fams)):
            for j in range(i+1,len(fams)):
                edges.append({"source":"FAMILY-"+fams[i],"target":"FAMILY-"+fams[j],"relation":"CROSS_FAMILY_ATOM_BRIDGE","atom":atom["atom"]})
    out={"engine":"VITRUVIUS_FAMILY_ATOM_NEURAL_MAPPER","source_file_count":len(m["source_files"]),"sources_present":sum(1 for s in m["source_files"] if Path(s).exists()),"family_count":len(m["root_families"]),"atom_count":len(atom_seen),"cross_family_atom_count":len(cross),"subatom_count":sum(1 for n in nodes if n["kind"]=="FAMILY_SUBATOM"),"governance_layer_count":len(m["governance_layers"]),"global_network":root,"nodes":nodes,"edges":edges}
    os.makedirs(os.path.dirname(args.output),exist_ok=True)
    json.dump(out,open(args.output,"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    print(json.dumps({k:out[k] for k in ["source_file_count","sources_present","family_count","atom_count","cross_family_atom_count","subatom_count","governance_layer_count"]},indent=2))
if __name__=="__main__": main()
