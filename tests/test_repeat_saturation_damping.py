from runtime.economic_diversity.repeat_saturation import repeat_saturation_penalty
from runtime.economic_diversity.diverse_selector import select_diverse_candidates

def test_repeat_saturation_penalty_detects_repetition():
    result = repeat_saturation_penalty(
        {
            "surface_id": "parent-001::session_workflow::2",
            "workflow_family": "session_workflow"
        },
        {"session_workflow": 2},
        {"parent-001": 2}
    )

    assert result["repeat_saturation_state"] == "saturated"

def test_diverse_selector_suppresses_repetitive_candidates():
    candidates = [
        {
            "surface_id": "parent-001::session_workflow::1",
            "workflow_family": "session_workflow",
            "priority": {"score": 0.89},
            "outcome_learning": {"score": 1.1},
            "replay_stability": {"score": 1.0}
        },
        {
            "surface_id": "parent-001::session_workflow::2",
            "workflow_family": "session_workflow",
            "priority": {"score": 0.89},
            "outcome_learning": {"score": 1.1},
            "replay_stability": {"score": 1.0}
        },
        {
            "surface_id": "parent-002::authentication_workflow::3",
            "workflow_family": "authentication_workflow",
            "priority": {"score": 0.89},
            "outcome_learning": {"score": 1.1},
            "replay_stability": {"score": 1.0}
        }
    ]

    result = select_diverse_candidates(candidates, limit=3)

    selected_ids = [
        item["surface_id"]
        for item in result["selected_candidates"]
    ]

    assert "parent-001::session_workflow::1" in selected_ids
    assert "parent-001::session_workflow::2" not in selected_ids
    assert "parent-002::authentication_workflow::3" in selected_ids
