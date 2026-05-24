from runtime.scoring.executor import ScoringExecutor

def test_scoring_execution():

    scoring = ScoringExecutor()

    result = scoring.classify(0.91)

    assert result == "queue_for_manual_review"
