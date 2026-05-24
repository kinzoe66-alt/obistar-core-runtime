from runtime.replay.reproduction_validator import (
    ReproductionValidator
)

def test_reproduction_validator():

    result = (
        ReproductionValidator()
        .validate({
            "deterministic_steps": True,
            "validation_preconditions": True,
            "replay_trace_reference": True,
            "expected_behavior": True,
            "observed_behavior": True
        })
    )

    assert result["valid"] is True
