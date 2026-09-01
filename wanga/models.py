"""
WANGA Architecture Models & Specification Types
"""

from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field, ConfigDict


class AgentSpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    name: str
    role: str = "orchestrator"
    capabilities: List[str] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list)


class NeuralComponentSpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    architecture_type: str = "mlp"  # e.g., mlp, cnn, transformer
    input_dim: int = 8
    output_dim: int = 4
    hidden_dims: List[int] = Field(default_factory=lambda: [16, 16])
    learning_rate: float = 0.01
    device: str = "cpu"
    seed: Optional[int] = 42


class VNPSpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    registers_count: int = 8
    memory_size: int = 256
    clock_speed_mhz: float = 1.0
    router_id: Optional[str] = None
    initial_instructions: List[Dict[str, Any]] = Field(default_factory=list)


class FabricConnection(BaseModel):
    model_config = ConfigDict(extra="ignore")
    source: str
    target: str
    bandwidth: int = 1000
    protocol: str = "direct"


class FabricSpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    connections: List[FabricConnection] = Field(default_factory=list)


class ToolSpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    name: str
    type: str = "builtin"
    permissions: List[str] = Field(default_factory=list)


class SecuritySpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    signature_required: bool = False
    sandbox_required: bool = True
    max_memory_mb: int = 512
    max_execution_seconds: int = 60
    allowed_gates: List[int] = Field(default_factory=lambda: list(range(1, 232)))


class ExperimentSpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    seed: int = 42
    steps: int = 10
    target_metric: str = "loss"
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)


class WangaArchitectureSpec(BaseModel):
    model_config = ConfigDict(extra="ignore")
    version: str = "1.0.0"
    name: str
    description: Optional[str] = ""
    agents: List[AgentSpec] = Field(default_factory=list)
    neural_components: List[NeuralComponentSpec] = Field(default_factory=list)
    virtual_nano_processors: List[VNPSpec] = Field(default_factory=list)
    fabric: FabricSpec = Field(default_factory=FabricSpec)
    tools: List[ToolSpec] = Field(default_factory=list)
    security: SecuritySpec = Field(default_factory=SecuritySpec)
    experiment: ExperimentSpec
    metadata: Dict[str, Any] = Field(default_factory=dict)
