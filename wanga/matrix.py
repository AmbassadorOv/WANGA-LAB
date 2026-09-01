"""
WANGA Unified Ontological Matrix Component
"""

import time
import uuid
from enum import Enum
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field, ConfigDict


class OntologicalLayerType(str, Enum):
    SOURCE = "SOURCE"            # Tanakh (Primitives, Source Relations)
    INTERPRETATION = "INTERPRETATION"  # Talmud (Birur, Argument, Reasoning space)
    CONFIGURATION = "CONFIGURATION"    # Kabbalah (Relational Matrix Configuration)
    METAPHYSICAL = "METAPHYSICAL"      # Ontological State Transitions
    RESOLUTION = "RESOLUTION"          # Resolved Decision / Rule Match
    REALIZATION = "REALIZATION"        # Executable Code / Realized State


class OntologicalNode(BaseModel):
    model_config = ConfigDict(extra="ignore")
    node_id: str
    layer: OntologicalLayerType
    label: str
    attributes: Dict[str, Any] = Field(default_factory=dict)
    provenance: Dict[str, Any] = Field(default_factory=dict)


class OntologicalRelation(BaseModel):
    model_config = ConfigDict(extra="ignore")
    relation_id: str
    source_node_id: str
    target_node_id: str
    relation_type: str
    layer_provenance: OntologicalLayerType
    weight: float = 1.0
    metadata: Dict[str, Any] = Field(default_factory=dict)


class OntologicalMatrix(BaseModel):
    """
    Multidimensional relational matrix G = (V, E, L, S) preserving provenance and non-flat layer hierarchy.
    """

    model_config = ConfigDict(extra="ignore")
    matrix_id: str = Field(default_factory=lambda: f"matrix-{uuid.uuid4().hex[:8]}")
    nodes: Dict[str, OntologicalNode] = Field(default_factory=dict)
    relations: List[OntologicalRelation] = Field(default_factory=list)
    created_at: float = Field(default_factory=time.time)

    def add_node(self, node: OntologicalNode) -> OntologicalNode:
        self.nodes[node.node_id] = node
        return node

    def add_relation(self, relation: OntologicalRelation) -> OntologicalRelation:
        if relation.source_node_id in self.nodes and relation.target_node_id in self.nodes:
            self.relations.append(relation)
        return relation

    def get_nodes_by_layer(self, layer: OntologicalLayerType) -> List[OntologicalNode]:
        return [n for n in self.nodes.values() if n.layer == layer]

    def get_relations_for_node(self, node_id: str) -> List[OntologicalRelation]:
        return [r for r in self.relations if r.source_node_id == node_id or r.target_node_id == node_id]

    def export_summary(self) -> Dict[str, Any]:
        layer_counts = {l.value: 0 for l in OntologicalLayerType}
        for n in self.nodes.values():
            layer_counts[n.layer.value] += 1

        return {
            "matrix_id": self.matrix_id,
            "total_nodes": len(self.nodes),
            "total_relations": len(self.relations),
            "layer_distribution": layer_counts
        }
