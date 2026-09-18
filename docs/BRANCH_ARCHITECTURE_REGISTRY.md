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
