from runtime.governed_cli.exploration_runtime import (
    GovernedExplorationRuntime
)


def test_exploration_runtime_generates_branches():

    runtime = (
        GovernedExplorationRuntime()
    )

    runtime.history.append({
        "transition_value": {
            "transition_score": 0.8
        }
    })

    replay = runtime.replay_history()

    assert (
        replay["adaptive_branches"]
        ["selection_count"]
        == 1
    )

    assert (
        replay["adaptive_branches"]
        ["selected"][0]
        ["priority"]
        == "high"
    )
