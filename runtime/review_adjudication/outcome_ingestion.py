import json
from pathlib import Path

from runtime.review_adjudication.outcome_schema import (
    validate_review_outcome,
)


class ReviewOutcomeIngestor:

    def __init__(self, store_path="review_outcomes/reviewer_outcomes.json"):
        self.store_path = Path(store_path)

    def ingest(self, record):
        validation = validate_review_outcome(record)

        if not validation["valid"]:
            return {
                "ingested": False,
                "validation": validation,
            }

        self.store_path.parent.mkdir(parents=True, exist_ok=True)

        existing = []

        if self.store_path.exists():
            existing = json.loads(self.store_path.read_text())

        existing.append(record)

        self.store_path.write_text(
            json.dumps(existing, indent=2, sort_keys=True)
        )

        return {
            "ingested": True,
            "validation": validation,
            "store_path": str(self.store_path),
            "outcome_count": len(existing),
        }
