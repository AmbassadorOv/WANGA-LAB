# Paper-to-Agent: From Static Publication to Executable Research Artifact

**Evidence class:** PRIMARY PAPER  
**Window:** 2026-09-12 to 2026-09-19  
**Anchor:** Miao et al., *Nature*, published 2026-09-16.

## Abstract

Scientific papers traditionally preserve methods and results as documents. Paper2Agent proposes a different representation: a research paper and its associated code, data, supplementary material, and workflows can be exposed through an AI-agent interface. The reported system builds MCP servers around research outputs, generates tests, and evaluates whether resulting agents can reproduce published results and answer new queries.

The architectural question is not whether every paper should become an agent. It is whether scientific knowledge can gain a second representation in which the method itself becomes executable, inspectable, and reusable.

## Structural model

**Paper → Method → Tool interface → Test → Reproduction → New query → Evidence**

This creates a useful separation:

- the paper remains the documentary record;
- the executable layer becomes the operational representation;
- tests establish whether the operational layer reproduces relevant behavior;
- new queries are distinguished from reproduction.

## WANGA connection

This maps naturally onto:

**Source → Normalize → Execute → Observe → Preserve evidence → Verify → Compose**

The critical boundary is between *representation* and *verification*. An agent generated from a paper is not automatically a verified scientific instrument. Its provenance, implementation, dependencies, test results, and version must remain visible.

## Research questions

1. Which parts of a paper can be safely operationalized?
2. What minimum tests establish reproduction before new experimentation?
3. How should version changes trigger re-validation?
4. Can multiple paper-agents interoperate without collapsing their methodological boundaries?

## Cross-domain fractals

The same structure can be instantiated for genomics, medical imaging, climate models, materials science, and computational biology:

**Research artifact → executable method → controlled test → evidence → domain-specific application.**

## Source

Miao et al., *Reimagining research papers as interactive and reliable AI agents*, Nature, 16 September 2026. citeturn0news0

**Status:** RESEARCH DRAFT grounded in a primary-paper report; implementation and replication claims remain source-specific.
