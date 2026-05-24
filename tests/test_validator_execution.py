from runtime.validators.executor import ValidatorExecutor

def test_validator_execution():

    executor = ValidatorExecutor()

    evidence = {
        "prior_state": {},
        "current_state": {},
        "transition_record": {},
        "replay_trace": {}
    }

    result = executor.execute(
        "session_state_consistency",
        evidence
    )

    assert result["valid"] is True
