#!/usr/bin/env python3
"""Deterministic significance gate for the WANGA -> ChatGPT bridge.

This script does not contact ChatGPT and never writes persistent ChatGPT memory.
It emits a bridge event only when selected repository control-plane dimensions
change materially since the previous checkpoint.
"""

from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "docs" / "WORK_MEMORY_STATE.json"
CHECKPOINT = ROOT / "docs" / "CHATGPT_BRIDGE_STATE.json"
EVENT = ROOT / "docs" / "CHATGPT_BRIDGE_EVENT.json"

FOUNDATIONAL_KEYS = (
    "architecture", "model_fabric", "autonomy", "wix", "source_history_policy"
)

def load(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))

def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))

def digest(value):
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()

def snapshot(state: dict) -> dict:
    return {k: state.get(k) for k in FOUNDATIONAL_KEYS}

def classify(old: dict | None, new: dict) -> tuple[str | None, list[str]]:
    if old is None:
        return "S2", ["initial_bridge_baseline"]

    changed = []
    for key in FOUNDATIONAL_KEYS:
        if old.get(key) != new.get(key):
            changed.append(key)

    old_f = old.get("model_fabric", {})
    new_f = new.get("model_fabric", {})
    for key in ("connected_slots", "verified_slots"):
        if old_f.get(key) != new_f.get(key):
            changed.append(f"model_fabric.{key}")

    old_v = old.get("verified_limits", {})
    new_v = new.get("verified_limits", {})
    for key in ("persistent_autonomous_loop", "global_work_manager_runtime",
                "provider_discovery", "capability_probe", "adapter_runtime",
                "ntm_runtime_binding"):
        if old_v.get(key) != new_v.get(key):
            changed.append(f"verified_limits.{key}")

    if not changed:
        return None, []

    foundational = any(x in changed for x in ("architecture", "autonomy", "source_history_policy"))
    return ("S3" if foundational else "S1"), sorted(set(changed))

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", default=str(STATE))
    parser.add_argument("--checkpoint", default=str(CHECKPOINT))
    parser.add_argument("--event", default=str(EVENT))
    args = parser.parse_args()

    state = load(Path(args.state), {})
    current = snapshot(state)
    previous = load(Path(args.checkpoint), None)
    significance, changed = classify(previous, current)

    # Always checkpoint the observed state; event emission is conditional.
    Path(args.checkpoint).write_text(
        json.dumps(current, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    if significance is None:
        print(json.dumps({"status":"NO_SIGNIFICANT_CHANGE","emit":False}, ensure_ascii=False))
        return 0

    memory_proposal = significance == "S3"
    verification = "VERIFIED"
    if state.get("verified_limits", {}).get("global_work_manager_runtime") == "workflow execution pending":
        verification = "PENDING"

    event_id = "wanga-" + digest({"snapshot": current, "changed": changed})[:16]
    event = {
        "version": 1,
        "event_id": event_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "significance": significance,
        "summary": "Significant WANGA control-plane state change detected.",
        "changed_dimensions": changed,
        "evidence_refs": [
            "docs/WORK_MEMORY_STATE.json",
            "docs/WANGA_GLOBAL_WORK_MANAGER_V2.md",
            "docs/WORK_MEMORY_PROTOCOL_V1.md"
        ],
        "verification_status": verification,
        "memory_proposal": memory_proposal,
        "memory_reason": (
            "Foundational working assumptions changed; propose persistent-memory review."
            if memory_proposal else
            "Operational/architectural update only; do not write persistent memory automatically."
        ),
        "recommended_next_action": (
            "Inspect bridge event and repository evidence; continue through Global Work Manager."
        )
    }
    Path(args.event).write_text(json.dumps(event, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status":"EMITTED","emit":True,"significance":significance,"event_id":event_id,"memory_proposal":memory_proposal}, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
