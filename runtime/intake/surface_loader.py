from runtime.intake.surface_validator import (
    SurfaceIntakeValidator
)

class GovernedSurfaceLoader:

    def __init__(self):
        self.validator = (
            SurfaceIntakeValidator()
        )

    def load(self, surfaces: list):

        admitted = []

        for surface in surfaces:

            self.validator.validate(surface)

            admitted.append({
                "surface_id": (
                    surface["surface_id"]
                ),
                "program": (
                    surface["program"]
                ),
                "authorized_scope": (
                    surface["authorized_scope"]
                ),
                "validation_surface": (
                    surface["validation_surface"]
                ),
                "manual_review_required": True
            })

        return admitted
