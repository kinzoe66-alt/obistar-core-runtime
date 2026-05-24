from runtime.comparison.comparison_runner import GovernedComparisonRunner

def test_governed_comparison_runner():
    result = GovernedComparisonRunner().run(
        "test_scopes/sample_surfaces.json"
    )

    assert result["surface_count"] == 3
    assert all(item["certified"] is True for item in result["results"])
    assert all(item["report_admissible"] is True for item in result["results"])
    assert all("value_classification" in item for item in result["results"])
    assert all("outcome_learning" in item for item in result["results"])
    assert all("deduplication" in item for item in result["results"])
    assert all("review_priority" in item for item in result["results"])
    assert all("inferred_patterns" in item for item in result["results"])
    assert all("human_readable_explanations" in item for item in result["results"])
    assert result["manual_review_required"] is True
