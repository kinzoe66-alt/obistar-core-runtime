import json
from pathlib import Path

from runtime.comparison.comparison_runner import GovernedComparisonRunner
from runtime.prioritization.review_queue import ReviewQueueBuilder

class ReviewQueueReport:

    def write(self, output="reports/review_queue/governed_review_queue.json"):
        comparison = GovernedComparisonRunner().run()
        queue = ReviewQueueBuilder().build(comparison)

        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(queue, indent=2),
            encoding="utf-8"
        )

        return path
