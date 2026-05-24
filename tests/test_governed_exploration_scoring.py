from runtime.governed_cli.exploration_runtime import (
    GovernedExplorationRuntime,
)


def test_exploration_history_accepts_transition_value():
    runtime = GovernedExplorationRuntime()

    runtime.history.append({
        "transition": {
            "transitions": ["status_transition"],
            "state_changed": True,
        },
        "transition_value": {
            "transition_score": 0.45,
            "manual_review_required": True,
            "autonomous_submission": False,
        },
    })

    replay = runtime.replay_history()

    assert replay["history_size"] == 1
    assert (
        replay["history"][0]
        ["transition_value"]
        ["manual_review_required"]
        is True
    )
