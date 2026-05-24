from runtime.governed_scoring.reviewer_calibration import (
    ReviewerCalibrationPersistence,
)


def test_reviewer_calibration_round_trip(tmp_path):
    path = tmp_path / "calibration.json"

    persistence = ReviewerCalibrationPersistence()

    persistence.write(
        {"accepted_for_review": 2},
        path=str(path),
    )

    result = persistence.read(
        path=str(path)
    )

    assert result["calibration"]["accepted_for_review"] == 2
    assert result["manual_review_required"] is True
