from runtime.reviewer_playbooks.playbook_builder import build_reviewer_playbook

def test_reviewer_playbook_builder():
    playbook = build_reviewer_playbook({
        "surface_id": "surface-001",
        "workflow_family": "session_workflow"
    })

    assert playbook["manual_review_required"] is True
    assert playbook["autonomous_submission"] is False
    assert len(playbook["manual_steps"]) > 0
