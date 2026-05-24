def control_plane_status(
    tests_passing,
    onboarding_ready,
    monetization_ready
):
    operational = (
        tests_passing and
        onboarding_ready and
        monetization_ready
    )

    return {
        "platform_operational": operational,
        "manual_review_required": True,
        "deployment_state": (
            "governed_beta_ready"
            if operational
            else "internal_only"
        )
    }
