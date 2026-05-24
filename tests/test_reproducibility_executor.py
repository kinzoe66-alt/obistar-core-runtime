from runtime.review.reproducibility_executor import (
    ReproducibilityExecutor
)

def test_reproducibility_executor():

    executor = ReproducibilityExecutor()

    result = executor.evaluate(
        initial_validation=False,
        live_validation=False
    )

    assert result == "reproducible_candidate"
