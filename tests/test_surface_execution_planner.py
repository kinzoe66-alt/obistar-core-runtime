from runtime.surfaces.execution_planner import (
    SurfaceExecutionPlanner
)

def test_surface_execution_planner():

    plan = (
        SurfaceExecutionPlanner()
        .build()
    )

    assert plan["surface_count"] == 3

    assert (
        plan["execution_surface"]
        == "governed_validation"
    )

    assert plan["activation_record"]

    assert all(
        item["manual_review_required"]
        is True
        for item in plan[
            "surface_execution_plan"
        ]
    )

    assert all(
        item["cognition"]
        for item in plan[
            "surface_execution_plan"
        ]
    )
