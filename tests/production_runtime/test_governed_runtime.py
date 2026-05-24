from runtime.production_runtime.governed_runtime import (
    GovernedProductionRuntime,
)


def test_governed_runtime_executes(
    tmp_path
):
    candidates = tmp_path / "candidates.json"

    review_memory = (
        tmp_path /
        "review_memory.json"
    )

    candidates.write_text(
        """
[
  {
    "candidate_id": "c1",
    "workflow_family": "auth",
    "fatigue_adjusted_priority": 0.9
  }
]
"""
    )

    review_memory.write_text(
        """
{
  "decision_counts": {
    "useful": 5
  }
}
"""
    )

    result = (
        GovernedProductionRuntime()
        .run(
            candidates,
            review_memory,
        )
    )

    assert (
        result["runtime_completed"]
        is True
    )

    assert (
        result["candidate_count"]
        == 1
    )

    assert (
        result["confirmed_issue"]
        is False
    )
