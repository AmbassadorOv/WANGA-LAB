"""
Unit tests for ARKAutonomousKnowledgeConnector module.
"""

import pytest
from ark_kernel import IterationEngine
from wanga.matrix import OntologicalMatrix, OntologicalLayerType
from ark_autonomous_knowledge_connector import ARKAutonomousKnowledgeConnector


def test_connector_fetch_knowledge():
    connector = ARKAutonomousKnowledgeConnector()
    payload = connector.fetch_knowledge("Test Knowledge Query")
    assert payload is not None
    assert "connector_id" in payload
    assert payload["query"] == "Test Knowledge Query"
    assert "proposal" in payload
    assert payload["proposal"]["version"] == "1.0.0"


def test_connector_ingest_into_matrix():
    connector = ARKAutonomousKnowledgeConnector()
    payload = connector.fetch_knowledge("Matrix Ingestion Query")
    matrix = OntologicalMatrix()

    updated_matrix = connector.ingest_into_matrix(matrix, payload)
    assert len(updated_matrix.nodes) >= 2
    assert len(updated_matrix.relations) >= 1

    source_nodes = updated_matrix.get_nodes_by_layer(OntologicalLayerType.SOURCE)
    assert len(source_nodes) >= 1
    assert "Matrix Ingestion Query" in source_nodes[0].label


def test_connector_synchronize_kernel():
    connector = ARKAutonomousKnowledgeConnector()
    engine = IterationEngine()
    matrix = OntologicalMatrix()
    payload = connector.fetch_knowledge("Kernel Sync Query")
    connector.ingest_into_matrix(matrix, payload)

    summary = connector.synchronize_kernel(engine, matrix)
    assert summary["sync_status"] == "SUCCESS"
    assert summary["iteration"] == 1
    assert summary["node_count"] == 22
    assert summary["matrix_node_count"] == len(matrix.nodes)


def test_connector_run_autonomous_cycle():
    connector = ARKAutonomousKnowledgeConnector()
    result = connector.run_autonomous_cycle("Autonomous Cycle Query")
    assert result["cycle_status"] == "COMPLETED"
    assert result["matrix_summary"]["total_nodes"] >= 2
    assert result["kernel_sync"]["sync_status"] == "SUCCESS"
