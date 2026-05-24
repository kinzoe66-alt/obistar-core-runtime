from runtime.governed_cli.exploration_runtime import (
    GovernedExplorationRuntime
)


def test_full_governed_scoring_pipeline():

    runtime = (
        GovernedExplorationRuntime()
    )

    runtime.history.append({
        "transition_value": {
            "transition_score": 0.9
        }
    })

    replay = runtime.replay_history()

    assert (
        replay["adaptive_branches"]
        ["selection_count"]
        == 1
    )

    assert (
        replay["replay_escalation"]
        ["escalated"][0]
        ["replay_runs"]
        == 5
    )

    assert (
        replay["replay_weighting"]
        ["weighted"][0]
        ["replay_weight"]
        == 1.0
    )

    assert (
        replay["evidence_escalation"]
        ["evidence_escalation"][0]
        ["evidence_level"]
        == "deep_validation"
    )
