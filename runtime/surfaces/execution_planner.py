from runtime.intake.surface_contracts import (
    SurfaceContractExecutor
)

from runtime.execution.planner import (
    build_execution_plan
)

from runtime.surfaces.cognition_resolver import (
    SurfaceCognitionResolver
)

class SurfaceExecutionPlanner:

    def build(self, scope_file=None):

        base_plan = build_execution_plan(
            "governed_validation"
        )

        surfaces = (
            SurfaceContractExecutor()
            .admitted_surfaces(scope_file)
        )

        resolver = (
            SurfaceCognitionResolver()
        )

        return {
            "surface_count": len(surfaces),

            "execution_surface": (
                base_plan["surface"]
            ),

            "activation_record": (
                base_plan["activation_record"]
            ),

            "surface_execution_plan": [

                {
                    "surface_id": (
                        surface["surface_id"]
                    ),

                    "surface_type": (
                        surface["surface_type"]
                    ),

                    "validation_surface": (
                        surface[
                            "validation_surface"
                        ]
                    ),

                    "workflow": (
                        surface.get("workflow_family", "governed_validation_workflow")
                    ),

                    "workflow_family": (
                        surface.get("workflow_family", "general_workflow")
                    ),

                    "cognition": (
                        resolver.resolve(
                            surface[
                                "surface_type"
                            ]
                        )
                    ),

                    "manual_review_required": True
                }

                for surface in surfaces
            ],

            "autonomous_submission": False
        }
