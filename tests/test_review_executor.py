from runtime.review.executor import ReviewExecutor

def test_review_executor():

    executor = ReviewExecutor()

    result = executor.adjudicate({
        "replay_trace": {},
        "evidence_bundle": {}
    })

    assert result["adjudicated"] is True
