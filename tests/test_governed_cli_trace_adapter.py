from runtime.governed_cli.trace_adapter import GovernedCLITraceAdapter


def test_cli_trace_adapter_records_review_safe_result():
    adapter = GovernedCLITraceAdapter()

    result = adapter.run_for_trace(
        ["python", "--version"],
        step_name="runtime_version_check",
    )

    assert result["step"] == "runtime_version_check"
    assert result["returncode"] == 0
    assert result["manual_review_required"] is True
    assert result["autonomous_submission"] is False
