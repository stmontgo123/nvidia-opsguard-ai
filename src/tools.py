SYNTHETIC_STATE = {
    "vpn_gateway": "healthy",
    "user_identity": "active",
    "mfa": "valid",
    "vpn_client": "stale_session",
    "last_successful_login": "2026-09-03T13:21:00Z",
}

def collect_vpn_status() -> dict:
    return {"vpn_gateway": SYNTHETIC_STATE["vpn_gateway"], "vpn_client": SYNTHETIC_STATE["vpn_client"]}

def collect_identity_status() -> dict:
    return {"user_identity": SYNTHETIC_STATE["user_identity"], "mfa": SYNTHETIC_STATE["mfa"]}

def refresh_vpn_client() -> dict:
    SYNTHETIC_STATE["vpn_client"] = "refreshed"
    return {"status": "completed", "vpn_client": "refreshed"}
