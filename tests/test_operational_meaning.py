from runtime.meaning.translator import OperationalMeaningTranslator

def test_operational_meaning_translation():
    result = OperationalMeaningTranslator().translate_item({
        "surface_id": "surface-001",
        "surface_type": "api",
        "replay_stability": {"classification": "stable"},
        "report_quality": {"classification": "high_quality"},
        "outcome_learning": {"classification": "high_signal"},
        "review_priority": {"classification": "priority_review"},
        "inferred_patterns": [],
        "human_readable_explanations": []
    })

    labels = [
        item["label"]
        for item in result["operational_meaning"]
    ]

    assert "Reproducibility Stability" in labels
    assert "Evidence Quality" in labels
    assert "Business / Review Priority" in labels
