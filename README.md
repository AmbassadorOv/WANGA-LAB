# WANGA-LAB — Imperial Audit Evidence Layer

This repository contains the Imperial Audit evidence-integrity layer. The evidence layer records exactly which inputs produced an evidence package and whether the package can be reproduced.

## Service scope

WANGA-LAB / Drift Forensics is intended to provide independent technical evidence, AI-drift analysis, model-behavior analysis, provenance reconstruction, and systemic-exposure assessment to insurance companies and institutional risk holders with material exposure to banks and other critical financial infrastructure.

The service is an evidence and forensic-analysis layer. It does not itself provide insurance coverage, underwriting, a financial guarantee, solvency assurance, or a regulated insurance product. Commercial and regulatory classification must be reviewed for the applicable jurisdiction before customer use.

## Components

- deterministic S1/S2/S3 + MASTER SHA-256 chain
- canonical JSON output
- contract SHA-256 binding
- RFC 3161 timestamp adapter using OpenSSL
- OpenTimestamps/Bitcoin anchor manifest
- integrity tests proving that changed input invalidates the chain
- GitHub Actions verification on push and pull request
- Israeli legal-review and notary submission templates

## Legal status

Software cannot make a commercial product legally proven by itself. Hashes, timestamps, blockchain anchors, electronic signatures and notarization address different evidentiary questions. Contract enforceability, regulatory classification, arbitration, payment/refund terms and financial representations require transaction-specific legal review.

The Israeli Electronic Signature Law recognizes qualifying electronic signatures and provides statutory evidentiary effects; the exact signing method therefore matters.

The Israeli insurance-supervision law is in force, so calling a service consulting does not by itself determine its regulatory classification.

## Verification

Run `python -m pytest -q`.

RFC 3161 output must be retained together with the certificate material needed for independent verification. External anchoring is not treated as complete until an actual receipt/proof is received and verified.
