from runtime.taxonomy.issue_classifier import IssueClassifier

def test_issue_classifier_professional_label():
    result = IssueClassifier().classify("workflow_state_transition")

    assert result["known"] is True
    assert result["label"] == "Workflow State Transition Issue"
    assert result["manual_review_required"] is True
