from runtime.intake.surface_loader import (
    GovernedSurfaceLoader
)

class IntakeTraceBuilder:

    def build(self, surfaces: list):

        admitted = (
            GovernedSurfaceLoader()
            .load(surfaces)
        )

        return {
            "surface_count": len(admitted),
            "admitted_surfaces": admitted,
            "manual_review_required": True,
            "autonomous_submission": False
        }
