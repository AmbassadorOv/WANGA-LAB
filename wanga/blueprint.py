"""
WANGA Blueprint Registry and Processor Profile Loader
"""

import json
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field, ConfigDict


class BlueprintNode(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: int
    role: str
    recommended_processor: str
    rationale: str
    category: str


class ProcessorProfile(BaseModel):
    model_config = ConfigDict(extra="ignore")
    family: str
    execution_mode: str = "virtual"
    capabilities: List[str] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class BlueprintProfile(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    name: str
    description: str
    operator: str
    purpose: str
    status: str = "conceptual"


class BlueprintTopology(BaseModel):
    model_config = ConfigDict(extra="ignore")
    vertex_count: int = 21
    gate_count: int = 231
    connections: List[Dict[str, Any]] = Field(default_factory=list)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class BlueprintRegistry:
    """
    Registry and strategy manager for architectural blueprints and processor profiles.
    """

    def __init__(self, config_path: str = "config/photonic_neuromorphic_matrix.json"):
        self.config_path = config_path
        self.raw_config: Dict[str, Any] = {}
        self.nodes: Dict[int, BlueprintNode] = {}
        self.blueprints: Dict[str, BlueprintProfile] = {}
        self.active_blueprint_name: Optional[str] = None
        self.topology: BlueprintTopology = BlueprintTopology()
        self.receptors: Dict[str, Any] = {}
        self.rule_system: Dict[str, Any] = {}
        self.load_config(config_path)

    def load_config(self, path: str):
        with open(path, "r", encoding="utf-8") as f:
            self.raw_config = json.load(f)

        self.nodes.clear()
        for nd in self.raw_config.get("nodes", []):
            node_obj = BlueprintNode.model_validate(nd)
            self.nodes[node_obj.id] = node_obj

        self.blueprints.clear()
        for bp in self.raw_config.get("blueprints", []):
            bp_obj = BlueprintProfile.model_validate(bp)
            self.blueprints[bp_obj.name] = bp_obj
            if self.active_blueprint_name is None:
                self.active_blueprint_name = bp_obj.name

        top_data = self.raw_config.get("topology", {})
        self.topology = BlueprintTopology(
            vertex_count=self.raw_config.get("total_vertices", 21),
            gate_count=self.raw_config.get("epicyclic_gates", 231),
            connections=top_data.get("connections", [])
        )

        self.receptors = self.raw_config.get("receptor_configuration", {})
        self.rule_system = self.raw_config.get("rule_system", {})

    def get_node(self, node_id: int) -> Optional[BlueprintNode]:
        return self.nodes.get(node_id)

    def get_nodes(self) -> List[BlueprintNode]:
        return list(self.nodes.values())

    def get_nodes_by_category(self, category: str) -> List[BlueprintNode]:
        return [n for n in self.nodes.values() if n.category.lower() == category.lower()]

    def list_blueprints(self) -> List[str]:
        return list(self.blueprints.keys())

    def get_blueprint(self, name: str) -> Optional[BlueprintProfile]:
        return self.blueprints.get(name)

    def set_active_blueprint(self, name: str):
        if name not in self.blueprints:
            raise KeyError(f"Blueprint '{name}' not found in registry")
        self.active_blueprint_name = name

    def get_active_blueprint(self) -> Optional[BlueprintProfile]:
        if self.active_blueprint_name:
            return self.blueprints.get(self.active_blueprint_name)
        return None

    def map_node_to_processor_profile(self, node: BlueprintNode) -> ProcessorProfile:
        rec = node.recommended_processor.lower()
        if "photonic" in rec or "optical" in rec:
            family = "photonic"
            capabilities = ["phase_compute", "optical_transform", "wavefront_routing"]
        elif "quantum" in rec:
            family = "quantum_morphic"
            capabilities = ["statevector_simulation", "superposition_calc"]
        elif "neuromorphic" in rec or "spike" in rec or "memristor" in rec:
            family = "neuromorphic"
            capabilities = ["spike_routing", "weight_adaptation"]
        elif "gate" in rec or "security" in rec or "firewall" in rec or "signer" in rec:
            family = "security_logic"
            capabilities = ["231_gate_check", "signature_verify", "sandbox_isolate"]
        else:
            family = "virtual_core"
            capabilities = ["register_compute", "memory_map"]

        return ProcessorProfile(
            family=family,
            execution_mode="virtual",
            capabilities=capabilities,
            metadata={
                "node_id": node.id,
                "role": node.role,
                "recommended_processor": node.recommended_processor,
                "category": node.category
            }
        )
