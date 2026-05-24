from runtime.governed_replay.replay_template import (
    ReplayTemplateBuilder,
)


def test_replay_template_builds_deterministic_route():

    template = (
        ReplayTemplateBuilder()
        .build({
            "observation_id": "obs_001",
            "surface_id": "surface_001",
        })
    )

    assert (
        template["observation_id"]
        == "obs_001"
    )

    assert (
        template["deterministic"]
        is True
    )

    assert (
        template["command"][0]
        == "python"
    )
