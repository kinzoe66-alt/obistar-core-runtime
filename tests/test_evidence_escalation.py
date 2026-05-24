from runtime.governed_scoring.evidence_escalation import (
    EvidenceEscalationEngine
)


def test_deep_validation_selected():

    engine = (
        EvidenceEscalationEngine()
    )

    result = engine.escalate({
        "weighted": [
            {
                "priority": "high",
                "replay_weight": 1.0,
            }
        ]
    })

    assert (
        result["evidence_escalation"][0]
        ["evidence_level"]
        == "deep_validation"
    )


def test_standard_validation_selected():

    engine = (
        EvidenceEscalationEngine()
    )

    result = engine.escalate({
        "weighted": [
            {
                "priority": "medium",
                "replay_weight": 0.6,
            }
        ]
    })

    assert (
        result["evidence_escalation"][0]
        ["evidence_level"]
        == "standard_validation"
    )
