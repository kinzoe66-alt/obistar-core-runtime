import json
from pathlib import Path

class DeduplicationHistory:

    def load(self, path="reports/outcomes/deduplication_history.json"):
        source = Path(path)

        if not source.exists():
            return []

        return json.loads(source.read_text(encoding="utf-8"))

    def compare_against_history(self, current: dict, scorer, path="reports/outcomes/deduplication_history.json"):
        history = self.load(path)

        results = []

        for prior in history:
            results.append(
                scorer.compare(current, prior)
            )

        if not results:
            return {
                "classification": "unique",
                "score": 0.0,
                "matched_signals": [],
                "manual_review_required": True,
                "autonomous_rejection": False
            }

        return max(results, key=lambda item: item["score"])
