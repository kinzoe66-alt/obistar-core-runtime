from runtime.quality.report_quality import (
    ReportQualityScorer
)

def test_report_quality():

    result = (
        ReportQualityScorer()
        .score({
            "simplified_explanation": True,
            "remediation_present": True,
            "replay_reference_present": True,
            "evidence_complete": True,
            "impact_clarity": True
        })
    )

    assert result["classification"] == "high_quality"
