from runtime.outcomes.outcome_tracker import OutcomeTracker

def test_outcome_tracker(tmp_path):
    path = tmp_path / "outcomes.json"

    result = OutcomeTracker().write(
        "surface-001",
        "accepted",
        str(path)
    )

    assert result["surface_id"] == "surface-001"
    assert path.exists()
