from runtime.comparison.comparison_runner import GovernedComparisonRunner

def test_comparison_metrics():
    result = GovernedComparisonRunner().run()

    assert result["metrics"]["surface_count"] == 3
    assert result["metrics"]["certification_rate"] == 1.0
    assert result["metrics"]["report_admissibility_rate"] == 1.0
    assert result["metrics"]["manual_review_rate"] == 1.0
    assert "high_value_candidate_rate" in result["metrics"]
