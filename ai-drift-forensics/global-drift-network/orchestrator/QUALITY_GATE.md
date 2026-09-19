# Quality Gate

The Quality Gate is a hard barrier between analysis and publication.

## Required checks

1. Run record is complete.
2. Input snapshot exists and is immutable.
3. Worker results are present for all required tasks.
4. Evidence IDs resolve to registry records.
5. Claims are classified as OBSERVED, SUPPORTED, HYPOTHESIS, or REFUTED.
6. No unsupported claim is promoted to an observed finding.
7. Provenance and integrity metadata are present.
8. Verification status is explicit.
9. Publication output contains limitations and unresolved items.

## Decisions

- `PASS`: all mandatory checks succeed.
- `REVIEW`: evidence or verification is incomplete; publication remains blocked.
- `BLOCK`: integrity, provenance, schema, or policy requirements fail.

The Publication Worker cannot override this decision.
