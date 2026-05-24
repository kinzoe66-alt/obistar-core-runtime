from runtime.review_routing.route_optimizer import (
    ReviewRouteOptimizer,
)


def test_routes_are_prioritized():
    candidates = [
        {
            "candidate_id": "c1",
            "workflow_family": "auth",
            "fatigue_adjusted_priority": 0.4,
        },
        {
            "candidate_id": "c2",
            "workflow_family": "checkout",
            "fatigue_adjusted_priority": 0.9,
        },
    ]

    result = ReviewRouteOptimizer().optimize(
        candidates
    )

    assert result["route_count"] == 2

    assert (
        result["routes"][0]["candidate_id"]
        == "c2"
    )

    assert (
        result["routes"][1]["candidate_id"]
        == "c1"
    )

    assert (
        result["confirmed_issue"]
        is False
    )


def test_handles_empty_candidates():
    result = ReviewRouteOptimizer().optimize([])

    assert result["route_count"] == 0


def test_route_positions_are_sequential():
    candidates = [
        {
            "candidate_id": "c1",
            "fatigue_adjusted_priority": 0.7,
        },
        {
            "candidate_id": "c2",
            "fatigue_adjusted_priority": 0.6,
        },
        {
            "candidate_id": "c3",
            "fatigue_adjusted_priority": 0.5,
        },
    ]

    result = ReviewRouteOptimizer().optimize(
        candidates
    )

    assert (
        result["routes"][0]["route_position"]
        == 1
    )

    assert (
        result["routes"][1]["route_position"]
        == 2
    )

    assert (
        result["routes"][2]["route_position"]
        == 3
    )
