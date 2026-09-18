# WANGA Global Manager Team V1

This registry defines the manager layer supervised by WANGA Global Work Manager V2. It is a repository-level architectural team, not a claim that GitHub has created an organization/team object or that these roles are human appointments.

## Hierarchy

GLOBAL WORK MANAGER
|
+-- OS / Runtime Manager
+-- Research Manager
+-- Model Fabric Manager
+-- Digital Model Agent Manager
+-- Runtime Adapter Manager
+-- Drift Forensics Manager
+-- Evidence & Provenance Manager
+-- NTM / Cognitive Routing Manager
+-- Governance Interface Manager
+-- Publication / Wix Manager
+-- Autonomous Build Manager
+-- Work Memory Manager

The Global Work Manager is the single cross-system coordinator.

## Manager roster

| ID | Manager | Scope | Primary daily question |
|---|---|---|---|
| MGR-OS | OS / Runtime Manager | WANGA OS, boot, runtime contracts | What is blocking or degrading the core runtime? |
| MGR-RESEARCH | Research Manager | Research groups and research queues | What evidence-backed research should move next? |
| MGR-MODEL | Model Fabric Manager | 5,000 model slots, discovery, binding | Which model capabilities changed or need verification? |
| MGR-DMA | Digital Model Agent Manager | DMA identities, roles, lifecycle | Which agents need role/configuration/health work? |
| MGR-ADAPTER | Runtime Adapter Manager | provider/runtime adapters | Which adapters are missing, failing, or drifting? |
| MGR-DRIFT | Drift Forensics Manager | drift probes, comparisons, findings | What new drift evidence exists? |
| MGR-EVIDENCE | Evidence & Provenance Manager | provenance and evidence envelopes | Which claims lack sufficient evidence or verification? |
| MGR-NTM | NTM / Cognitive Routing Manager | NTM intake, escalation, reasoning status | What requires NTM escalation or conflict resolution? |
| MGR-GOV | Governance Interface Manager | WANGA/GAG interface | Are governance interfaces consistent and evidence-bounded? |
| MGR-WIX | Publication / Wix Manager | publication and external integration | What validated material is ready for publication? |
| MGR-AUTOBUILD | Autonomous Build Manager | autonomous construction branch | What verified change can safely be built next? |
| MGR-MEMORY | Work Memory Manager | durable work memory | What must be checkpointed so work can resume correctly? |

## Reporting contract

Each manager reports:
STATUS -> NEW_EVIDENCE -> METRICS -> DRIFT/CHANGE -> REQUIRED_WORK -> PROPOSED_ACTION -> TESTS -> VERIFIED -> BLOCKED/CONFLICT -> NEXT_ACTION

No manager may silently promote a proposal to a verified result.

## Daily assignment rule

The Global Work Manager compares manager reports with Work Memory, Global Work Plan, repository state, open PRs, CI results, model verification state, evidence/drift records, and validated external research. It then creates the next bounded work queue.

## Independence boundaries

Managers own bounded domains only. They do not create competing global queues, bypass verification, change main, delete preserved branches, store secrets, or invent external model/provider facts.

## Final review

Manager recommendations and autonomous changes remain subject to repository review. Final review is not delegated to the manager team.
