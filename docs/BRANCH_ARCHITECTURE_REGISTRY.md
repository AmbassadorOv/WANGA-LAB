# WANGA-LAB Branch & Architecture Registry

Status: active reconciliation registry — 2026-09-18

## Canonical architecture map

| Architecture | Repository area | Canonical branch path | Existing source branch(es) |
|---|---|---|---|
| Control Plane / Agent Governance | `.github/`, `docs/` | `agent/codex-002/control-plane/* ` | `agent/codex-002/control-plane-governance-hardening`, `agent/codex-002/repository-hygiene-ci` |
| Global Algorithmic Governance | `ai-drift-forensics/global-algorithmic-governance-institute/` | `governance/algorithmic-governance/standard-v0-1` | `codex/algorithmic-governance-standard-v0-1` |
| Global Drift Network / Evidence | `ai-drift-forensics/global-drift-network/` | `drift/global-network/evidence-infrastructure` | `whitepaper-evidence-infrastructure`, distributed-evidence family |
| Global Drift Network Security | `.github/workflows/regional-drift-agents.yml` | `drift/global-network/secret-hardening` | `agent/codex-002/drift-network-secret-hardening` |
| Drift Whitepaper Pipeline | `ai-drift-forensics/global-drift-network/whitepaper-prep/` | `drift/global-network/whitepaper-pipeline` | `feature/global-drift-whitepaper-pipeline` |
| Epistemic Frontier | root implementation | `research/epistemic-frontier/baseline` | `feature/epistemic-frontier-baseline` |
| ARK / SL compiler-runtime | WANGA root implementation | `runtime/ark-sl/compiler-runtime-binding` | `feat/ark-sl-compiler-runtime-binding-6185253793362141196` |
| Autonomous knowledge connector | WANGA runtime | `runtime/ark/autonomous-knowledge-connector` | `jules-16755109129419681351-0b3755ec` |
| Virtual GPU / nano fabric | WANGA runtime | `runtime/nano/virtual-gpu-fabric` | `jules-2742570839290368558-84513077` |
| Historical / unresolved | historical evidence | `legacy/*` | stale, superseded, unknown, and temporary branches |

## Branch reconciliation policy

1. `main` remains the integration base.
2. Branches are organized by responsibility; a branch is not itself an architecture.
3. Existing branches are preserved. This pass does **not** delete or disable branches.
4. Where GitHub connector capabilities do not expose an in-place branch rename, a canonical architecture-aligned branch is created from the exact existing branch head; the original branch remains intact as a historical/source reference.
5. No branch is merged merely because it has been aligned.
6. Historical work remains evidence until reviewed.
7. WANGA-LAB and the Global Algorithmic Governance Institute remain distinct responsibilities connected through explicit interfaces.
8. Wix remains a publication/integration surface, not a second GitHub orchestration plane.

## Canonical aligned branches created in this pass

| New aligned branch | Source branch | Purpose |
|---|---|---|
| `agent/codex-002/control-plane/governance-hardening` | `agent/codex-002/control-plane-governance-hardening` | control-plane governance |
| `agent/codex-002/control-plane/repository-hygiene-ci` | `agent/codex-002/repository-hygiene-ci` | CI/repository hygiene |
| `governance/algorithmic-governance/standard-v0-1` | `codex/algorithmic-governance-standard-v0-1` | governance standard |
| `drift/global-network/evidence-infrastructure` | `whitepaper-evidence-infrastructure` | global drift evidence |
| `drift/global-network/secret-hardening` | `agent/codex-002/drift-network-secret-hardening` | regional secret isolation |
| `drift/global-network/whitepaper-pipeline` | `feature/global-drift-whitepaper-pipeline` | publication pipeline |
| `drift/global-network/distributed-evidence` | `distributed-evidence-network` | canonical representative of duplicate family |
| `research/epistemic-frontier/baseline` | `feature/epistemic-frontier-baseline` | epistemic frontier |
| `runtime/ark-sl/compiler-runtime-binding` | `feat/ark-sl-compiler-runtime-binding-6185253793362141196` | ARK-SL runtime |
| `runtime/ark/autonomous-knowledge-connector` | `jules-16755109129419681351-0b3755ec` | knowledge connector |
| `runtime/nano/virtual-gpu-fabric` | `jules-2742570839290368558-84513077` | nano/virtual GPU |
| `legacy/stale/control-plane-mvp` | `agent/codex-002/control-plane-mvp` | preserved stale branch |
| `legacy/unclassified/jules-93324678969383236-63b1c010` | `jules-93324678969383236-63b1c010` | preserved unknown branch |
| `legacy/superseded/jules-11016927793168577821-b6767505` | `jules-11016927793168577821-b6767505` | preserved historical hello test |
| `legacy/superseded/jules-14645773145571184025-42db8e24` | `jules-14645773145571184025-42db8e24` | preserved historical hello test |
| `legacy/audit/distributed-evidence-tmp-check` | `tmp-check` | preserved temporary audit branch |

## Complete branch inventory

### Control / governance
- `agent/codex-002/control-plane-governance-hardening` → ACTIVE; PR #12.
- `agent/codex-002/control-plane/repository-hygiene-ci` → ALIGNED; source has PR #13.
- `agent/codex-002/repository-hygiene-ci` → ACTIVE source; PR #13.
- `agent/codex-002/control-plane-mvp` → STALE/HISTORICAL; 143 commits behind `main`.

### Governance
- `codex/algorithmic-governance-standard-v0-1` → ACTIVE; PR #11.
- `governance/algorithmic-governance/standard-v0-1` → ALIGNED canonical branch.

### Drift / evidence
- `whitepaper-evidence-infrastructure` → ACTIVE-BLOCKED; PR #9; security remediation separated into PR #14.
- `agent/codex-002/drift-network-secret-hardening` → ACTIVE SECURITY; PR #14.
- `drift/global-network/evidence-infrastructure` → ALIGNED canonical branch.
- `drift/global-network/secret-hardening` → ALIGNED security branch.
- `feature/global-drift-whitepaper-pipeline` → CANDIDATE/ALIGNED.
- `drift/global-network/whitepaper-pipeline` → ALIGNED.
- `distributed-evidence-network` and `distributed-evidence-network-{2,3,4,5,6,active,dev,final,impl,live,main,ready,v2,v3,v4,v5,work,x}` → DUPLICATE-FAMILY; same 33-commit architecture payload and same historical merge base; preserved, not deleted.
- `tmp-check` → DUPLICATE-FAMILY/AUDIT; preserved.
- `drift/global-network/distributed-evidence` → ALIGNED representative.

### Research / runtime
- `feature/epistemic-frontier-baseline` → CANDIDATE; 4 commits ahead of its historical merge base.
- `research/epistemic-frontier/baseline` → ALIGNED.
- `feat/ark-sl-compiler-runtime-binding-6185253793362141196` → CANDIDATE; PR #5.
- `runtime/ark-sl/compiler-runtime-binding` → ALIGNED.
- `jules-16755109129419681351-0b3755ec` → CANDIDATE; PR #6.
- `runtime/ark/autonomous-knowledge-connector` → ALIGNED.
- `jules-2742570839290368558-84513077` → CANDIDATE; PR #3.
- `runtime/nano/virtual-gpu-fabric` → ALIGNED.
- `jules-93324678969383236-63b1c010` → UNKNOWN; preserved under legacy mapping.
- `legacy/unclassified/jules-93324678969383236-63b1c010` → ALIGNED legacy reference.

### Historical
- `jules-11016927793168577821-b6767505` → SUPERSEDED; PR #2 previously closed.
- `jules-14645773145571184025-42db8e24` → SUPERSEDED; PR #1 previously closed.
- Corresponding `legacy/superseded/*` aligned branches preserve their exact heads.

## Current open PR relationships

| PR | Branch | Role | State |
|---|---|---|---|
| #14 | `agent/codex-002/drift-network-secret-hardening` | regional secret isolation | Draft/Open |
| #13 | `agent/codex-002/repository-hygiene-ci` | repository integrity baseline | Draft/Open |
| #12 | `agent/codex-002/control-plane-governance-hardening` | agent/control-plane governance | Draft/Open |
| #11 | `codex/algorithmic-governance-standard-v0-1` | governance standard seed | Draft/Open |
| #9 | `whitepaper-evidence-infrastructure` | global drift network | Draft/Open; security review required |
| #6 | `jules-16755109129419681351-0b3755ec` | autonomous knowledge connector | Draft/Open; non-mergeable |
| #5 | `feat/ark-sl-compiler-runtime-binding-6185253793362141196` | ARK-SL compiler/runtime | Draft/Open; non-mergeable |
| #3 | `jules-2742570839290368558-84513077` | virtual GPU/nano fabric | Draft/Open; non-mergeable |

## Verification note

The branch comparisons were performed against `main`. The large distributed-evidence family resolves to the same historical 33-commit payload and is therefore treated as a single architecture family for mapping purposes, while each original branch remains preserved.

No branch deletion, branch disabling, or merge was performed in this reconciliation pass.
