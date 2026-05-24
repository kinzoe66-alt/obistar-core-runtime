from runtime.adjudication_packages.package_builder import (
    AdjudicationPackageBuilder,
)


def test_builds_adjudication_package():
    candidate = {
        "candidate_id": "c1",
        "workflow_family": "auth",
        "fatigue_adjusted_priority": 0.82,
    }

    review_memory = {
        "decision_counts": {
            "useful": 5,
        }
    }

    continuity_memory = {
        "continuity_score": 1.5,
    }

    result = (
        AdjudicationPackageBuilder()
        .build(
            candidate,
            review_memory,
            continuity_memory,
        )
    )

    assert result["candidate_id"] == "c1"

    assert (
        result["workflow_family"]
        == "auth"
    )

    assert (
        result["priority"]
        == 0.82
    )

    assert (
        result["manual_review_required"]
        is True
    )

    assert (
        result["confirmed_issue"]
        is False
    )


def test_handles_missing_candidate_fields():
    result = (
        AdjudicationPackageBuilder()
        .build(
            {},
            {},
            {},
        )
    )

    assert (
        result["candidate_id"]
        == "unknown"
    )

    assert (
        result["workflow_family"]
        == "unknown"
    )
