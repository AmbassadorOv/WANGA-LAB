# drift-known-risk-001

## Evidence Status

**Current state: VERIFIED**

This is a controlled synthetic AI-drift forensic case package.

It demonstrates a reproducible **criterion-drift** finding while holding the model output constant.

## Case identity

- Case reference: `CASE_REF_2026_DRIFT_KNOWN_RISK_001`
- Fixture type: SYNTHETIC
- Subject: controlled criterion-drift forensic evaluation
- Client: none
- Verification scope: repository-level independent recheck
- External timestamp: PENDING
- External anchor: PENDING

## Finding

The same synthetic model output is evaluated against two preserved criteria:

**Baseline:** `criterion-v1`, threshold `0.80` → `REJECT`

**Observed:** `criterion-v2`, threshold `0.60` → `ACCEPT`

The model output remains unchanged:

- score: `0.75`
- answer class: `ACCEPT_CANDIDATE`

Therefore the replay establishes:

- `deviation_detected = true`
- `drift_type = CRITERION_DRIFT`
- `model_output_changed = false`
- `criterion_changed = true`

## Evidence package

- `case.yaml` — case scope and status
- `replay/inputs.json` — frozen synthetic replay input
- `evidence-manifest.json` — SHA-256 inventory of the evidence package
- `outputs/replay-result.json` — deterministic replay result
- `analysis.md` — forensic interpretation and limitations
- `verification/CHECKLIST.md` — verification gates
- `verification/verification-result.json` — repository-level independent recheck
- `tools/replay_known_risk.py` — deterministic replay procedure
- `tools/verify_known_risk.py` — separate verification procedure

## Verification rule

**VERIFIED** means the defined synthetic replay and repository integrity gates passed.

It does **not** mean:

- third-party audit;
- legal admissibility;
- regulatory certification;
- insurance underwriting authority;
- commercial performance validation;
- a completed client engagement.

External timestamping and anchoring remain **PENDING** because no external proof is part of this fixture.

## Research significance

The fixture isolates one important forensic question:

> Can an apparent behavioral change be explained by a change in the evaluation criterion rather than by a change in the model output?

Within this controlled case, the answer is yes.

The result supports the broader research distinction between **point error** and **criterion drift** and motivates preservation of evaluation criteria alongside model outputs.

## Limitations

This is a deterministic synthetic fixture. It demonstrates the evidence and replay procedure, not drift in a deployed production model.
