# WANGA-LAB Branch & Architecture Registry

Status: proposed operational registry

## Canonical ownership map

| Architecture | Canonical repository area | Branch/PR candidates | Status |
|---|---|---|---|
| Control Plane / Agent Governance | `.github/`, `docs/` | `agent/codex-002/control-plane-governance-hardening`, `agent/codex-002/repository-hygiene-ci` | Active |
| Global Algorithmic Governance | `ai-drift-forensics/global-algorithmic-governance-institute/` | `codex/algorithmic-governance-standard-v0-1` | Active |
| Global Drift Network / Evidence | `ai-drift-forensics/global-drift-network/` | `whitepaper-evidence-infrastructure`, PR #9 | Security review required |
| Epistemic Frontier | repository root implementation | `feature/epistemic-frontier-baseline` | Candidate |
| ARK / SL compiler-runtime | repository root / WANGA implementation | `feat/ark-sl-compiler-runtime-binding-6185253793362141196` | Candidate |
| Autonomous knowledge connector | WANGA implementation | `jules-16755109129419681351-0b3755ec` | Candidate |
| Virtual GPU / nano fabric | WANGA implementation | `jules-2742570839290368558-84513077` | Candidate |
| Hello/connection tests | historical test artifacts | PR #1 / PR #2 | Superseded candidates |
| Distributed evidence branch family | historical/duplicate family | 20 branches at one identical SHA | Requires cleanup audit |

## Rules

1. `main` is the integration base, not a development workspace.
2. Each architecture gets one canonical implementation path.
3. A branch is not an architecture; the branch carries a change toward an existing responsibility.
4. Historical branches remain evidence until classified.
5. Duplicate branches are not merged merely because they exist.
6. WANGA-LAB and Global Algorithmic Governance remain distinct responsibilities connected by explicit interfaces.
7. Wix/site delivery is treated as an external publication/integration surface, not as a second GitHub orchestration plane.

## Next classification pass

Classify every non-main branch as ACTIVE, HISTORICAL, DUPLICATE, SUPERSEDED, or UNKNOWN before destructive branch deletion.


## Complete current branch inventory

| Branch | Disposition | Architecture / reason |
|---|---|---|
| `agent/codex-002/control-plane-governance-hardening` | ACTIVE | Control-plane governance; PR #12 |
| `agent/codex-002/control-plane-mvp` | HISTORICAL-CANDIDATE | Earlier control-plane implementation; stale relative to main, inspect before reuse |
| `agent/codex-002/repository-hygiene-ci` | ACTIVE | Repository governance/CI repair; PR #13 |
| `codex/algorithmic-governance-standard-v0-1` | ACTIVE | Global Algorithmic Governance standard; PR #11 |
| `whitepaper-evidence-infrastructure` | ACTIVE-BLOCKED | Global Drift Network / evidence; PR #9 has security findings |
| `feature/global-drift-whitepaper-pipeline` | CANDIDATE | Global Drift publication/evidence pipeline |
| `feature/epistemic-frontier-baseline` | CANDIDATE | Epistemic Frontier |
| `feat/ark-sl-compiler-runtime-binding-6185253793362141196` | CANDIDATE | ARK / SL compiler-runtime |
| `jules-16755109129419681351-0b3755ec` | CANDIDATE | Autonomous knowledge connector |
| `jules-2742570839290368558-84513077` | CANDIDATE | Virtual GPU / nano processor fabric |
| `jules-93324678969383236-63b1c010` | UNKNOWN | Requires content audit |
| `jules-14645773145571184025-42db8e24` | SUPERSEDED | PR #1 closed; duplicate hello test |
| `jules-11016927793168577821-b6767505` | SUPERSEDED | PR #2 closed; duplicate hello test |
| `distributed-evidence-network` | DUPLICATE-FAMILY | Same SHA as 19 other distributed-evidence branches; audit before deletion |
| `distributed-evidence-network-2` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-3` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-4` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-5` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-6` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-active` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-dev` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-final` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-impl` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-live` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-main` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-ready` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-v2` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-v3` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-v4` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-v5` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-work` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `distributed-evidence-network-x` | DUPLICATE-FAMILY | Same SHA; audit before deletion |
| `tmp-check` | DUPLICATE-FAMILY | Same SHA; temporary branch, audit before deletion |
