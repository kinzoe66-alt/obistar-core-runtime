from runtime.outcome_weighting.history_loader import load_weighting_history
from runtime.outcome_weighting.workflow_weighting import workflow_weight
from runtime.outcome_weighting.evidence_history import evidence_history_weight
from runtime.outcome_weighting.outcome_weighted_priority import outcome_weighted_priority
from runtime.outcome_weighting.weighting_table import build_weighting_table

def test_weighting_history_loader():
    histories = load_weighting_history("outcome_history/governed_weighting.sample.json")
    assert len(histories) == 3

def test_workflow_weighting_strong():
    result = workflow_weight({
        "workflow_family": "session_workflow",
        "replay_success_rate": 0.95,
        "reviewer_acceptance_rate": 0.81,
        "evidence_strength": 0.91
    })

    assert result["workflow_weight_classification"] == "strong_weight"

def test_evidence_history_weight():
    result = evidence_history_weight(0.88)
    assert result["evidence_history_classification"] == "strong_evidence_history"

def test_outcome_weighted_priority():
    result = outcome_weighted_priority(
        {
            "review_priority": {"score": 0.75},
            "outcome_learning": {"score": 1.0}
        },
        workflow_weight_score=0.85,
        evidence_history_score=0.88
    )

    assert result["weighted_priority_classification"] == "priority_review"

def test_weighting_table():
    table = build_weighting_table("outcome_history/governed_weighting.sample.json")
    assert "session_workflow" in table
