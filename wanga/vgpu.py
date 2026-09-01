"""
WANGA-NANO-21 Phase 1: Virtual GPU, Virtual NanoProcessor, and Execution Engine Abstraction Layer
"""

import time
import uuid
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional, Callable


class VNPState(str, Enum):
    CREATED = "CREATED"
    READY = "READY"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"


@dataclass
class VNPConfig:
    id: str
    vnp_type: str = "virtual_nano"
    capacity: int = 1
    memory_capacity_mb: int = 64
    enabled: bool = True
    device: str = "cpu"
    priority: int = 1
    blueprint_node_id: Optional[int] = None
    processor_family: Optional[str] = None
    category: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass
class ExecutionPacket:
    packet_id: str
    source_processor: str
    destination_processor: str
    operation: str
    payload: Any
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)


class VirtualNanoProcessor:
    """
    Logical Virtual NanoProcessor execution unit with strict lifecycle states.
    """

    def __init__(self, config: VNPConfig, op_handler: Optional[Callable[[Any], Any]] = None):
        self.config = config
        self.id = config.id
        self.blueprint_node_id = config.blueprint_node_id
        self.processor_family = config.processor_family or "virtual_core"
        self.category = config.category or "General"
        self.state = VNPState.CREATED
        self.memory: Dict[str, Any] = {}
        self.input_buffer: List[ExecutionPacket] = []
        self.output_buffer: List[ExecutionPacket] = []
        self.op_handler = op_handler or self._default_op_handler
        self.metrics = {
            "operations_executed": 0,
            "packets_processed": 0,
            "errors": 0,
            "total_execution_time": 0.0
        }
        self.state = VNPState.READY

    def _default_op_handler(self, payload: Any) -> Any:
        if isinstance(payload, (int, float)):
            return payload * 2
        elif isinstance(payload, str):
            return f"processed_{payload}"
        elif isinstance(payload, dict):
            res = dict(payload)
            res["processed"] = True
            return res
        return payload

    def receive_packet(self, packet: ExecutionPacket):
        self.input_buffer.append(packet)

    def execute_next(self) -> Optional[ExecutionPacket]:
        if not self.input_buffer:
            return None

        packet = self.input_buffer.pop(0)
        self.state = VNPState.RUNNING
        start_time = time.time()

        try:
            res_payload = self.op_handler(packet.payload)
            self.metrics["operations_executed"] += 1
            self.metrics["packets_processed"] += 1
            exec_time = time.time() - start_time
            self.metrics["total_execution_time"] += exec_time

            out_packet = ExecutionPacket(
                packet_id=f"pkt-{uuid.uuid4().hex[:8]}",
                source_processor=self.id,
                destination_processor=packet.destination_processor,
                operation=packet.operation,
                payload=res_payload,
                metadata={"prev_packet_id": packet.packet_id, "exec_time": exec_time}
            )
            self.output_buffer.append(out_packet)
            self.state = VNPState.COMPLETED
            return out_packet
        except Exception as e:
            self.state = VNPState.ERROR
            self.metrics["errors"] += 1
            raise e

    def reset_state(self):
        self.state = VNPState.READY


class VirtualNeuralProcessor:
    """
    Interface/Placeholder abstraction for future Virtual Neural Processor composition.
    """

    def __init__(self, processor_id: str):
        self.processor_id = processor_id
        self.input_processors: List[str] = []
        self.compute_processors: List[str] = []
        self.output_processors: List[str] = []
        self.memory_state: Dict[str, Any] = {}

    def connect_input(self, vnp_id: str):
        self.input_processors.append(vnp_id)

    def connect_output(self, vnp_id: str):
        self.output_processors.append(vnp_id)
