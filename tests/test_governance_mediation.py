import unittest

from core.governance_mediation import (
    GovernanceClaim,
    GovernanceMediator,
    MediationState,
)


class GovernanceMediationTests(unittest.TestCase):
    def setUp(self):
        self.mediator = GovernanceMediator()

    def test_common_frame_stabilizes_non_conflicting_inputs(self):
        packet = self.mediator.mediate([
            GovernanceClaim("A", "finance", "same", "e1", "p1"),
            GovernanceClaim("B", "finance", "same", "e2", "p2"),
        ])
        self.assertEqual(packet.state, MediationState.STABILIZED)
        self.assertFalse(packet.common_frame["substantive_resolution"])
        self.assertEqual(packet.common_frame["actors"], ["A", "B"])

    def test_conflict_is_buffered_not_silently_resolved(self):
        packet = self.mediator.mediate([
            GovernanceClaim("A", "finance", "claim-A", "e1", "p1"),
            GovernanceClaim("B", "finance", "claim-B", "e2", "p2"),
        ])
        self.assertEqual(packet.state, MediationState.CONFLICT)
        self.assertEqual(packet.conflicts, (("A", "B"),))

    def test_digest_is_deterministic(self):
        claims = [
            GovernanceClaim("B", "x", "two", "e2", "p2"),
            GovernanceClaim("A", "x", "one", "e1", "p1"),
        ]
        self.assertEqual(
            self.mediator.mediate(claims).integrity_sha256,
            self.mediator.mediate(list(reversed(claims))).integrity_sha256,
        )

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            self.mediator.mediate([])
