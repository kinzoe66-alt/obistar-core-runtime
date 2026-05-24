from runtime.quality.evidence_quality import EvidenceQualityScorer

def test_evidence_quality():
    result = EvidenceQualityScorer().score({
        "replay_trace_present": True,
        "state_lineage_present": True,
        "affected_surface_present": True,
        "validation_conditions_present": True,
        "remediation_present": True
    })

    assert result["classification"] == "strong"
