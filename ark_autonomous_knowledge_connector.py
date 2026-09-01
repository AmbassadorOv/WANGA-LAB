"""
ARK Autonomous Knowledge Connector Component
--------------------------------------------
Interfaces ARK-KERNEL T-duality/holographic execution engine with the
WANGA Unified Ontological Matrix, Gemini proposal engine, and external APIs.
"""

import logging
import uuid
import time
from typing import Dict, Any, List, Optional
import requests

from ark_kernel import IterationEngine, HEBREW_LETTERS
from wanga.matrix import (
    OntologicalMatrix,
    OntologicalNode,
    OntologicalRelation,
    OntologicalLayerType,
)
from wanga.gemini import GeminiAdapter
from wanga.ontology import OntologyValidator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ARKAutonomousKnowledgeConnector")


class ARKAutonomousKnowledgeConnector:
    """
    Autonomous Knowledge Connector bridging external data streams,
    Gemini proposal generation, WANGA Ontological Matrix, and ARK-KERNEL engine.
    """

    def __init__(
        self,
        gemini_adapter: Optional[GeminiAdapter] = None,
        validator: Optional[OntologyValidator] = None,
    ):
        self.gemini_adapter = gemini_adapter or GeminiAdapter()
        self.validator = validator or OntologyValidator()

    def fetch_knowledge(
        self, query: str, source_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Fetches external knowledge payload via URL or generates proposal via Gemini adapter.
        """
        fetched_content = None
        if source_url:
            try:
                response = requests.get(source_url, timeout=5)
                if response.status_code == 200:
                    fetched_content = response.text[:1000]
            except Exception as e:
                logger.warning(f"Failed to fetch external URL {source_url}: {e}")

        proposal = self.gemini_adapter.generate_architecture_proposal(query)

        payload = {
            "connector_id": f"conn-{uuid.uuid4().hex[:8]}",
            "query": query,
            "timestamp": time.time(),
            "source_url": source_url,
            "fetched_content": fetched_content,
            "proposal": proposal,
        }
        return payload

    def ingest_into_matrix(
        self, matrix: OntologicalMatrix, data: Dict[str, Any]
    ) -> OntologicalMatrix:
        """
        Ingests fetched knowledge payload into an OntologicalMatrix as layered nodes & relations.
        """
        query_node = OntologicalNode(
            node_id=f"node-query-{uuid.uuid4().hex[:6]}",
            layer=OntologicalLayerType.SOURCE,
            label=f"Query: {data.get('query', 'Unknown')}",
            attributes={
                "source_url": data.get("source_url"),
                "has_content": bool(data.get("fetched_content")),
            },
            provenance={"connector_id": data.get("connector_id")},
        )
        matrix.add_node(query_node)

        proposal = data.get("proposal", {})
        proposal_node = OntologicalNode(
            node_id=f"node-proposal-{uuid.uuid4().hex[:6]}",
            layer=OntologicalLayerType.INTERPRETATION,
            label=proposal.get("name", "Generated Proposal"),
            attributes={
                "version": proposal.get("version"),
                "description": proposal.get("description"),
            },
            provenance={"generator": "GeminiAdapter"},
        )
        matrix.add_node(proposal_node)

        relation = OntologicalRelation(
            relation_id=f"rel-{uuid.uuid4().hex[:6]}",
            source_node_id=query_node.node_id,
            target_node_id=proposal_node.node_id,
            relation_type="DERIVES_PROPOSAL",
            layer_provenance=OntologicalLayerType.INTERPRETATION,
            weight=1.0,
        )
        matrix.add_relation(relation)

        # Ingest sub-components from proposal if present
        for agent in proposal.get("agents", []):
            agent_node = OntologicalNode(
                node_id=agent.get("id", f"agent-{uuid.uuid4().hex[:6]}"),
                layer=OntologicalLayerType.REALIZATION,
                label=agent.get("name", "Agent"),
                attributes={"role": agent.get("role")},
            )
            matrix.add_node(agent_node)
            matrix.add_relation(
                OntologicalRelation(
                    relation_id=f"rel-{uuid.uuid4().hex[:6]}",
                    source_node_id=proposal_node.node_id,
                    target_node_id=agent_node.node_id,
                    relation_type="CONTAINS_AGENT",
                    layer_provenance=OntologicalLayerType.REALIZATION,
                )
            )

        return matrix

    def synchronize_kernel(
        self, engine: IterationEngine, matrix: Optional[OntologicalMatrix] = None
    ) -> Dict[str, Any]:
        """
        Synchronizes the ARK-KERNEL iteration engine with the Ontological Matrix state.
        """
        if matrix:
            # Adjust kernel nodes based on matrix total nodes count and distribution
            node_count = len(matrix.nodes)
            for node in engine.nodes:
                node.bulk_energy += node_count * 0.01

        step_state = engine.step()
        summary = {
            "sync_status": "SUCCESS",
            "iteration": step_state["meta"]["iteration"],
            "node_count": step_state["meta"]["node_count"],
            "total_entropy": step_state["meta"]["total_entropy"],
            "matrix_node_count": len(matrix.nodes) if matrix else 0,
            "matrix_relation_count": len(matrix.relations) if matrix else 0,
        }
        return summary

    def run_autonomous_cycle(
        self, query: str, source_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Executes an end-to-end autonomous knowledge connector cycle.
        """
        logger.info(f"Starting autonomous knowledge cycle for query: '{query}'")

        # 1. Fetch Knowledge
        knowledge = self.fetch_knowledge(query, source_url=source_url)

        # 2. Ingest into Ontological Matrix
        matrix = OntologicalMatrix()
        matrix = self.ingest_into_matrix(matrix, knowledge)

        # 3. Validate Ontology if proposal has architecture specs
        proposal = knowledge.get("proposal", {})
        validation_errors = self.validator.validate(proposal)

        # 4. Synchronize Kernel Engine
        engine = IterationEngine()
        sync_result = self.synchronize_kernel(engine, matrix)

        return {
            "cycle_status": "COMPLETED",
            "knowledge_payload": knowledge,
            "matrix_summary": matrix.export_summary(),
            "validation_errors": validation_errors,
            "kernel_sync": sync_result,
        }


def main():
    print("Initializing ARK Autonomous Knowledge Connector...")
    connector = ARKAutonomousKnowledgeConnector()
    cycle_result = connector.run_autonomous_cycle(
        query="Connect autonomous knowledge streams with photonic-neuromorphic matrix"
    )

    print("\n" + "=" * 50)
    print("ARK AUTONOMOUS KNOWLEDGE CONNECTOR CYCLE REPORT")
    print("=" * 50)
    print(f"Cycle Status: {cycle_result['cycle_status']}")
    print(f"Matrix Nodes Created: {cycle_result['matrix_summary']['total_nodes']}")
    print(
        f"Matrix Relations Created: {cycle_result['matrix_summary']['total_relations']}"
    )
    print(
        f"Validation Errors Count: {len(cycle_result['validation_errors'])}"
    )
    print(f"Kernel Iteration: {cycle_result['kernel_sync']['iteration']}")
    print(f"Kernel Total Entropy: {cycle_result['kernel_sync']['total_entropy']}")
    print("=" * 50)


if __name__ == "__main__":
    main()
