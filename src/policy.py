from dataclasses import dataclass

@dataclass(frozen=True)
class ActionDecision:
    action: str
    risk: str
    allowed: bool
    requires_approval: bool
    reason: str

LOW_RISK = {"collect_vpn_status", "collect_identity_status", "refresh_vpn_client"}
HIGH_RISK = {"restart_production_service", "change_firewall_rule", "grant_admin", "rotate_credentials"}

def evaluate_action(action: str) -> ActionDecision:
    if action in LOW_RISK:
        return ActionDecision(action, "LOW", True, False, "Explicitly allow-listed low-risk action")
    if action in HIGH_RISK:
        return ActionDecision(action, "HIGH", False, True, "Privileged or production-impacting action requires human approval")
    return ActionDecision(action, "UNKNOWN", False, True, "Unknown actions are denied by default")
