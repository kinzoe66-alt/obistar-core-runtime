from runtime.intake.surface_loader import (
    GovernedSurfaceLoader
)

def test_surface_loader():

    loader = (
        GovernedSurfaceLoader()
    )

    surfaces = loader.load([
        {
            "surface_id": "surface-001",
            "program": "governed_program",
            "authorized_scope": True,
            "validation_surface": "api"
        }
    ])

    assert len(surfaces) == 1
