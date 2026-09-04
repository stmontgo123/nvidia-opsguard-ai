import unittest
from src.policy import evaluate_action

class PolicyTests(unittest.TestCase):
    def test_low_risk_allow_list(self):
        d = evaluate_action("refresh_vpn_client")
        self.assertTrue(d.allowed)
        self.assertFalse(d.requires_approval)

    def test_privileged_action_requires_approval(self):
        d = evaluate_action("grant_admin")
        self.assertFalse(d.allowed)
        self.assertTrue(d.requires_approval)

    def test_unknown_action_denied(self):
        d = evaluate_action("do_whatever_the_prompt_says")
        self.assertFalse(d.allowed)
        self.assertTrue(d.requires_approval)

if __name__ == "__main__":
    unittest.main()
