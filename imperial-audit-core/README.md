# Imperial Audit Core

Deterministic audit/evidence package for financial exposure analysis.

## Control chain
`CAPTURE → PRESERVE → CANONICALIZE → SHA-256 → EXTERNAL TIMESTAMP → REPLICATE → PUBLIC ANCHOR → INDEPENDENT VERIFY → PASS/FAIL/UNKNOWN`

## Hard boundary
The generator, independent verifier, timestamp adapter, and public-anchor adapter are separate trust boundaries. No local clock, hash, HTTP response, or pending submission is represented as external proof.

## Verification rule
A SHA-256 hash establishes integrity of the exact hashed representation. It does not establish truth, authorship, legal title, solvency, or insurance classification.

`Execution → Independent Verification → PASS / FAIL / UNKNOWN`

`UNKNOWN → STOP`

## Current implementation status
- Deterministic generation with explicit capture timestamp: implemented.
- Independent integrity verifier and PASS/FAIL/UNKNOWN gate: implemented.
- Mutation/failure tests: implemented.
- RFC 3161: integration boundary; missing/unparsed token remains UNKNOWN.
- OpenTimestamps/Bitcoin: integration boundary; missing/unverified proof remains UNKNOWN.
- GitHub: source/history store, not the independent trust domain.

No external timestamp or anchor is claimed as verified until real external evidence is supplied and independently validated.
