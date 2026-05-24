from runtime.economic_diversity.novelty_score import novelty_score
from runtime.economic_diversity.diverse_selector import select_diverse_candidates
from runtime.economic_diversity.diversity_metrics import diversity_metrics

def test_novelty_score_detects_new_family_and_parent():
    result = novelty_score(
        {
            "surface_id": "parent-001::authentication_workflow::1",
            "workflow_family": "authentication_workflow"
        },
        set(),
        set()
    )

    assert result["novelty_classification"] == "novel"

def test_diverse_selector_prioritizes_novel_candidates():
    candidates = [
        {
            "surface_id": "parent-001::authentication_workflow::1",
            "workflow_family": "authentication_workflow",
            "priority": {"score": 0.89},
            "outcome_learning": {"score": 1.1},
            "replay_stability": {"score": 1.0}
        },
        {
            "surface_id": "parent-001::authentication_workflow::2",
            "workflow_family": "authentication_workflow",
            "priority": {"score": 0.89},
            "outcome_learning": {"score": 1.1},
            "replay_stability": {"score": 1.0}
        },
        {
            "surface_id": "parent-002::session_workflow::3",
            "workflow_family": "session_workflow",
            "priority": {"score": 0.89},
            "outcome_learning": {"score": 1.1},
            "replay_stability": {"score": 1.0}
        }
    ]

    result = select_diverse_candidates(candidates, limit=2)

    assert result["selected_count"] == 2
    assert len({item["workflow_family"] for item in result["selected_candidates"]}) == 2

def test_diversity_metrics():
    result = diversity_metrics([
        {
            "surface_id": "parent-001::authentication_workflow::1",
            "workflow_family": "authentication_workflow"
        },
        {
            "surface_id": "parent-002::session_workflow::2",
            "workflow_family": "session_workflow"
        }
    ])

    assert result["unique_workflow_families"] == 2
    assert result["unique_parent_surfaces"] == 2
