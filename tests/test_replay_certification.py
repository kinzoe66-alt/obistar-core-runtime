from runtime.certification.replay_certification import (
    ReplayCertificationBuilder
)

def test_replay_certification():

    artifact = (
        ReplayCertificationBuilder()
        .build()
    )

    assert artifact["certified"] is True

    assert (
        "activation_record"
        in artifact
    )

    assert (
        "authority_snapshot"
        in artifact
    )

    assert (
        "execution_trace"
        in artifact
    )
