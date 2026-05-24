def deployment_readiness(
    runtime_stable,
    monetization_ready,
    onboarding_ready
):
    ready = (
        runtime_stable and
        monetization_ready and
        onboarding_ready
    )

    return {
        "deployment_ready": ready,
        "deployment_stage": (
            "governed_operational_beta"
            if ready
            else "internal_calibration"
        )
    }
