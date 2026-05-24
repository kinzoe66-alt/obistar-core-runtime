from runtime.governed_scoring.cross_program_weighting import (
    CrossProgramAdaptiveWeighting,
)


def test_cross_program_weighting_adjusts_by_outcomes():
    result = CrossProgramAdaptiveWeighting().weight([
        {
            "program_id": "p1",
            "base_score": 0.5,
            "accepted_count": 2,
            "rejected_count": 1,
        }
    ])

    assert result["program_weights"][0]["adjusted_score"] == 0.55
