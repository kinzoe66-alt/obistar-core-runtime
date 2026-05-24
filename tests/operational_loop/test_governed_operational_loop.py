from runtime.operational_loop.governed_operational_loop import (
    GovernedOperationalLoop,
)


def test_operational_loop_executes():
    candidates = [
        {
            "candidate_id": "c1",
            "workflow_family": "auth",
            "fatigue_adjusted_priority": 0.9,
        },
        {
            "candidate_id": "c2",
            "workflow_family": "checkout",
            "fatigue_adjusted_priority": 0.6,
        },
    ]

    review_memory = {
        "decision_counts": {
            "useful": 5,
            "duplicate": 1,
        }
    }

    result = (
        GovernedOperationalLoop()
        .execute(
            candidates,
            review_memory,
        )
    )

    assert (
        result["routing"]["route_count"]
        == 2
    )

    assert (
        len(result["packages"])
        == 2
    )

    assert (
        result["export_result"]["exported"]
        is True
    )

    assert (
        result["confirmed_issue"]
        is False
    )


def test_handles_empty_candidates():
    result = (
        GovernedOperationalLoop()
        .execute(
            [],
            {},
        )
    )

    assert (
        result["routing"]["route_count"]
        == 0
    )

    assert (
        len(result["packages"])
        == 0
    )
