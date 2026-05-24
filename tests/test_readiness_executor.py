from runtime.review.readiness_executor import (
    ReadinessExecutor
)

def test_readiness_executor():

    executor = ReadinessExecutor()

    result = executor.evaluate({
        "observation_id": "real_surface_001",
        "confidence_score": 1.0,
        "priority": "high"
    })

    assert result is True
