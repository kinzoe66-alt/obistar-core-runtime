from runtime.confidence_drift.drift_detector import (
    ConfidenceDriftDetector,
)


def test_detects_confidence_drift():
    history = [
        0.91,
        0.88,
        0.52,
    ]

    result = ConfidenceDriftDetector().detect(
        history
    )

    assert result["drift_detected"] is True
    assert result["drift_delta"] == 0.39
    assert result["confirmed_issue"] is False


def test_detects_stable_confidence():
    history = [
        0.91,
        0.89,
        0.9,
    ]

    result = ConfidenceDriftDetector().detect(
        history
    )

    assert result["drift_detected"] is False


def test_handles_small_history():
    result = ConfidenceDriftDetector().detect(
        [0.91]
    )

    assert result["drift_detected"] is False
    assert result["history_size"] == 1
