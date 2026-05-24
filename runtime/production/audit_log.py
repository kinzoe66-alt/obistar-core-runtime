from datetime import UTC, datetime

def build_audit_event(event_type, tenant_id, details):
    return {
        "event_type": event_type,
        "tenant_id": tenant_id,
        "details": details,
        "timestamp": datetime.now(UTC).isoformat(),
        "manual_review_required": True
    }
