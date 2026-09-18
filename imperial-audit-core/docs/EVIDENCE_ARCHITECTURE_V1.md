# Evidence Architecture V1

## Objective

Build a tamper-evident historical evidence system for preserving what a source record contained, when it was committed, how it was copied, and whether later verification detects alteration.

This is an evidence-continuity architecture. It does not claim that a hash, timestamp, biometric record, blockchain anchor, or notarization proves the truth of the underlying claim.

## Non-negotiable invariants

1. Source data is preserved before transformation.
2. Canonicalization is deterministic and reproducible.
3. Every transformed artifact retains provenance to its source.
4. SHA-256 commits to exact canonical bytes.
5. External timestamp evidence is separate from local system time.
6. External anchoring is separate from the hash calculation.
7. Identity evidence is separate from asset/content truth.
8. Replication is independent of the primary storage location.
9. Verification never depends solely on the component that created the artifact.
10. UNKNOWN is a terminal verification state: UNKNOWN -> STOP.

## Evidence object

Each evidence object SHOULD contain:

- evidence_id
- source_type
- source_reference
- captured_at
- canonicalization_method
- canonical_bytes_hash
- source_metadata
- identity_attestation (optional)
- registry_reference (optional)
- timestamp_evidence
- external_anchor_evidence
- replication_manifest
- verification_history
- provenance_parent_ids

## Pipeline

SOURCE
  -> CAPTURE
  -> PRESERVE
  -> CANONICALIZE
  -> HASH
  -> EXTERNAL_TIMESTAMP
  -> REPLICATE
  -> EXTERNAL_ANCHOR
  -> VERIFY
  -> AUDIT

## Verification separation

Creator:
  produces evidence package

Independent verifier:
  receives package and recomputes hashes

External timestamp authority:
  independently attests to a timestamp token

External anchor:
  independently records an anchor commitment

Verifier must not infer truth from successful integrity verification.

## Identity and biometric records

Biometric or identity records are optional evidence components and must be minimized, encrypted, access-controlled, and retained only as required.

A biometric match establishes an identity linkage under the applicable verification method; it does not by itself establish the truth of an asset, account, registry, or transaction record.

## Failure states

- HASH_MISMATCH
- SOURCE_MISSING
- CANONICALIZATION_MISMATCH
- TIMESTAMP_UNVERIFIED
- ANCHOR_UNVERIFIED
- PROVENANCE_BROKEN
- IDENTITY_UNVERIFIED
- REPLICATION_INCOMPLETE
- UNKNOWN

Any unresolved critical verification state -> STOP.

## Current implementation boundary

The existing SHA-256 chain is an integrity mechanism.

RFC 3161 and Bitcoin/OpenTimestamps modules are currently integration boundaries and must not be represented as completed external verification until real standards-compliant evidence is produced and independently checked.

## Acceptance criteria

A release is accepted only when:

- deterministic canonicalization tests pass;
- mutation tests detect changed source bytes;
- provenance links resolve;
- independent verification reproduces every commitment;
- timestamp evidence validates independently;
- external anchor evidence validates independently;
- replication can reconstruct the package;
- UNKNOWN states stop acceptance;
- no component can mark its own unverified output as independently verified.
