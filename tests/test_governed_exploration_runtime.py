from runtime.governed_cli.exploration_runtime import (
    GovernedExplorationRuntime
)


def test_exploration_runtime_tracks_history():

    runtime = (
        GovernedExplorationRuntime()
    )

    runtime.history.append({
        "transition": {
            "state_changed": False
        },

        "transition_value": {
            "transition_score": 0.0
        }
    })

    replay = runtime.replay_history()

    assert (
        replay["history_size"]
        == 1
    )

    assert (
        replay["manual_review_required"]
        is True
    )
