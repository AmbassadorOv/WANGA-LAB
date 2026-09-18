#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def files(pattern):
    return sorted({str(p.relative_to(ROOT)) for pat in pattern for p in ROOT.rglob(pat)})

def run(cmd):
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True,timeout=180)
    return p.returncode==0,(p.stdout+"\n"+p.stderr).strip()[-3000:]

checks=[]
def add(name,category,ok,evidence=None):
    checks.append({"name":name,"category":category,"status":"VERIFIED" if ok else "MISSING/FAILED","score":1.0 if ok else 0.0,"evidence":evidence or []})

add("NTM Core","architecture",
    Path(ROOT/"wanga-research-groups/neural-thinking-machine").exists(),
    files([["*orchestrat*.py","*router*.py","*state*.py"]]))
add("Verification","verification",
    Path(ROOT/"ai-drift-forensics/VERIFICATION_PROTOCOL.md").exists(),
    files([["*verif*.py","*validation*.py"]]))
add("Drift Forensics","drift",
    Path(ROOT/"ai-drift-forensics").exists(),
    files([["*drift*.py","*forensic*.py"]]))
add("Memory/Audit","memory",
    bool(files([["*memory*.py","*audit*.py","*persistence*.py"]])),
    files([["*memory*.py","*audit*.py","*persistence*.py"]]))
add("Research/Vitruvius","research",
    bool(files([["*research*.py","*vitruvius*.py","*cluster*.py","*graph*.py"]])),
    files([["*research*.py","*vitruvius*.py","*cluster*.py","*graph*.py"]]))
add("API","api",
    bool(files([["*api*.py","*fastapi*.py"]]) or Path(ROOT/"main.py").exists()),
    files([["*api*.py","*fastapi*.py","main.py"]]))

ok,out=run([sys.executable,"-m","compileall","-q","."])
add("Python Compilation","implementation",ok,[out] if out else [])
tests=files([["test_*.py","*_test.py"],["tests/**/*.py"]])
if tests:
    ok,out=run([sys.executable,"-m","pytest","-q"])
    add("Automated Tests","testing",ok,tests+[out])
else:
    add("Automated Tests","testing",False,[])
gitok,out=run(["git","status","--short"])
add("Git Integrity","repository",gitok,[out] if out else ["clean"])

weights={"architecture":.15,"verification":.15,"drift":.15,"memory":.10,"research":.15,"api":.10,"implementation":.10,"testing":.10}
cats={}
for c in checks: cats.setdefault(c["category"],[]).append(c["score"])
score=sum((sum(v)/len(v))*weights[k] for k,v in cats.items() if k in weights)/sum(weights[k] for k in cats if k in weights)
hard=any(c["status"]=="MISSING/FAILED" and c["name"] in ("Python Compilation","Automated Tests") for c in checks)
verdict="NOT_READY" if hard or score<.60 else ("POC_PARTIAL" if score<.85 else "POC_READY")
report={"project":"WANGA-LAB","readiness_score_percent":round(score*100,2),"verdict":verdict,"checks":checks}
print(json.dumps(report,indent=2,ensure_ascii=False))
(Path(ROOT)/"POC_READINESS_REPORT.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
sys.exit(0 if verdict=="POC_READY" else 1)
