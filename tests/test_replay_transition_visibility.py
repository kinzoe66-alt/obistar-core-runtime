from runtime.governed_replay.replay_transition_visibility import (
    ReplayTransitionVisibility
)


def test_transition_visibility_preserves_execution():

    sequence = [
        {
            "step": 1,
            "command": [
                "python",
                "--version"
            ],
            "returncode": 0,
        }
    ]

    augmented = (
        ReplayTransitionVisibility()
        .augment(
            sequence,
            candidate_id="obs_001",
            surface_id="surface_001",
        )
    )

    assert (
        augmented[0]["transition"]
        == "candidate_ingest"
    )

    assert (
        augmented[0]["result"]
        == "validated"
    )

    assert (
        augmented[0]["execution"]
        == sequence[0]
    )


def test_transition_visibility_empty_sequence():

    augmented = (
        ReplayTransitionVisibility()
        .augment([])
    )

    assert len(augmented) == 1

    assert (
        augmented[0]["execution"]
        is None
    )
