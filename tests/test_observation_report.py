from runtime.observations.report import ObservationSelectionReport

def test_observation_report(tmp_path):
    out = tmp_path / "observations.json"

    path = ObservationSelectionReport().write(str(out))

    assert path.exists()
