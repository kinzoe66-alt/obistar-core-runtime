from runtime.patterns.pattern_inferencer import PatternInferencer

def test_pattern_inferencer_possible_idor():
    result = PatternInferencer().infer({
        "object_reference_present": True,
        "authorization_context_present": True,
        "replay_stable": True,
        "evidence_complete": True
    })

    top = result[0]

    assert top["pattern_id"] == "possible_idor_pattern"
    assert top["strength"] == "strong_inference"
    assert top["confirmed_issue"] is False
