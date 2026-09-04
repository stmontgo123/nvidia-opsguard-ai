from .policy import evaluate_action
from .tools import collect_vpn_status, collect_identity_status, refresh_vpn_client
from .audit import record

APPROVED_RUNBOOK = {
    "title": "VPN-101 Stale Session Recovery",
    "status": "APPROVED",
    "steps": [
        "Confirm gateway health",
        "Confirm identity and MFA status",
        "Refresh the local VPN client session",
        "Escalate if connectivity is not restored",
    ],
}

def investigate_vpn_incident() -> dict:
    evidence = {
        "vpn": collect_vpn_status(),
        "identity": collect_identity_status(),
        "runbook": APPROVED_RUNBOOK,
    }
    record("EVIDENCE_COLLECTED", evidence)

    probable_cause = "Stale local VPN client session"
    recommendation = "Refresh the VPN client session and retest connectivity"
    action = "refresh_vpn_client"
    decision = evaluate_action(action)
    record("ACTION_EVALUATED", decision.__dict__)

    execution = None
    if decision.allowed and not decision.requires_approval:
        execution = refresh_vpn_client()
        record("ACTION_EXECUTED", {"action": action, "result": execution})

    return {
        "evidence": evidence,
        "probable_cause": probable_cause,
        "recommendation": recommendation,
        "policy_decision": decision.__dict__,
        "execution": execution,
    }
