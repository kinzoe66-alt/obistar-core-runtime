from runtime.intake.intake_trace import (
    IntakeTraceBuilder
)

def test_intake_trace():

    trace = (
        IntakeTraceBuilder()
        .build([
            {
                "surface_id": "surface-001",
                "program": "governed_program",
                "authorized_scope": True,
                "validation_surface": "api"
            }
        ])
    )

    assert trace["surface_count"] == 1

    assert (
        trace["manual_review_required"]
        is True
    )
