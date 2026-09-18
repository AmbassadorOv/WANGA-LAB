# Control-Plane Audit — 2026-09-18

## Scope

Repository: WANGA-LAB
Base reviewed: `main`
Existing control-plane branch: `agent/codex-002/control-plane-mvp`
Review focus: agent operating discipline, authority boundaries, provenance, verification, branch isolation, and workflow security.

## Verified observations

1. The repository separates Research, Implementation, and Integration in its README.
2. The Neural Thinking Machine architecture explicitly separates observation, reasoning, proposed repair, and verification.
3. The research asset registry preserves historical artifacts and defines an intent-recovery workflow.
4. The existing control-plane branch is stale relative to `main`: the GitHub comparison reports 0 commits ahead and 143 commits behind. Its README path is not present at the branch tip through the file API.
5. There are multiple open draft PRs. This increases the need for explicit ownership and duplication checks before further implementation.
6. PR #9 has two unresolved CodeQL comments reporting excessive secrets exposure from dynamic matrix-based secret references in `.github/workflows/regional-drift-agents.yml`.
7. The repository workflow `.github/workflows/brain-network.yml` currently runs on pushes to `main` and has access to multiple provider API secrets. This is an architectural/security surface that should be reviewed before expanding automation.

## Interpretation

The architecture contains many of the desired governance ideas already, but they are distributed across README files, schemas, workflows, PR descriptions, and historical branches. The primary remaining improvement is to make the operating contract explicit and repository-visible so agents apply one consistent protocol.

## Implemented in this branch

- Added `.github/WANGA_AGENT_OPERATING_CONTRACT_V1.md`.
- Added this audit record.
- Established explicit authority, evidence, historical-recovery, branch-isolation, verification, provenance, security, and post-mutation self-audit rules.

## Not changed

- `main` was not modified.
- No existing PR was merged, closed, or rewritten.
- PR #9 workflow secrets were not changed from this branch because that fix belongs to the PR's implementation branch and requires targeted testing.
- The stale `agent/codex-002/control-plane-mvp` branch was not force-updated.

## Next controlled actions

1. Review and merge this governance contract if accepted.
2. Remediate PR #9's CodeQL secret-exposure findings on its own branch.
3. Audit the main-triggered Brain Network workflow for least-privilege permissions and execution boundaries.
4. Reconcile or archive stale/duplicate control-plane branches and PRs without deleting historical evidence.
5. Add executable CI checks for the contract where practical.

## Status

Governance hardening: IMPLEMENTED
Repository-wide conformity: NOT YET VERIFIED
Security remediation for PR #9: PENDING
Main workflow hardening: PENDING
