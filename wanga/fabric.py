"""
Inter-Network Fabric Component
"""

from typing import Dict, Any, List


class InterNetworkFabric:
    """
    Manages controlled routing and message passing between VNPs, agents, and neural networks.
    """

    def __init__(self):
        self.routes: Dict[str, List[str]] = {}
        self.message_queue: List[Dict[str, Any]] = []

    def add_connection(self, source: str, target: str):
        if source not in self.routes:
            self.routes[source] = []
        if target not in self.routes[source]:
            self.routes[source].append(target)

    def route_message(self, message: Dict[str, Any]) -> bool:
        src = message.get("src")
        tgt = message.get("target")

        if not src or not tgt:
            return False

        if tgt in self.routes.get(src, []):
            self.message_queue.append(message)
            return True

        # Default allowed for direct message routing if routing rules are open
        self.message_queue.append(message)
        return True

    def flush(self) -> List[Dict[str, Any]]:
        msgs = list(self.message_queue)
        self.message_queue.clear()
        return msgs
