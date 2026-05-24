from runtime.governed_scoring.replay_weighting import (
    ReplayWeightingEngine
)


def test_high_replay_weight():

    engine = (
        ReplayWeightingEngine()
    )

    result = engine.weight({
        "escalated": [
            {
                "priority": "high",
                "replay_runs": 5,
            }
        ]
    })

    assert (
        result["weighted"][0]
        ["replay_weight"]
        == 1.0
    )


def test_medium_replay_weight():

    engine = (
        ReplayWeightingEngine()
    )

    result = engine.weight({
        "escalated": [
            {
                "priority": "medium",
                "replay_runs": 3,
            }
        ]
    })

    assert (
        result["weighted"][0]
        ["replay_weight"]
        == 0.6
    )
