# Imperial Audit Portable Evidence Pack

This directory documents the format of a self-contained evidence package.

A production package is exported outside the source repository and should contain:
- audit_output.json
- legal_contract.bin when a contract is part of the commitment
- verification_report.json
- chain-specific proof material when available

Run the verifier from the imperial-audit-core directory:

    python tools/verify_evidence_pack.py /path/to/evidence-pack

JSON output:

    python tools/verify_evidence_pack.py /path/to/evidence-pack --json

The verifier is intentionally conservative. It never upgrades an unverified blockchain claim into a verified fact merely because a TxID or block number is present.
