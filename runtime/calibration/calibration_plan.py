def calibration_plan(surface_counts):
    return [
        {
            "surface_count": count,
            "mode": "governed_batch_replay",
            "manual_review_required": True,
            "autonomous_submission": False
        }
        for count in surface_counts
    ]
