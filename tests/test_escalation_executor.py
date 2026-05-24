from runtime.escalation.executor import EscalationExecutor

def test_escalation_executor():

    executor = EscalationExecutor()

    result = executor.evaluate(
        0.91,
        replay_consistent=True
    )

    assert result == "manual_review_required"
