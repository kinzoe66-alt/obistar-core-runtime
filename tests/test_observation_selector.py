from runtime.observations.selector import ObservationSelector

def test_observation_selector():
    result = ObservationSelector().select(
        "test_scopes/sample_surfaces.json"
    )

    assert result["selected_count"] == 3
    assert result["ordered_observations"]
    assert result["manual_review_required"] is True
