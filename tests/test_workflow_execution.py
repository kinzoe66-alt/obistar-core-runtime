from runtime.execution.workflow_runner import WorkflowRunner

def test_workflow_execution():

    runner = WorkflowRunner()

    result = runner.execute()

    assert "queue_manual_review" in result["executed_steps"]
    assert result["terminal_state"] == "manual_review"
