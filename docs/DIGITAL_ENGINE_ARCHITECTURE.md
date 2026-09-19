# Digital Engine Architecture

The **Digital Engine Architecture (DEA)** is the lower execution architecture of WANGA. It classifies the computational machinery that turns architectural intent, work, models, evidence and verification requirements into executable operations.

## Core layers

1. **Work Control** — Global Work Manager and bounded task state.
2. **Translation** — structural and semantic representation changes.
3. **Model Fabric** — model slots, providers, runtimes, capabilities, health and policy.
4. **Digital Model Agents** — bounded workers.
5. **Evidence & Provenance** — artifact identity, lineage and preservation.
6. **Drift Forensics & Verification** — reconstruction, comparison and independent verification.
7. **Rational Logic / NTM boundary** — reasoning and re-evaluation interfaces, with protected implementation boundaries.
8. **Work Memory** — persistent operational state.
9. **Governance Interface** — controlled external publication and governance-facing outputs.

## Engine analogy

The phrase **“steam engine”** is used as an architectural analogy for the inner work-producing core: the part that converts defined inputs and constraints into computational work.

The **digital engine** is the actual executable architecture surrounding that core. It supplies routing, translation, model execution, evidence capture, verification and state management.

## Upper/lower contract

The DEA does not independently decide the global architecture.

The VSA/Vitruvius layer supplies architectural identity, family membership, relationship candidates, dependency and impact maps, integration boundaries and affected-work sets.

The DEA supplies executable tasks, runtime operations, artifacts, evidence, test results and verification inputs.

Neither layer is allowed to silently promote its own output to VERIFIED.
