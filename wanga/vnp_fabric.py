"""
WANGA-NANO-21 Phase 1: Processor Fabric, Virtual GPU Orchestrator, and Execution Engine
"""

import time
import uuid
from typing import Dict, Any, List, Optional, Tuple
from wanga.vgpu import VirtualNanoProcessor, VNPConfig, VNPState, ExecutionPacket


class VirtualProcessorFabric:
    """
    Manages processor graph topologies, directed connections, dependencies, and routing.
    """

    def __init__(self):
        self.nodes: Dict[str, VirtualNanoProcessor] = {}
        self.edges: List[Tuple[str, str]] = []  # (src_id, tgt_id)

    def add_processor(self, vnp: VirtualNanoProcessor):
        self.nodes[vnp.id] = vnp

    def add_connection(self, src_id: str, tgt_id: str):
        if src_id in self.nodes and tgt_id in self.nodes:
            edge = (src_id, tgt_id)
            if edge not in self.edges:
                self.edges.append(edge)

    def get_downstream(self, src_id: str) -> List[str]:
        return [tgt for src, tgt in self.edges if src == src_id]

    def route_packet(self, packet: ExecutionPacket) -> bool:
        tgt_id = packet.destination_processor
        if tgt_id in self.nodes:
            self.nodes[tgt_id].receive_packet(packet)
            return True
        return False

    def get_topology_info(self) -> Dict[str, Any]:
        return {
            "node_count": len(self.nodes),
            "edge_count": len(self.edges),
            "nodes": list(self.nodes.keys()),
            "edges": list(self.edges)
        }


class VirtualGPU:
    """
    Virtual GPU resource manager and orchestrator.
    Manages registry, allocation, dispatching, synchronization, and observability metrics.
    """

    def __init__(self, vgpu_id: str = "vgpu-0"):
        self.vgpu_id = vgpu_id
        self.fabric = VirtualProcessorFabric()
        self.metrics = {
            "registered_processors": 0,
            "dispatches_count": 0,
            "completed_operations": 0,
            "failed_operations": 0
        }

    def register_processor(self, vnp: VirtualNanoProcessor):
        self.fabric.add_processor(vnp)
        self.metrics["registered_processors"] = len(self.fabric.nodes)

    def unregister_processor(self, vnp_id: str):
        if vnp_id in self.fabric.nodes:
            del self.fabric.nodes[vnp_id]
            self.fabric.edges = [(s, t) for s, t in self.fabric.edges if s != vnp_id and t != vnp_id]
            self.metrics["registered_processors"] = len(self.fabric.nodes)

    def get_processor(self, vnp_id: str) -> Optional[VirtualNanoProcessor]:
        return self.fabric.nodes.get(vnp_id)

    def list_processors(self) -> List[str]:
        return list(self.fabric.nodes.keys())

    def connect_processors(self, src_id: str, tgt_id: str):
        self.fabric.add_connection(src_id, tgt_id)

    def dispatch(self, src_id: str, payload: Any, operation: str = "COMPUTE", tgt_id: Optional[str] = None) -> ExecutionPacket:
        proc = self.get_processor(src_id)
        if not proc:
            raise KeyError(f"Processor {src_id} not registered in VirtualGPU")

        target = tgt_id or src_id
        pkt = ExecutionPacket(
            packet_id=f"pkt-{uuid.uuid4().hex[:8]}",
            source_processor=src_id,
            destination_processor=target,
            operation=operation,
            payload=payload
        )
        proc.receive_packet(pkt)
        self.metrics["dispatches_count"] += 1
        return pkt

    def synchronize(self) -> List[ExecutionPacket]:
        """
        Executes all queued processor inputs across fabric in topological/pipeline order.
        """
        results = []
        active = True

        while active:
            active = False
            for vnp_id, vnp in list(self.fabric.nodes.items()):
                if vnp.input_buffer:
                    active = True
                    try:
                        out_pkt = vnp.execute_next()
                        if out_pkt:
                            results.append(out_pkt)
                            self.metrics["completed_operations"] += 1
                            # Route to downstream processors if connected
                            downstream = self.fabric.get_downstream(vnp_id)
                            for ds_id in downstream:
                                routed_pkt = ExecutionPacket(
                                    packet_id=f"pkt-{uuid.uuid4().hex[:8]}",
                                    source_processor=vnp_id,
                                    destination_processor=ds_id,
                                    operation=out_pkt.operation,
                                    payload=out_pkt.payload
                                )
                                self.fabric.route_packet(routed_pkt)
                    except Exception as e:
                        self.metrics["failed_operations"] += 1
                        raise e

        return results

    def status(self) -> Dict[str, Any]:
        active_count = sum(1 for v in self.fabric.nodes.values() if v.state == VNPState.RUNNING)
        completed_count = sum(1 for v in self.fabric.nodes.values() if v.state == VNPState.COMPLETED)
        error_count = sum(1 for v in self.fabric.nodes.values() if v.state == VNPState.ERROR)

        return {
            "vgpu_id": self.vgpu_id,
            "processor_count": len(self.fabric.nodes),
            "active_processors": active_count,
            "completed_processors": completed_count,
            "error_processors": error_count,
            "metrics": dict(self.metrics),
            "fabric_topology": self.fabric.get_topology_info()
        }
