from runtime.review_packages.package_builder import (
    build_review_package
)

def test_review_package_builder():

    package = build_review_package({

        "surface_id": (
            "surface-001"
        ),

        "workflow_family": (
            "authentication_workflow"
        ),

        "parent_authorized_surface_id": (
            "parent-001"
        ),

        "priority": {
            "classification": (
                "highest_priority"
            )
        },

        "outcome_learning": {
            "classification": (
                "high_signal"
            )
        },

        "replay_stability": {
            "classification": (
                "stable"
            )
        },

        "report_quality": {
            "classification": (
                "high_quality"
            )
        },

        "deduplication": {
            "classification": (
                "unique"
            )
        }
    })

    assert (
        package["surface_id"]
        == "surface-001"
    )

    assert (
        package["review_guidance"][
            "manual_review_required"
        ]
        is True
    )
