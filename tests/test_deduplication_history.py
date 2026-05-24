import json

from runtime.deduplication.deduplication_scorer import DeduplicationScorer
from runtime.deduplication.history import DeduplicationHistory

def test_deduplication_history(tmp_path):
    path = tmp_path / "dedupe.json"

    path.write_text(json.dumps([
        {
            "surface_type": "api",
            "validation_surface": "api",
            "issue_class": "governed_validation_observation",
            "workflow": "governed_validation_workflow",
            "cognition_focus": ["replay_consistency"]
        }
    ]), encoding="utf-8")

    current = {
        "surface_type": "api",
        "validation_surface": "api",
        "issue_class": "governed_validation_observation",
        "workflow": "governed_validation_workflow",
        "cognition_focus": ["replay_consistency"]
    }

    result = DeduplicationHistory().compare_against_history(
        current,
        DeduplicationScorer(),
        str(path)
    )

    assert result["classification"] == "duplicate"
