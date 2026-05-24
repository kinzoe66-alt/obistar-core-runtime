from runtime.deliverables.report_deliverable import (
    DeliverableValidator
)

def test_report_deliverable():

    result = (
        DeliverableValidator()
        .validate({
            "professional_label": True,
            "simplified_summary": True,
            "affected_surface": True,
            "validation_conditions": True,
            "replay_steps": True,
            "evidence_summary": True,
            "remediation_guidance": True,
            "confidence_rationale": True
        })
    )

    assert result["valid"] is True
