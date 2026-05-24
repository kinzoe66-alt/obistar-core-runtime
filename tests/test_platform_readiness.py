from runtime.platform.tenant_isolation import isolate_tenant_scope
from runtime.platform.reviewer_workflow import reviewer_workflow_state
from runtime.platform.onboarding_readiness import onboarding_readiness

def test_tenant_isolation():
    result = isolate_tenant_scope(
        "tenant-001",
        [{"id": "OBS-001"}]
    )

    assert result["cross_tenant_leakage_detected"] is False

def test_reviewer_workflow():
    result = reviewer_workflow_state({
        "replay_history_strength": "stable",
        "confidence_drift_status": "stable"
    })

    assert result["workflow_state"] == "ready_for_manual_review"

def test_onboarding_readiness():
    result = onboarding_readiness({
        "replay_quality": 0.9,
        "reviewer_signal_quality": 0.9
    })

    assert result["onboarding_ready"] is True
