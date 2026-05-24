from runtime.reporting.review_queue_report import ReviewQueueReport

def test_review_queue_report(tmp_path):
    out = tmp_path / "queue.json"

    path = ReviewQueueReport().write(str(out))

    assert path.exists()
