from runtime.confidence.confidence_scorer import (
    ConfidenceScorer
)

def test_confidence_scorer():

    result = (
        ConfidenceScorer()
        .score({
            "replay_stability": {
                "classification": "stable"
            },
            "evidence_quality": {
                "classification": "strong"
            },
            "report_quality": {
                "classification": "high_quality"
            },
            "remediation_quality": {
                "classification": "strong"
            },
            "outcome_learning": {
                "classification": "high_signal"
            },
            "deduplication": {
                "classification": "possible_duplicate"
            }
        })
    )

    assert (
        result["classification"]
        == "high_confidence"
    )

    assert (
        result["confirmed_issue"]
        is False
    )
