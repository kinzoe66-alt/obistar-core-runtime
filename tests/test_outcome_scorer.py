from runtime.outcomes.outcome_scorer import (
    OutcomeScorer
)

def test_outcome_scorer():

    result = (
        OutcomeScorer()
        .score([
            "accepted",
            "rewarded"
        ])
    )

    assert (
        result["classification"]
        == "high_signal"
    )
