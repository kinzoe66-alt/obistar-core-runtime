from runtime.human_language.workflow_names import human_workflow_name
from runtime.human_language.deliverable_language import humanize_deliverable

def test_human_workflow_name():
    assert human_workflow_name("session_workflow") == "session continuity review"

def test_humanize_deliverable():
    result = humanize_deliverable({
        "surface_id": "surface-001",
        "workflow_family": "session_workflow",
        "status": "manual_review_required",
        "what_evidence_to_collect": [
            "Timestamp of review attempt."
        ]
    })

    assert result["title"] == "Session Continuity Review"
    assert result["confirmed_issue"] is False
    assert result["manual_review_required"] is True
