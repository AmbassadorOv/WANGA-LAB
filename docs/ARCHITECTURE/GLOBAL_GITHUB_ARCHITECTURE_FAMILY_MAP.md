# Global GitHub Architecture Family Map

Status: RESEARCH INDEX
Branch: agent/architecture/wanga-computer-architecture

## Principle

GitHub is treated as a distributed architecture ecosystem. WANGA maps repositories into family trees by architectural function, lineage, capability, interface, evidence, and possible descendants.

This is an expanding index, not an exhaustive scan and not a claim of ownership, partnership, integration, or license permission.

## Root families

NEURAL
  -> Transformers / Foundation Architectures
  -> Graph Transformers
  -> Neuro-Symbolic
  -> Reinforcement Learning
  -> Vector-Symbolic

ORCHESTRATION
  -> Multi-Agent
  -> Workflow / Runtime
  -> Execution Control

DATA / MEMORY
  -> Vector Databases
  -> Knowledge Graphs
  -> Provenance / Lineage
  -> Model Registry

GOVERNANCE
  -> AI Governance
  -> Policy / Capability Control
  -> Reference Architecture

SYSTEMS
  -> Distributed / Cloud
  -> Digital Twin
  -> Hardware / Accelerated Compute

VERIFICATION
  -> Formal Methods
  -> Runtime Verification
  -> Evaluation / Drift

## Current lineage anchors

IBM/neuro-symbolic-ai [main]
  -> NEURO-SYMBOLIC
  -> Rational Logic interface / Translation / Verification

IBM/neuro-vector-symbolic-architectures
  -> VECTOR-SYMBOLIC
  -> NTM representation / Translation

microsoft/torchscale [main]
  -> FOUNDATION ARCHITECTURE
  -> Model Fabric / Computational Engine

graphdeeplearning/graphtransformer [repository metadata reports master]
  -> GRAPH TRANSFORMER
  -> Lineage Knowledge / Relationship Mapping / NTM

milvus-io/milvus [master]
  -> VECTOR DATA
  -> Work Memory / Semantic Memory / Model Fabric

openlineage/OpenLineage [main]
  -> PROVENANCE / LINEAGE
  -> Evidence / Provenance / Drift Forensics

mlflow/mlflow [master]
  -> MODEL LIFECYCLE / REGISTRY
  -> Model Fabric / Lineage / Evidence

wso2/reference-architecture [master]
  -> REFERENCE ARCHITECTURE / GOVERNANCE / CONTROL PLANE
  -> Vitruvius / Politeia / WANGA OS

VRSEN/agency-swarm [main]
  -> MULTI-AGENT ORCHESTRATION
  -> Digital Model Agents / WANGA OS / NTM

dennybritz/reinforcement-learning [master]
  -> REINFORCEMENT LEARNING
  -> NTM / Computational Engine / adaptive decision layer

## Architectural marriages

NEURAL + SYMBOLIC
  -> NEURO-SYMBOLIC TRANSLATION

GRAPH + LINEAGE
  -> ARCHITECTURAL RELATIONSHIP GRAPH

MODEL REGISTRY + PROVENANCE
  -> VERIFIED MODEL LINEAGE

MULTI-AGENT + GOVERNANCE
  -> GOVERNED AGENT FABRIC

VECTOR MEMORY + LINEAGE
  -> EVIDENCE-AWARE SEMANTIC MEMORY

RL + VERIFICATION
  -> VERIFICATION-GATED ADAPTIVE COMPUTATION

TRANSFORMER + MOE + MODEL FABRIC
  -> COMPOSABLE COMPUTATIONAL ENGINE

DIGITAL TWIN + PROVENANCE + DRIFT
  -> ARCHITECTURAL STATE TWIN

## Branch attachment policy

External lineages are observed against their repository's default/primary branch.

No external branch is merged into WANGA.

A WANGA integration PoC uses:
agent/integration/<lineage>/<adapter>

The external repository remains the source of truth for its own implementation.

## Promotion lifecycle

OBSERVED
  -> CLASSIFIED
  -> MAPPED
  -> ADAPTER SPECIFIED
  -> PROTOTYPED
  -> TESTED
  -> VERIFIED
  -> INTEGRATED LINEAGE
  -> DESCENDANT ARCHITECTURE

## Research boundary

A global scan of GitHub cannot be considered literally complete because GitHub is enormous and continuously changing. The objective is therefore to build a machine-maintained architecture index that expands by family, not a one-time list of repositories.

Rational Logic remains a protected architectural component. Public mapping may describe its role and interfaces without exposing its implementation.
