# WANGA Model-Agent Architecture V1

Status: ARCHITECTURE / BUILD SPECIFICATION

Create a scalable model fabric in which every connected AI model is represented by a deterministic Digital Model Agent (DMA). The target scale is 5,000+ model slots. A slot is not a claim that a real model endpoint exists; activation requires discovery, configuration, capability declaration, connectivity verification, and policy validation.

System position:
WANGA OS -> Model Fabric -> Digital Model Agents -> Model Providers/Runtimes
Model Fabric -> existing Work Manager / Orchestrator
Model Fabric -> Evidence / Drift Forensics
Model Fabric -> Rational Logic -> Neural Thinking Machine
Rational Logic -> Evidence / Verification

The Neural Thinking Machine (NTM) remains the high-level cognitive CPU. Rational Logic is a complementary formal reasoning layer; it is not an executor and does not replace NTM. It receives bounded representations, evidence, conflicts, and verified findings; it does not become an unrestricted executor.

Agent lifecycle:
DISCOVER -> CLASSIFY -> ASSIGN_GENERAL_ROLE -> ASSIGN_PRIVATE_ROLES -> ADAPTER_BIND -> CAPABILITY_PROBE -> POLICY_BIND -> REGISTER -> HEALTH_CHECK -> ENABLE

Model family classes:
reasoning, planning, general-language, coding, research, vision, audio, embedding, reranking, classification, translation, mathematics, science, long-context, tool-use, safety-policy, evaluation, drift, knowledge-graph, image-generation, video, domain-specialist, local-open-weight, edge, router-ensemble.

General role:
Each model receives one primary general role such as planner, reasoner, researcher, coder, verifier, critic, synthesizer, perception, speech_processor, embedder, reranker, classifier, translator, mathematician, scientist, document_analyst, tool_operator, safety_analyst, evaluator, drift_analyst, knowledge_builder, generator, temporal_analyst, domain_specialist, local_runtime, edge_runtime, or router.

Private roles:
Each model agent receives a bounded set derived from declared capabilities: task decomposition, hypothesis generation, evidence extraction, source comparison, code synthesis, code review, test generation, semantic normalization, structural comparison, contradiction detection, drift classification, retrieval query planning, provenance packaging, confidence estimation, output formatting, escalation to NTM, verification request, tool invocation, latency fallback, context compression, multimodal alignment, embedding generation, reranking, and translation normalization.

Routing:
task -> capability match -> policy filter -> model-agent selection -> execution -> evidence envelope -> Rational Logic check when required -> verification -> NTM escalation when required

The existing WANGA Work Manager / Orchestrator remains the coordination layer. This fabric does not create a second global task manager.

Scaling:
The registry contains model slots, not invented live endpoints. Each slot records family, provider, exact model_id when known, general role, private roles, adapter, capability metadata, policy class, status, provenance, and verification state.

Thinking Machine interface:
The NTM receives task_id, model_agent_id, model/version identifier, capability claims, input/output provenance, evidence references, reasoning status, drift findings, conflicts, verification status, and escalation reason.

Invariants:
- No provider secret is stored in the registry.
- No model is marked ENABLED without successful capability and health verification.
- Conflicts block automatic promotion rather than being guessed through.
- Historical branches and architecture artifacts remain preserved.
- Final architecture review remains a separate stage after automated construction.
