from runtime.governed_replay.replay_package import (
    ReplayRoutePackager
)


def test_replay_route_package_builds():

    package = (
        ReplayRoutePackager()
        .build(
            candidate={
                "observation_id": (
                    "obs_001"
                )
            },

            replay_artifact={
                "candidate_id": (
                    "obs_001"
                ),

                "surface_id": (
                    "surface_001"
                ),

                "replay_sequence": [],

                "reproducible": True,

                "deterministic": True,

                "stdout": "ok",

                "stderr": "",
            },
        )
    )

    assert (
        package["reviewer_ready"]
        is True
    )

    assert (
        package["reproducible"]
        is True
    )

    assert (
        package["manual_review_required"]
        is True
    )
