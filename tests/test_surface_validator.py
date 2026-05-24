from runtime.intake.surface_validator import (
    SurfaceIntakeValidator
)

def test_surface_validator():

    validator = (
        SurfaceIntakeValidator()
    )

    assert validator.validate({
        "surface_id": "surface-001",
        "program": "governed_program",
        "authorized_scope": True,
        "validation_surface": "api"
    }) is True
