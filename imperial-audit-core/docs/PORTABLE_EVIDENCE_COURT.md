# Portable Evidence Court — Imperial Audit Core

## Purpose

Imperial Audit Core now has a portable evidence verification mode.
The goal is operational resilience: a complete evidence package can be copied to removable storage and verified on an independent machine without access to the issuer application server.

The device is not treated as a literal judge. It is a deterministic verifier that answers:
- Does the supplied data reproduce S1/S2/S3?
- Does the supplied contract reproduce LEGAL_CONTRACT_HASH?
- Does the supplied data reproduce MASTER_CHAIN_HASH?
- Does each declared blockchain anchor point to that exact master hash?
- Has an independent chain adapter actually verified the blockchain proof, or is the anchor only declared?

## Verification states

- PASS: local cryptographic check succeeded.
- FAIL: package is internally inconsistent or tampered.
- UNVERIFIED: a claim exists, but there is not enough proof for independent verification.
- PARTIAL: local integrity is verified but an external claim remains unverified.
- VERIFIED: all implemented checks passed and every required external proof was independently verified.

A transaction ID, block height, explorer URL, or screenshot is not by itself a cryptographic proof of chain inclusion.

## Threat model

The portable mode assumes the original issuer may be unavailable. It therefore avoids requiring the issuer web server, issuer database, GitHub, or a single timestamp server.

It does not assume that every blockchain remains reachable forever. If a full chain proof or independently maintained chain snapshot is not present, the system reports UNVERIFIED rather than inventing certainty.

## Blockchain layer

Bitcoin OP_RETURN can carry a compact hash commitment; Bitcoin Core documents OP_RETURN relay/mining behavior and script-size limits.

Ethereum transaction receipts contain logs emitted by contract execution, and Ethereum JSON-RPC exposes those receipts.

Ethereum logs can be affected by chain reorganizations while they are not final on the canonical chain, so the verifier records chain ID, block hash, transaction hash and a finality policy rather than treating a transaction hash as absolute truth.

## Legal boundary

The software establishes technical facts about bytes, hashes and supplied chain proofs. It does not automatically establish that the underlying financial data is true, who legally owns the data, that a signer had authority, that a transaction is legally enforceable, or that a court or arbitrator must accept a particular conclusion.

## Operating principle

source -> canonical data -> S1/S2/S3 -> MASTER_CHAIN_HASH -> evidence pack -> optional Bitcoin anchor -> optional Ethereum anchor -> removable storage -> independent verifier

The critical property is that verification can continue even when the original application is gone.
