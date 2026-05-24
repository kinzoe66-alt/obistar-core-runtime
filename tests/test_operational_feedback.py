import json

from runtime.operations.feedback import OperationalFeedbackBuilder

def test_operational_feedback(tmp_path):
    scope = tmp_path / "scope.json"
    scope.write_text(json.dumps([
        {
            "surface_id": "authorized-surface-001",
            "program": "governed_program",
            "authorized_scope": True,
            "validation_surface": "api"
        }
    ]), encoding="utf-8")

    result = OperationalFeedbackBuilder().build(str(scope))

    assert result["readiness"]["ready"] is True
    assert result["evidence_quality"]["classification"] == "strong"
    assert result["remediation_quality"]["classification"] == "strong"
