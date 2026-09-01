"""
Capability-Aware GPU/CPU Worker Registry Component
"""

import time
from typing import Dict, Any, List, Optional
import torch


class Worker:
    def __init__(
        self,
        worker_id: str,
        provider: str = "local",
        gpu_type: Optional[str] = None,
        vram_mb: int = 0,
        cuda_version: Optional[str] = None,
        capabilities: Optional[List[str]] = None
    ):
        self.worker_id = worker_id
        self.provider = provider
        self.gpu_type = gpu_type or ("CUDA GPU" if torch.cuda.is_available() else "CPU")
        self.vram_mb = vram_mb or (16384 if torch.cuda.is_available() else 8192)
        self.cuda_version = cuda_version or (torch.version.cuda if torch.cuda.is_available() else "None")
        self.capabilities = capabilities or ["cpu", "vnp", "neural"]
        if torch.cuda.is_available():
            self.capabilities.append("gpu")
        self.status = "IDLE"
        self.current_job: Optional[str] = None
        self.quota = 100
        self.heartbeat = time.time()
        self.software_version = "1.0.0"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "worker_id": self.worker_id,
            "provider": self.provider,
            "gpu_type": self.gpu_type,
            "vram_mb": self.vram_mb,
            "cuda_version": self.cuda_version,
            "capabilities": self.capabilities,
            "status": self.status,
            "current_job": self.current_job,
            "quota": self.quota,
            "heartbeat": self.heartbeat,
            "software_version": self.software_version
        }


class WorkerRegistry:
    """
    Registry for managing compute workers (supports scaling from local slice to 30-50 worker pool).
    Supports capability-aware scheduling.
    """

    def __init__(self):
        self.workers: Dict[str, Worker] = {}

    def register_worker(self, worker: Worker):
        self.workers[worker.worker_id] = worker

    def list_workers(self) -> List[Dict[str, Any]]:
        return [w.to_dict() for w in self.workers.values()]

    def find_worker(self, required_capabilities: List[str]) -> Optional[Worker]:
        for w in self.workers.values():
            if w.status == "IDLE" and all(cap in w.capabilities for cap in required_capabilities):
                return w
        return None

    def assign_job(self, worker_id: str, job_id: str) -> bool:
        if worker_id in self.workers:
            w = self.workers[worker_id]
            w.status = "BUSY"
            w.current_job = job_id
            return True
        return False

    def release_worker(self, worker_id: str):
        if worker_id in self.workers:
            w = self.workers[worker_id]
            w.status = "IDLE"
            w.current_job = None
