def reviewer_outcomes(packages):
    accepted = [
        package for package in packages
        if package.get("review_outcome") == "accepted"
    ]

    rejected = [
        package for package in packages
        if package.get("review_outcome") == "rejected"
    ]

    return {
        "accepted_count": len(accepted),
        "rejected_count": len(rejected),
        "reviewer_acceptance_ratio": (
            0.0
            if len(packages) == 0
            else round(len(accepted) / len(packages), 4)
        )
    }
