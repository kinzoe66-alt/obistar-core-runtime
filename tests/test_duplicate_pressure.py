from runtime.deduplication.pressure import (
    DuplicatePressure
)

def test_duplicate_pressure():

    result = (
        DuplicatePressure()
        .apply("duplicate")
    )

    assert result["multiplier"] == 0.25
