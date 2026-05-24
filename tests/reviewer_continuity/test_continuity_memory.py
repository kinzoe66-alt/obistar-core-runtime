from runtime.reviewer_continuity.continuity_memory import (
    ReviewerContinuityMemory,
)


def test_builds_workflow_history():
    routes = [
        {"workflow_family": "auth"},
        {"workflow_family": "auth"},
        {"workflow_family": "checkout"},
    ]

    result = ReviewerContinuityMemory().build(
        routes
    )

    assert (
        result["workflow_history"]["auth"]
        == 2
    )

    assert (
        result["workflow_history"]["checkout"]
        == 1
    )

    assert (
        result["workflow_family_count"]
        == 2
    )

    assert (
        result["confirmed_issue"]
        is False
    )


def test_continuity_score_exists():
    routes = [
        {"workflow_family": "auth"},
        {"workflow_family": "checkout"},
    ]

    result = ReviewerContinuityMemory().build(
        routes
    )

    assert (
        result["continuity_score"]
        > 0
    )


def test_handles_empty_routes():
    result = ReviewerContinuityMemory().build([])

    assert (
        result["workflow_family_count"]
        == 0
    )

    assert (
        result["continuity_score"]
        == 0
    )
