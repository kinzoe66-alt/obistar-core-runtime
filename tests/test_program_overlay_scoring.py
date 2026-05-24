from runtime.governed_scoring.program_overlay_scoring import (
    ProgramSpecificScoringOverlay,
)


def test_overlay_multiplier_adjusts_score():
    result = ProgramSpecificScoringOverlay().apply(
        0.5,
        {"priority_multiplier": 1.5},
    )

    assert result["adjusted_score"] == 0.75
    assert result["overlay_applied"] is True
