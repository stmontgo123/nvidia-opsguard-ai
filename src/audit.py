from datetime import datetime, timezone

AUDIT_EVENTS = []

def record(event_type: str, details: dict) -> dict:
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "details": details,
    }
    AUDIT_EVENTS.append(event)
    return event
