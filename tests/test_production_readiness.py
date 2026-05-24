from runtime.production.audit_log import build_audit_event
from runtime.production.customer_safety import governed_customer_safety
from runtime.production.replay_retention import replay_retention_policy
from runtime.production.control_plane import control_plane_status

def test_audit_event():
    result = build_audit_event(
        "review_queue_created",
        "tenant-001",
        {"count": 3}
    )

    assert result["event_type"] == "review_queue_created"

def test_customer_safety():
    result = governed_customer_safety(
        observation_count=5,
        unstable_count=0
    )

    assert result["customer_safe"] is True

def test_retention_policy():
    result = replay_retention_policy(90)

    assert result["retention_tier"] == "operational"

def test_control_plane_status():
    result = control_plane_status(
        tests_passing=True,
        onboarding_ready=True,
        monetization_ready=True
    )

    assert result["platform_operational"] is True
