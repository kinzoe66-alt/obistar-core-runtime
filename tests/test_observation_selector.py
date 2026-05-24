from runtime.observations.selector import ObservationSelector

def test_observation_selector():
    result = ObservationSelector().select()

    assert result["selected_count"] == 3
    assert result["ordered_observations"]
    assert result["manual_review_required"] is True
