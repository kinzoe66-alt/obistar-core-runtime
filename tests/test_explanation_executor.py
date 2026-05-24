from runtime.reporting.explanation_executor import ExplanationExecutor

def test_explanation_executor_simplifies_validated_fields():
    executor = ExplanationExecutor()

    summary = executor.summarize({
        "affected_surface": "account workflow",
        "issue": "a state consistency problem",
        "impact": "high"
    })

    assert "account workflow" in summary
    assert "state consistency problem" in summary
    assert "Replay evidence" in summary
