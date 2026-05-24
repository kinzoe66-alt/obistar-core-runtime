from runtime.deduplication.deduplication_scorer import DeduplicationScorer

def test_deduplication_scorer_duplicate():
    scorer = DeduplicationScorer()

    current = {
        "surface_type": "state_transition",
        "validation_surface": "api",
        "issue_class": "governed_validation_observation",
        "workflow": "governed_validation_workflow",
        "cognition_focus": ["transition_ordering"]
    }

    prior = {
        "surface_type": "state_transition",
        "validation_surface": "api",
        "issue_class": "governed_validation_observation",
        "workflow": "governed_validation_workflow",
        "cognition_focus": ["transition_ordering"]
    }

    result = scorer.compare(current, prior)

    assert result["classification"] == "duplicate"
    assert result["autonomous_rejection"] is False
