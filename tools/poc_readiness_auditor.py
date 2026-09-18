#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def find_files(patterns):
    out=[]
    for pat in patterns:
        out += [str(p.relative_to(ROOT)) for p in ROOT.rglob(pat)]
    return sorted(set(out))

def run(cmd):
    try:
        p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True,timeout=180)
        return p.returncode==0,(p.stdout+"\n"+p.stderr).strip()[-4000:]
    except Exception as e: return False,str(e)

def add(checks,name,category,ok,evidence,weight):
    checks.append({"name":name,"category":category,"status":"VERIFIED" if ok else "MISSING/FAILED",
                   "score":1.0 if ok else 0.0,"weight":weight,"evidence":evidence})

checks=[]
add(checks,"NTM executable core","implementation",
    (ROOT/"wanga-research-groups/neural_thinking_machine/ntm_core.py").exists(),
    find_files(["*ntm*.py"]),.20)
add(checks,"ARK Kernel","implementation",(ROOT/"ark_kernel.py").exists(),["ark_kernel.py"],.10)
add(checks,"Verification protocol","verification",
    (ROOT/"ai-drift-forensics/VERIFICATION_PROTOCOL.md").exists(),
    ["ai-drift-forensics/VERIFICATION_PROTOCOL.md"],.10)
add(checks,"Drift Forensics","drift",(ROOT/"ai-drift-forensics").exists(),
    find_files(["*drift*.py","*forensic*.py","*DRIFT*.md"]),.15)
add(checks,"Memory/Audit","memory",
    bool(find_files(["*memory*.py","*audit*.py","*persistence*.py","*MEMORY*.md","*AUDIT*.md"])),
    find_files(["*memory*.py","*audit*.py","*persistence*.py","*MEMORY*.md","*AUDIT*.md"]),.10)
add(checks,"Research/Vitruvius","research",
    bool(find_files(["*research*.py","*vitruvius*.py","*cluster*.py","*graph*.py","*RESEARCH*.md","*VITRUVIUS*.md"])),
    find_files(["*research*.py","*vitruvius*.py","*cluster*.py","*graph*.py","*RESEARCH*.md","*VITRUVIUS*.md"]),.10)
add(checks,"API","api",bool(find_files(["*api*.py","*fastapi*.py","main.py"])),
    find_files(["*api*.py","*fastapi*.py","main.py"]),.05)
ok,out=run([sys.executable,"-m","compileall","-q","."])
add(checks,"Python compilation","testing",ok,[out] if out else [],.10)
ok,out=run([sys.executable,"-m","pytest","-q"])
add(checks,"Automated tests","testing",ok,[out] if out else [],.10)

weighted=sum(c["score"]*c["weight"] for c in checks)/sum(c["weight"] for c in checks)
hard=[c["name"] for c in checks if c["name"] in ("Python compilation","Automated tests") and c["score"]<1]
verdict="NOT_READY" if hard else ("POC_PARTIAL" if weighted<.85 else "POC_READY")
report={"project":"WANGA-LAB","readiness_score_percent":round(weighted*100,2),
        "verdict":verdict,"hard_failures":hard,"checks":checks}
print(json.dumps(report,indent=2,ensure_ascii=False))
(ROOT/"POC_READINESS_REPORT.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
sys.exit(0 if verdict=="POC_READY" else 1)
