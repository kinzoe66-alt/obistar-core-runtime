import json

from runtime.outcomes.outcome_history import (
    OutcomeHistory
)

def test_outcome_history(tmp_path):

    path = tmp_path / "outcomes.json"

    path.write_text(
        json.dumps({
            "surface-001": ["accepted"]
        }),
        encoding="utf-8"
    )

    assert (
        OutcomeHistory()
        .outcomes_for(
            "surface-001",
            str(path)
        )
        == ["accepted"]
    )
