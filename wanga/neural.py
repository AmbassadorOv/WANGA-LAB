"""
Neural Lab PyTorch Component
"""

import hashlib
from typing import Dict, Any, List, Optional
import torch
import torch.nn as nn
import torch.optim as optim


class NeuralModule(nn.Module):
    def __init__(self, input_dim: int, output_dim: int, hidden_dims: List[int]):
        super().__init__()
        layers = []
        prev_dim = input_dim
        for h in hidden_dims:
            layers.append(nn.Linear(prev_dim, h))
            layers.append(nn.ReLU())
            prev_dim = h
        layers.append(nn.Linear(prev_dim, output_dim))
        self.model = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)


class NeuralLabComponent:
    """
    Neural Lab component utilizing PyTorch.
    Supports CPU/GPU execution, deterministic seed setting, metric recording, and state checkpoints.
    """

    def __init__(
        self,
        component_id: str,
        input_dim: int = 8,
        output_dim: int = 4,
        hidden_dims: Optional[List[int]] = None,
        learning_rate: float = 0.01,
        device: str = "cpu",
        seed: Optional[int] = 42
    ):
        self.component_id = component_id
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dims = hidden_dims or [16, 16]
        self.learning_rate = learning_rate
        self.device_str = device if (device == "cuda" and torch.cuda.is_available()) else "cpu"
        self.device = torch.device(self.device_str)

        if seed is not None:
            self.set_seed(seed)

        self.net = NeuralModule(self.input_dim, self.output_dim, self.hidden_dims).to(self.device)
        self.optimizer = optim.Adam(self.net.parameters(), lr=self.learning_rate)
        self.loss_fn = nn.MSELoss()
        self.metrics: Dict[str, Any] = {}

    def set_seed(self, seed: int):
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)

    def run_step(self, x_data: Optional[List[float]] = None, y_data: Optional[List[float]] = None) -> float:
        self.net.train()
        if x_data is None:
            x_tensor = torch.randn(1, self.input_dim, device=self.device)
        else:
            x_tensor = torch.tensor([x_data], dtype=torch.float32, device=self.device)

        if y_data is None:
            y_tensor = torch.ones(1, self.output_dim, device=self.device)
        else:
            y_tensor = torch.tensor([y_data], dtype=torch.float32, device=self.device)

        self.optimizer.zero_grad()
        output = self.net(x_tensor)
        loss = self.loss_fn(output, y_tensor)
        loss.backward()
        self.optimizer.step()

        loss_val = float(loss.item())
        self.metrics["last_loss"] = loss_val
        self.metrics["output_sample"] = output.detach().cpu().numpy().tolist()[0]
        return loss_val

    def get_state(self) -> Dict[str, Any]:
        return {
            "component_id": self.component_id,
            "metrics": self.metrics,
            "device": self.device_str,
            "input_dim": self.input_dim,
            "output_dim": self.output_dim
        }

    def compute_sha256(self) -> str:
        weights_bytes = b""
        for param in self.net.parameters():
            weights_bytes += param.detach().cpu().numpy().tobytes()
        return hashlib.sha256(weights_bytes).hexdigest()
