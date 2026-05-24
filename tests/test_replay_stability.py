from runtime.stability.replay_stability import (
    ReplayStabilityScorer
)

def test_replay_stability():

    result = (
        ReplayStabilityScorer()
        .score({
            "replay_consistent": True,
            "evidence_consistent": True,
            "lineage_consistent": True,
            "cognition_consistent": True
        })
    )

    assert result["classification"] == "stable"
