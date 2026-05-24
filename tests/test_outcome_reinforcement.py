from runtime.outcome_intelligence.reviewer_outcomes import reviewer_outcomes
from runtime.outcome_intelligence.evidence_learning import evidence_learning
from runtime.outcome_intelligence.reviewer_alignment import reviewer_alignment
from runtime.outcome_intelligence.economic_reinforcement import economic_reinforcement

def test_reviewer_outcomes():
    result = reviewer_outcomes([
        {"review_outcome": "accepted"},
        {"review_outcome": "accepted"},
        {"review_outcome": "rejected"}
    ])

    assert result["reviewer_acceptance_ratio"] == 0.6667

def test_evidence_learning():
    result = evidence_learning([
        {"replay_success_rate": 0.9},
        {"replay_success_rate": 0.8},
        {"replay_success_rate": 0.95}
    ])

    assert result["evidence_learning_strength"] == "strong"

def test_reviewer_alignment():
    result = reviewer_alignment(
        acceptance_ratio=0.8,
        reviewer_clarity=0.8
    )

    assert result["reviewer_alignment_strength"] == "high"

def test_economic_reinforcement():
    result = economic_reinforcement(
        reviewer_alignment_score=0.8,
        throughput_quality=0.8
    )

    assert result["economic_reinforcement_strength"] == "high"
