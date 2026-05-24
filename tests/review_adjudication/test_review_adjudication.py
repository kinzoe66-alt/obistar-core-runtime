from runtime.review_adjudication.outcome_schema import (
    validate_review_outcome,
)

from runtime.review_adjudication.outcome_ingestion import (
    ReviewOutcomeIngestor,
)

from runtime.review_adjudication.review_memory import (
    ReviewMemoryBuilder,
)

from runtime.review_adjudication.confidence_adjustment import (
    ReviewConfidenceAdjuster,
)


def test_review_outcome_schema_accepts_valid_record():
    record = {
        "candidate_id": "candidate_001",
        "reviewer_decision": "useful",
        "review_notes": "clear governed validation evidence",
        "replay_accuracy": 0.9,
        "priority_correctness": 0.8,
        "timestamp": "2026-05-23T00:00:00Z",
    }

    result = validate_review_outcome(record)

    assert result["valid"] is True


def test_review_outcome_schema_rejects_invalid_decision():
    record = {
        "candidate_id": "candidate_001",
        "reviewer_decision": "confirmed_issue",
        "review_notes": "invalid terminal claim",
        "replay_accuracy": 0.9,
        "priority_correctness": 0.8,
        "timestamp": "2026-05-23T00:00:00Z",
    }

    result = validate_review_outcome(record)

    assert result["valid"] is False
    assert result["reason"] == "invalid_reviewer_decision"


def test_review_outcome_ingestion_and_memory(tmp_path):
    store = tmp_path / "reviewer_outcomes.json"

    record = {
        "candidate_id": "candidate_001",
        "reviewer_decision": "useful",
        "review_notes": "clear governed validation evidence",
        "replay_accuracy": 0.9,
        "priority_correctness": 0.8,
        "timestamp": "2026-05-23T00:00:00Z",
    }

    ingestion = ReviewOutcomeIngestor(store).ingest(record)

    assert ingestion["ingested"] is True

    memory = ReviewMemoryBuilder(store).build()

    assert memory["outcome_count"] == 1
    assert memory["decision_counts"]["useful"] == 1
    assert memory["average_replay_accuracy"] == 0.9
    assert memory["average_priority_correctness"] == 0.8


def test_review_confidence_adjustment_preserves_manual_review_boundary():
    candidate = {
        "candidate_id": "candidate_001",
        "review_priority": 0.8,
    }

    memory = {
        "average_replay_accuracy": 0.9,
        "average_priority_correctness": 0.8,
    }

    adjusted = ReviewConfidenceAdjuster().adjust(candidate, memory)

    assert adjusted["manual_review_required"] is True
    assert adjusted["confirmed_issue"] is False
    assert adjusted["adjusted_review_priority"] == 0.68
