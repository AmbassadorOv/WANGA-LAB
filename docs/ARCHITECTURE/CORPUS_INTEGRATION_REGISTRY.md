# Corpus Integration Registry

This registry is the control-plane index for connecting existing research artifacts to the WANGA architecture.

## Registry fields

- artifact_id
- repository
- path
- artifact_type
- domain
- subdomain
- research_group
- project
- provenance
- maturity
- publication_status
- verification_status
- related_artifacts
- integration_target
- historical_notes
- unresolved_questions

## Initial integration targets

### AI Drift Forensics
Behavioral drift, evidence preservation, reconstruction, verification, evaluation lifecycle.

### WANGA Systems Architecture
Global Work Manager, Model Fabric, Digital Model Agents, providers/runtimes, evidence/provenance, work memory.

### Rational Logic / NTM
Reasoning architecture, inference-time computation, memory, search, neuro-symbolic verification.

### AI²³¹ / Formal Language
Higayon-related formal structures, symbolic relations, place/context and computational framing.

### Research Composition
Paper-to-agent workflows, cross-domain research composition, evaluation re-entry, executable research.

### Governance / Institutional Architecture
Governance interfaces, institutional infrastructure, risk/evidence systems and research governance.

### Publication Network
Articles, public research surfaces, scientific indexing and evidence-linked publication.

## Operating rule

The registry is append-only at the evidence level. Reclassification is allowed, but previous classification decisions should remain recoverable through Git history.
