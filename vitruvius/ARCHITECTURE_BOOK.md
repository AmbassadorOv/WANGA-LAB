# Vitruvius Architecture Book

Status: ACTIVE DEVELOPMENT
Version: 0.1.0

This book is the human-readable companion to vitruvius/data/architecture_book.json. It records where each observed architecture came from, which primary branch was observed, how it is classified, and where it may connect to WANGA.

## Family roots

NEURAL -> MODEL_FABRIC / NTM / TRANSLATION / COMPUTATIONAL_ENGINE
LOGIC -> RATIONAL_LOGIC_BOUNDARY / TRANSLATION / VERIFICATION
SYSTEMS -> COMPUTATIONAL_ENGINE / WANGA_OS / VITRUVIUS
GOVERNANCE -> POLITEIA / WANGA_OS / VITRUVIUS
MEMORY -> LINEAGE_KNOWLEDGE / WORK_MEMORY / EVIDENCE_PROVENANCE / MODEL_FABRIC
ORCHESTRATION -> WANGA_OS / DIGITAL_MODEL_AGENTS / NTM / VITRUVIUS

## Current observed anchors

| Repository | Primary branch | Family | WANGA target | State |
|---|---|---|---|---|
| AmbassadorOv/WANGA-LAB | main | WANGA_COMPUTER | WANGA-LAB | OBSERVED_SEED |
| AmbassadorOv/AI231.meta.io | main | LOGIC | RATIONAL_LOGIC | OBSERVED_SEED |
| AmbassadorOv/ai-agent-terraform | main | ORCHESTRATION | WANGA_OS | OBSERVED_SEED |
| AmbassadorOv/multi-agent-orchestator | main | ORCHESTRATION | WANGA_OS | OBSERVED_SEED |
| AmbassadorOv/python-genai | main | NEURAL | MODEL_FABRIC | OBSERVED_SEED |
| IBM/neuro-symbolic-ai | main | NEURAL | TRANSLATION | OBSERVED_SEED |
| stepfun-ai/StepFun-Prover-Preview | main | LOGIC | VERIFICATION | OBSERVED_SEED |
| vercel/workflow | main | ORCHESTRATION | WANGA_OS | OBSERVED_SEED |
| microsoft/agent-framework | main | ORCHESTRATION | DIGITAL_MODEL_AGENTS | OBSERVED_SEED |
| GovernanceAISystems/AI-Governance-Architecture | main | GOVERNANCE | POLITEIA | OBSERVED_SEED |
| delorenj/mcp-qdrant-memory | main | MEMORY | WORK_MEMORY | OBSERVED_SEED |
| openlineage/OpenLineage | main | MEMORY | EVIDENCE_PROVENANCE | OBSERVED_SEED |
| milvus-io/milvus | master | MEMORY | WORK_MEMORY | OBSERVED_SEED |
| Developer-Y/Scalable-Software-Architecture | master | SYSTEMS | VITRUVIUS | OBSERVED_SEED |
| theanalyst/awesome-distributed-systems | master | SYSTEMS | COMPUTATIONAL_ENGINE | OBSERVED_SEED |

## Origin rule

Primary/default branch is the observation source. It does not establish ancestry by itself.

An ancestry edge is valid only when supported by a source reference, explicit project decision, documented derivation, or verified integration event.

## Architectural connection rule

EXTERNAL LINEAGE
  -> PROPERTY
  -> FAMILY
  -> VITRUVIUS NODE
  -> WANGA TARGET
  -> ADAPTER CANDIDATE
  -> TEST
  -> VERIFY
  -> DESCENDANT

No automatic external merge is implied.

## Model-assisted layer

GPT/LLM/neural models may assist extraction, classification, relationship proposals and composition candidates through vitruvius/MODEL_BRIDGE.md. Model output is retained as observation/candidate data until independently checked.

## Automated index

vitruvius/architecture_indexer.py performs public GitHub repository discovery and produces observed architecture records. .github/workflows/vitruvius-global-index.yml schedules refreshes.

The global corpus is necessarily incremental; this book is an expanding index, not a claim of exhaustive GitHub coverage.
