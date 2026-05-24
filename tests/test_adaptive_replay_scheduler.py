from runtime.governed_scoring.adaptive_replay_scheduler import (
    AdaptiveReplayScheduler,
)


def test_stable_replay_reduces_runs():
    result = AdaptiveReplayScheduler().schedule({
        "success_rate": 1.0
    })

    assert result["replay_runs"] == 2


def test_unstable_replay_increases_runs():
    result = AdaptiveReplayScheduler().schedule({
        "success_rate": 0.25
    })

    assert result["replay_runs"] == 7
