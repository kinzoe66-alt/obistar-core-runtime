from runtime.value.evidence_validator import ValueEvidenceValidator

def test_value_evidence_validator_accepts_supported_signals():
    result = ValueEvidenceValidator().validate({
        "replay_stable": True,
        "evidence": {
            "replay_trace": {}
        }
    })

    assert result["valid"] is True

def test_value_evidence_validator_rejects_missing_signal_evidence():
    result = ValueEvidenceValidator().validate({
        "replay_stable": True,
        "evidence": {}
    })

    assert result["valid"] is False
    assert "replay_trace" in result["missing_evidence"]
