# Imperial Audit Core

Deterministic audit/evidence package for financial exposure analysis.

## Evidence chain

1. Canonical audit JSON
2. SHA-256 hashes for S1 Exposure, S2 Screw, S3 Recovery
3. MASTER_CHAIN_HASH
4. External RFC 3161 timestamp token (TSA)
5. Bitcoin/OpenTimestamps anchoring proof
6. Legal agreement hash binding
7. Notary submission package

## Repository layout

- `src/core/audit_generator.py` — financial audit JSON generation
- `src/crypto/sha256_chain.py` — S1/S2/S3/Master chain
- `src/crypto/rfc3161_timestamp.py` — RFC 3161 timestamp integration
- `src/crypto/bitcoin_anchor.py` — OpenTimestamps/Bitcoin anchoring interface
- `src/legal/contract_binder.py` — binds contract hash to audit artifact
- `src/output/json_builder.py` — canonical JSON construction
- `docs/LEGAL_AGREEMENT.md` — advisory/due-diligence agreement template
- `docs/NOTARY_SUBMISSION_FORM.md` — notary submission checklist
- `.github/workflows/verification-ci.yml` — automated verification

## Verification rule

A local SHA-256 proves integrity relative to the hashed bytes; it does not independently prove creation time, authorship, truth of the underlying claims, or legal enforceability.

The verification chain is:

**Execution → Independent Verification → PASS / FAIL / UNKNOWN**

**UNKNOWN → STOP**

External timestamping, anchoring, contracts and notarization are evidence/control layers; they do not by themselves establish that the financial content is true or that a service is legally classified as insurance.

## Status

Implementation must be tested against independent verification before any production/legal claim is made.
