import json
from pathlib import Path


class ReviewMemoryBuilder:

    def __init__(self, store_path="review_outcomes/reviewer_outcomes.json"):
        self.store_path = Path(store_path)

    def build(self):
        if not self.store_path.exists():
            return {
                "outcome_count": 0,
                "decision_counts": {},
                "average_replay_accuracy": 0,
                "average_priority_correctness": 0,
            }

        records = json.loads(self.store_path.read_text())

        decision_counts = {}

        replay_total = 0
        priority_total = 0

        for record in records:
            decision = record["reviewer_decision"]
            decision_counts[decision] = decision_counts.get(decision, 0) + 1
            replay_total += record["replay_accuracy"]
            priority_total += record["priority_correctness"]

        count = len(records)

        return {
            "outcome_count": count,
            "decision_counts": decision_counts,
            "average_replay_accuracy": round(replay_total / count, 4) if count else 0,
            "average_priority_correctness": round(priority_total / count, 4) if count else 0,
        }
