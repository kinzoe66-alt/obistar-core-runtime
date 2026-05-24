from runtime.comparison.comparison_runner import GovernedComparisonRunner
from runtime.prioritization.review_queue import ReviewQueueBuilder

def test_review_queue_orders_results():
    comparison = GovernedComparisonRunner().run()
    queue = ReviewQueueBuilder().build(comparison)

    scores = [
        item["review_priority"]["score"]
        for item in queue["queue"]
    ]

    assert scores == sorted(scores, reverse=True)
    assert queue["manual_review_required"] is True
