from runtime.reviewer_deliverables.deliverable_builder import (
    build_reviewer_deliverable
)

def test_reviewer_deliverable_builder():

    deliverable = build_reviewer_deliverable(
        {
            "surface_id": "surface-001",
            "workflow_family": "session_workflow"
        },
        {
            "manual_steps": [
                "Open the authorized surface.",
                "Repeat the workflow."
            ]
        }
    )

    assert deliverable["confirmed_issue"] is False
    assert deliverable["autonomous_submission"] is False
    assert deliverable["status"] == "manual_review_required"
    assert len(deliverable["how_to_reproduce"]) == 2
