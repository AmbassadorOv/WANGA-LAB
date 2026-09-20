# Vitruvius — Research Group and Branch Integration Map

Status: ARCHITECTURE INTEGRATION SPECIFICATION
Version: 0.1.0
Parent: VITRUVIUS-ORCHESTRATOR

## Purpose

This document fixes the attachment points between Vitruvius and the currently configured WANGA research groups. It is the branch map for future expansion.

## Canonical relation

    RESEARCH ASSET
          |
          v
    RESEARCH GROUP
          |
          v
    PROJECT / ARTIFACT
          |
          v
    LINEAGE
          |
          v
    INTEGRATION EVENT
          |
          v
    WANGA POLITEIA
          |
          v
    VITRUVIUS
          |
          v
    CANDIDATE ARCHITECTURE / MODEL
          |
          v
    LOGIC HANDOFF

## Research groups

| Group | Mission | Vitruvius relation | Future branch family |
|---|---|---|---|
| RG-NEURAL-CORE | Neural representation, state, transition, behavior | Neural architecture lineage and model candidates | neural-core descendants |
| RG-NEURAL-OS | Neural-native OS, kernel, memory, scheduling | System architecture lineage and dependency context | neural-os descendants |
| RG-MODEL-RUNTIME | Local/remote model runtimes and adapters | Runtime compatibility and deployment context | runtime descendants |
| RG-NODE-NETWORK | Communication, synchronization, offline operation | Topology, node lineage and integration context | node-network descendants |
| RG-MEMORY-KNOWLEDGE | Memory, provenance, evidence, knowledge representation | Provenance/lineage substrate | memory-knowledge descendants |
| RG-ARCHITECT-INTERFACE | Architect workspace, project graph, human-machine interface | Whole-system visualization and control surface | interface descendants |

## Current asset integration

The existing research-asset registry maps 15 assets into the six groups. Vitruvius treats these mappings as integration evidence and organizational structure, not as proof that every asset is a separate architecture.

The 15 assets currently represented are:

- ASSET-001 Neural Network Research Core
- ASSET-002 WANGA OS Architecture
- ASSET-003 WANGA Boot Protocol
- ASSET-004 ARK Kernel
- ASSET-005 AI Drift Forensics
- ASSET-006 Forensic Card / Case Engine
- ASSET-007 International Drift Propagation
- ASSET-008 Event Response System
- ASSET-009 Daily Scientific Digest
- ASSET-010 Research Architecture Map
- ASSET-011 Research Subdomain Groups
- ASSET-012 WANGA Work Manager
- ASSET-013 Agent Bridge
- ASSET-014 Model Runtime Layer
- ASSET-015 WANGA Research Groups

## Branch attachment rules

A future branch must attach to one or more of:

1. a research group;
2. an existing asset;
3. a lineage;
4. an architecture family;
5. an integration event;
6. a documented research question.

It must not appear as an unanchored top-level branch.

## Branch classes

### DOMAIN_BRANCH
A new research domain or subdomain.

### ASSET_BRANCH
A new implementation/research asset.

### LINEAGE_BRANCH
A new descendant from an existing lineage.

### INTEGRATION_BRANCH
A branch created by combining existing lineages.

### ARCHITECTURE_BRANCH
A new architecture family or architecture revision.

### MODEL_BRANCH
A model candidate or model family.

### VALIDATION_BRANCH
A validation, replication, audit or evidence branch.

## Vitruvius branch semantics

Vitruvius does not own the scientific content of the branch. It owns the architectural relation of the branch to the whole.

For every branch, Vitruvius should be able to answer:

- Where did it come from?
- What does it inherit?
- What is new?
- What does it connect to?
- What evidence supports the connection?
- What conflicts exist?
- What was validated?
- What remains unknown?
- What architecture role does it currently occupy?
- What downstream model or logic boundary can it affect?

## Recursive branch formation

    GROUP
      |
    ASSET
      |
    LINEAGE
      |
    INTEGRATION
      |
    DESCENDANT
      |
    NEW BRANCH
      |
    NEW LINEAGE
      |
    VITRUVIUS UPDATE

## Group-to-Vitruvius matrix

| Group | Primary input | Primary Vitruvius object | Downstream concern |
|---|---|---|---|
| NEURAL-CORE | neural research | MODEL / MODEL_FAMILY | logical model candidates |
| NEURAL-OS | OS architecture | ARCHITECTURE / FAMILY | system composition |
| MODEL-RUNTIME | runtime adapter | COMPATIBILITY_OBSERVATION | executable model context |
| NODE-NETWORK | node topology | INTEGRATION_EVENT | distributed composition |
| MEMORY-KNOWLEDGE | provenance/evidence | LINEAGE / VALIDATION_RECORD | evidence integrity |
| ARCHITECT-INTERFACE | graph/workspace | WHOLE_ARCHITECTURE_VIEW | human inspection and control |

## Installation / organization scope

The connected GitHub organization installation is treated as an access boundary, not as an architectural branch by itself. Repository membership and permissions establish where Vitruvius may discover and maintain artifacts; architectural identity must still come from explicit registry records.

Installation reference supplied for this project:
https://github.com/organizations/Quadruple-Multilevel-projection-project/settings/installations/90200124

## Canonical rule

No future GitHub repository, branch, group or file becomes a WANGA architectural descendant merely because it exists.

Existence in GitHub is an artifact fact.

Architectural membership requires an explicit relationship record.
