from runtime.governed_scoring.transition_value import (
    TransitionValueScorer,
)


def test_stable_state_scores_zero():
    result = TransitionValueScorer().score({
        "transitions": ["stable_state"],
        "state_changed": False,
    })

    assert result["transition_score"] == 0.0
    assert result["evidence_value"] == "none"
    assert result["adjudication_escalation"] is False
    assert result["manual_review_required"] is True


def test_changed_transition_scores_for_review():
    result = TransitionValueScorer().score({
        "transitions": [
            "status_transition",
            "reflection_transition",
        ],
        "state_changed": True,
    })

    assert result["transition_score"] >= 0.5
    assert result["evidence_value"] in {
        "medium",
        "high",
    }
    assert result["replay_weight"] >= 2
    assert result["adjudication_escalation"] is True
    assert result["autonomous_submission"] is False
