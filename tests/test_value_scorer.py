from runtime.value.value_scorer import ValueScorer

def test_value_scorer_high_value_candidate():
    result = ValueScorer().score({
        "replay_stable": True,
        "evidence_complete": True,
        "state_lineage_present": True,
        "authorization_boundary_relevant": True,
        "business_workflow_relevant": True,
        "manual_review": True,
        "evidence": {
            "replay_trace": {},
            "evidence_bundle": {},
            "state_lineage": {},
            "boundary_context": {},
            "workflow_context": {}
        }
    })

    assert result["classification"] == "high_value_candidate"
    assert result["score"] == 1.0

def test_value_scorer_rejects_missing_replay():
    result = ValueScorer().score({
        "replay_stable": False,
        "evidence_complete": True,
        "manual_review": True,
        "evidence": {
            "evidence_bundle": {}
        }
    })

    assert result["classification"] == "rejected"
