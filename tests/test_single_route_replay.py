from runtime.governed_replay.single_route import (
    SingleRouteReplayExecutor,
)


def test_single_route_replay_generates_reviewer_artifact(tmp_path):

    output = (
        tmp_path
        / "single_route_replay.json"
    )

    candidate = {
        "observation_id": (
            "candidate_001"
        ),

        "surface_id": (
            "surface_001"
        ),
    }

    artifact = (
        SingleRouteReplayExecutor()
        .run(
            candidate=candidate,
            output_path=str(output),
        )
    )

    assert (
        artifact["candidate_id"]
        == "candidate_001"
    )

    assert (
        artifact["deterministic"]
        is True
    )

    assert (
        artifact["reproducible"]
        is True
    )

    assert (
        artifact[
            "manual_review_required"
        ]
        is True
    )

    assert (
        artifact[
            "autonomous_submission"
        ]
        is False
    )

    assert output.exists()
