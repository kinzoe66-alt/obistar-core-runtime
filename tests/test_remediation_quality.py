from runtime.quality.remediation_quality import RemediationQualityScorer

def test_remediation_quality():
    result = RemediationQualityScorer().score({
        "root_cause_guidance": True,
        "validation_context": True,
        "replay_reference": True,
        "recommended_review_action": True
    })

    assert result["classification"] == "strong"
