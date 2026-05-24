from runtime.governed_replay.replay_route_runner import (
    GovernedReplayRouteRunner
)


def test_governed_replay_route_runner_executes():

    result = (
        GovernedReplayRouteRunner()
        .run()
    )

    assert (
        result["package"]
        ["reviewer_ready"]
        is True
    )

    assert (
        result["replay"]
        ["reproducible"]
        is True
    )

    assert (
        result[
            "manual_review_required"
        ]
        is True
    )
