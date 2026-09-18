#!/usr/bin/env python3
"""Deterministic repository-wide WANGA work planner.

The planner incorporates open agent-system patterns at the contract level:
explicit task graphs, bounded handoffs, guardrails, checkpoint/resume metadata,
trace identifiers, and bounded evaluator loops. It does not execute arbitrary
commands, access secrets, or merge code.
"""

from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "docs" / "WORK_MEMORY_STATE.json"
OUT = ROOT / "docs" / "GLOBAL_WORK_PLAN.json"

SUBSYSTEMS = [
    ("WANGA-OS", "ARCHITECTURE", "Maintain OS architecture and boot/runtime contracts."),
    ("RESEARCH-GROUPS", "RESEARCH", "Coordinate specialized research-group work."),
    ("MODEL-FABRIC", "MODEL_DISCOVERY", "Discover, classify and bind verified model candidates."),
    ("DIGITAL-MODEL-AGENTS", "MODEL_BINDING", "Maintain deterministic model-agent identities and roles."),
    ("RUNTIME", "RUNTIME", "Coordinate provider-neutral runtime and adapter work."),
    ("DRIFT-FORENSICS", "DRIFT_FORENSICS", "Collect, compare and verify drift evidence."),
    ("EVIDENCE", "EVIDENCE", "Maintain provenance and evidence integrity."),
    ("NTM", "NTM_ESCALATION", "Route verified high-level reasoning and conflicts to NTM."),
    ("GOVERNANCE", "GOVERNANCE_INTERFACE", "Maintain explicit WANGA/GAG interface boundaries."),
    ("WIX", "PUBLICATION", "Prepare validated publication/integration work."),
    ("AUTOBUILD", "AUTOBUILD", "Continue deterministic architecture construction."),
    ("WORK-MEMORY", "MAINTENANCE", "Checkpoint current state and next actions."),
]

GUARDRAILS = [
    "no_secrets",
    "no_unverified_model_execution",
    "no_direct_main_changes",
    "no_invented_endpoints_or_capabilities",
    "no_evidence_free_promotion",
    "no_policy_boundary_bypass",
]

def load_state() -> dict:
    return json.loads(STATE.read_text(encoding="utf-8"))

def build_plan(state: dict) -> dict:
    tasks = []
    for i, (name, cls, objective) in enumerate(SUBSYSTEMS, 1):
        task_id = f"WGM-{i:02d}-{name}"
        tasks.append({
            "task_id": task_id,
            "task_class": cls,
            "objective": objective,
            "owner": "GLOBAL_WORK_MANAGER",
            "dependencies": [],
            "inputs": ["docs/WORK_MEMORY_STATE.json"],
            "expected_artifacts": [],
            "status": "READY",
            "evidence_policy": "REQUIRED",
            "verification_required": True,
            "risk_level": "MEDIUM",
            "provenance": ["docs/WORK_MEMORY_STATE.json"],
            "execution": {
                "run_id": f"run-{task_id.lower()}",
                "state_model": "GRAPH_STATE_V1",
                "checkpoint_policy": "BEFORE_AND_AFTER_SIDE_EFFECT",
                "resume_policy": "RESUME_FROM_LAST_VERIFIED_CHECKPOINT",
                "idempotency_required": True,
                "trace_required": True,
                "guardrails": GUARDRAILS,
                "handoff_policy": "BOUNDED_CAPABILITY_HANDOFF",
                "max_handoffs": 3,
                "evaluation_loop": {
                    "enabled": True,
                    "pattern": "PRODUCE_EVALUATE_REVISE_VERIFY",
                    "max_iterations": 3,
                    "acceptance_criteria_locked": True,
                },
            },
        })

    by_id = {t["task_id"]: t for t in tasks}
    by_id["WGM-03-MODEL-FABRIC"]["dependencies"] = ["WGM-01-WANGA-OS"]
    by_id["WGM-04-DIGITAL-MODEL-AGENTS"]["dependencies"] = ["WGM-03-MODEL-FABRIC"]
    by_id["WGM-05-RUNTIME"]["dependencies"] = ["WGM-01-WANGA-OS"]
    by_id["WGM-06-DRIFT-FORENSICS"]["dependencies"] = ["WGM-07-EVIDENCE"]
    by_id["WGM-08-NTM"]["dependencies"] = ["WGM-07-EVIDENCE", "WGM-04-DIGITAL-MODEL-AGENTS"]
    by_id["WGM-10-WIX"]["dependencies"] = ["WGM-07-EVIDENCE"]
    by_id["WGM-11-AUTOBUILD"]["dependencies"] = ["WGM-01-WANGA-OS", "WGM-07-EVIDENCE"]
    by_id["WGM-12-WORK-MEMORY"]["dependencies"] = ["WGM-07-EVIDENCE"]

    return {
        "version": 2,
        "manager": "WANGA_GLOBAL_WORK_MANAGER_V2",
        "mode": "deterministic-plan",
        "pattern_profile": "EXTERNAL_AGENT_PATTERN_INTEGRATION_V1",
        "repository": state.get("repository", "AmbassadorOv/WANGA-LAB"),
        "build_branch": state.get("build_branch"),
        "main_branch": state.get("main_branch"),
        "review_policy": state.get("review_policy"),
        "task_count": len(tasks),
        "graph_policy": {
            "explicit_dependencies": True,
            "bounded_loops": True,
            "checkpoint_resume": True,
            "human_review_state": "REVIEW_REQUIRED",
            "verification_is_promotion_gate": True,
        },
        "tasks": tasks,
        "invariants": [
            "no_direct_main_changes",
            "preserve_source_branches",
            "no_secrets_in_registry",
            "no_invented_endpoints_or_capabilities",
            "no_duplicate_global_orchestrator",
            "verification_before_enablement",
            "final_review_separate",
        ],
    }

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default=str(OUT))
    args = parser.parse_args()
    plan = build_plan(load_state())
    Path(args.output).write_text(
        json.dumps(plan, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "status": "PLANNED",
        "manager": plan["manager"],
        "task_count": plan["task_count"],
        "pattern_profile": plan["pattern_profile"],
        "main_changes": False,
    }, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
