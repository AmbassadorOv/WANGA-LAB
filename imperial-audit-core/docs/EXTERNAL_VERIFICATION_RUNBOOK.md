# External Verification Runbook

## Control path
`CAPTURE → PRESERVE → CANONICALIZE → HASH → EXTERNAL TIMESTAMP → REPLICATE → PUBLIC ANCHOR → INDEPENDENT VERIFY → PASS/FAIL/UNKNOWN`

## Hard controls
- Capture time is explicit input; generator never reads the wall clock.
- Independent verifier is a separate code boundary.
- Missing external evidence cannot produce PASS.
- `UNKNOWN → STOP` for acceptance.
- Hash integrity does not establish truth of content.
- Public anchoring does not equal verification.

## Implementation boundary
GitHub stores source/history. It is not the independent trust domain. Real TSA and public-anchor evidence must be supplied externally and verified before PASS.
