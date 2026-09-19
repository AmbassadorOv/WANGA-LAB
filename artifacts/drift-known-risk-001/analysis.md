# Forensic Analysis — drift-known-risk-001

## Finding

The synthetic fixture produces an observable decision deviation while keeping the model output unchanged.

**Model output:** unchanged (`score=0.75`, `answer_class=ACCEPT_CANDIDATE`)

**Baseline criterion:** `criterion-v1`, pass threshold `0.80` → `REJECT`

**Observed criterion:** `criterion-v2`, pass threshold `0.60` → `ACCEPT`

Therefore:

**deviation_detected = true**

**drift_type = CRITERION_DRIFT**

**model_output_changed = false**

**criterion_changed = true**

## Interpretation

Within the controlled fixture, the apparent change in system behavior is fully explained by a change in the evaluation criterion rather than a change in the model output.

This demonstrates the forensic distinction that an apparent correction or behavioral change cannot be interpreted solely from the final answer when the criterion used to evaluate the answer may itself have changed.

## Evidence chain

**Model → Answer → Evaluation → Correction / Decision → Criterion Change → Re-evaluation**

The fixture preserves both criterion versions and recomputes the resulting decisions from the same model output.

## Limitations

- This is a synthetic deterministic fixture.
- It does not establish drift in a deployed commercial model.
- It does not establish legal admissibility, regulatory status, underwriting authority, or commercial performance.
- The verification is a repository-level recheck using a separate verifier procedure; it is not an independent third-party audit.
- External timestamps and anchors remain pending because no external receipt is attached to this fixture.
