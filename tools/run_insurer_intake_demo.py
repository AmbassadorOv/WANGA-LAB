"""Run the public synthetic ten-prospect intake scenario."""
from __future__ import annotations
import json
from pathlib import Path
from tools.insurer_intake import load_records

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "artifacts" / "insurer-intake-demo" / "intake.json"

def main() -> None:
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    result = load_records(data["records"], int(data["active_limit"]))
    print(json.dumps({"scenario":data["scenario"],"active_limit":data["active_limit"],"results":result},indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
