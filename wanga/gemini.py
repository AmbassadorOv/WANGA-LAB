"""
Gemini Adapter Component
"""

import os
import json
from typing import Dict, Any, Optional


class GeminiAdapter:
    """
    Adapter for Google Gemini LLM proposal generation.
    Never hard-codes API keys; uses GEMINI_API_KEY environment variable.
    If unavailable, uses deterministic fallback proposal.
    """

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

    def generate_architecture_proposal(self, prompt: str) -> Dict[str, Any]:
        if not self.api_key:
            # Fallback static test architecture proposal
            return {
                "version": "1.0.0",
                "name": f"Gemini Proposal: {prompt[:30]}",
                "description": "Static fallback proposal (GEMINI_API_KEY not configured)",
                "agents": [
                    {"id": "agent-gemini-1", "name": "Gemini Proposed Agent", "role": "worker"}
                ],
                "neural_components": [
                    {"id": "nc-gemini-1", "architecture_type": "mlp", "input_dim": 8, "output_dim": 4, "hidden_dims": [16], "seed": 42}
                ],
                "virtual_nano_processors": [
                    {"id": "vnp-gemini-1", "registers_count": 8, "memory_size": 256}
                ],
                "experiment": {
                    "id": "exp-gemini-1",
                    "seed": 42,
                    "steps": 10
                }
            }

        # Simulated or actual API client call when GEMINI_API_KEY is available
        # LLMs are untrusted proposal generators; output must pass validation before execution.
        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel("gemini-pro")
            resp = model.generate_content(
                f"Generate a valid WANGA architecture JSON for: {prompt}. Return ONLY valid JSON."
            )
            data = json.loads(resp.text)
            return data
        except Exception as e:
            # Fallback gracefully if external call fails
            fallback = self.generate_architecture_proposal(prompt)
            fallback["description"] = f"Fallback after Gemini API error: {str(e)}"
            return fallback
