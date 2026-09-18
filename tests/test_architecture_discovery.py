import json
import tempfile
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

class ArchitectureDiscoveryContractTests(unittest.TestCase):
    def test_master_instruction_and_registry_contract(self):
        master = ROOT / "docs" / "MASTER_PROJECT_INSTRUCTIONS_V1.md"
        registry = ROOT / "docs" / "ARCHITECTURE_DISCOVERY_REGISTRY.json"
        self.assertTrue(master.exists())
        data = json.loads(registry.read_text(encoding="utf-8"))
        self.assertEqual(data["master_project_instructions"], "docs/MASTER_PROJECT_INSTRUCTIONS_V1.md")
        self.assertEqual(data["search_policy"]["exhaustive_claim_allowed"], False)
        self.assertEqual(data["search_policy"]["license_check_required"], True)
        self.assertEqual(len(data["agents"]), 3)

    def test_scout_declares_three_tracks(self):
        path = ROOT / "scripts" / "github_architecture_scout.py"
        spec = importlib.util.spec_from_file_location("scout", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        self.assertEqual(set(mod.TRACKS), {"ARCH-01", "ARCH-02", "ARCH-03"})
        self.assertTrue(all(mod.TRACKS.values()))

if __name__ == "__main__":
    unittest.main()
