# Imperial Evidence Record (IER) — Format v1.0

## Purpose

IER is the platform-neutral archival/exchange format for Imperial Audit.

It is independent of GitHub, a vendor database, a web application, or a
particular storage provider. A package is a directory of ordinary files that
can be copied to removable media, another computer, or another archive.

The design follows established digital-preservation principles: explicit
format documentation, fixity information, provenance, and self-contained
packaging. PREMIS is a preservation-metadata standard, while BagIt is an
established packaging format for arbitrary digital content.

## Package layout

    evidence-record/
      audit_output.json
      manifest.json
      verification_report.json
      legal_contract.bin
      chain-proof/
      source/
      metadata/
      verifier/

legal_contract.bin, chain-proof, source, metadata and verifier are optional.

## Required properties

1. audit_output.json contains the canonical audit record.
2. manifest.json contains SHA-256 fixity for every package file except itself.
3. The manifest records the package format version and master_hash.
4. Paths are relative POSIX paths; no absolute filesystem paths are required.
5. JSON is UTF-8.
6. The package does not require GitHub, a cloud service, or the original
   application to verify its internal cryptographic relationships.

## Meaning

The manifest proves file integrity relative to the recorded hashes. It does
not prove that financial assertions contained in those files are true.

The master_hash connects the package to the audit chain. A blockchain anchor,
when present and independently verified, provides an external cryptographic
commitment to that hash. It is not the package itself.

## Preservation model

IER separates:

- content — what was recorded;
- provenance — where, when and how it was produced;
- fixity — whether bytes changed;
- external anchors — independent commitments;
- verification — what can be established using only the package.

PREMIS models preservation information around objects, events, agents and
rights, including provenance and fixity.

## Survival property

The critical rule is:

**GitHub is not part of the evidence format.**

GitHub may be a publication/development location. If it disappears, an IER
package remains structurally meaningful because its specification, files,
hashes and verification rules travel with the evidence.

A blockchain is an external anchor, not the storage format. Independent copies
remain necessary for preserving the actual evidence bytes.

## Verification states

VERIFIED — all required internal checks passed.
PARTIAL — internal checks passed but optional external proofs are unavailable.
FAIL — an integrity relationship failed.
INVALID_PACKAGE — required structure is absent or malformed.

These are technical verification states, not legal judgments.
