# WANGA-LAB Agent Operating Contract v1

Status: ACTIVE / GOVERNANCE BASELINE
Purpose: make agent work reviewable, reproducible, and resistant to architectural drift.

## 1. Authority boundaries

| Role | May observe | May propose | May modify | May verify | May merge |
|---|---:|---:|---:|---:|---:|
| Agent | Yes | Yes | Yes, on isolated branch | Yes, by tests/evidence | No |
| Orchestrator | Yes | Yes | Only through an approved implementation path | Yes, by gate | No, unless explicitly delegated |
| Reviewer | Yes | Yes | No | Yes | No |
| Repository owner | Yes | Yes | Yes | Yes | Yes |

A proposal, model output, agent instruction, or historical artifact is not authoritative merely because it exists.

## 2. Required lifecycle

`READ -> CLAIM -> IMPLEMENT -> TEST -> VERIFY -> COMMIT -> PR -> REVIEW`

Before implementation, inspect:
- current default branch;
- target branch;
- related open PRs/issues;
- relevant historical artifacts;
- existing orchestration paths;
- applicable schemas and workflows.

Do not create a parallel implementation when an existing path already owns the same responsibility.

## 3. Evidence states

Every substantive result must be classified as one of:

- OBSERVATION — directly retrieved or measured.
- RAW_EVIDENCE — preserved source/output.
- NORMALIZED_DATA — transformed representation with documented transformation.
- DERIVED_METRIC — calculation from identified inputs.
- INFERENCE — interpretation supported by evidence.
- HYPOTHESIS — testable but unverified explanation.
- PROPOSED_CHANGE — implementation proposal.
- VERIFIED_RESULT — checked by defined validation.
- CONFLICT — incompatible evidence/design requiring review.

Temporal order, correlation, or similarity alone does not establish causation.

## 4. Historical architecture rule

Older architecture is preserved as historical evidence. When intent is unclear:

`LOCATE_ORIGINAL -> READ_ORIGINAL -> COMPARE_WITH_CURRENT -> RECOVER_INTENT -> TEST -> VERIFY`

Do not silently replace an earlier design with a newer one.

## 5. Change isolation

- Never develop directly on `main`.
- Preferred branch format: `agent/<agent-id>/<task-slug>`.
- One coherent task per branch.
- No force-push or destructive ref movement unless explicitly authorized.
- No automatic merge after implementation.
- Pull requests are the review boundary.

## 6. Verification gate

A change is not DONE merely because a commit or PR exists.

The implementation report must distinguish:
- DONE
- VERIFIED
- PENDING
- NOT DONE
- CONFLICTS
- NEXT ACTION

Verification should include, where applicable:
- syntax/tests;
- schema validation;
- deterministic behavior;
- repository state after writes;
- CI status;
- provenance of generated evidence.

## 7. Agent drift control

For each material decision record:

`RULE -> INTERPRETATION -> DECISION -> ACTION -> RESULT`

If the result contradicts the rule or expected invariant, stop and re-evaluate instead of silently adapting the rule.

## 8. Control-plane architecture

The preferred control flow is:

`OBSERVE -> ROUTE -> ANALYZE -> CRITIQUE -> VERIFY -> SYNTHESIZE -> RETURN`

The Neural Thinking Machine is a reasoning/comparison/verification layer. It does not become an unbounded authority. Proposed repairs remain proposals until the verification gate accepts them.

## 9. Provenance

Every durable research result should retain enough metadata to answer:
- What was observed?
- When?
- From which source/system?
- Under which version/configuration?
- Which code produced the result?
- What transformation produced the derived result?
- Which verification step accepted or rejected it?

Raw observations must remain distinguishable from normalized and derived data.

## 10. Security boundary

Secrets must never be treated as ordinary data or exposed through broad job-level environments when narrower step-level scope is possible.

Dynamic secret selection in workflows must be reviewed by the security gate before merge. A CodeQL secret-exposure finding is a BLOCKING finding until fixed or explicitly dispositioned by a reviewer.

Workflows that write to the repository must have the minimum required `permissions` and must not publish unverified research results as established findings.

## 11. Repository self-audit

After every GitHub mutation:
1. fetch the resulting object;
2. confirm the intended branch/ref;
3. confirm the expected file/content or PR metadata;
4. compare against the intended base;
5. record unresolved conflicts.

This contract is a governance baseline, not proof that every existing repository component already conforms to it.
