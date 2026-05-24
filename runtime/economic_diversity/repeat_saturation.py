def repeat_saturation_penalty(candidate, family_counts, parent_counts):
    family = candidate.get("workflow_family", "unknown")
    parent = (
        candidate.get("parent_authorized_surface_id")
        or candidate.get("surface_id", "").split("::")[0]
    )

    family_count = family_counts.get(family, 0)
    parent_count = parent_counts.get(parent, 0)

    penalty = 0.0

    if family_count >= 1:
        penalty += 0.20

    if family_count >= 2:
        penalty += 0.20

    if parent_count >= 1:
        penalty += 0.20

    if parent_count >= 2:
        penalty += 0.20

    penalty = min(penalty, 0.80)

    return {
        "workflow_family": family,
        "parent_authorized_surface_id": parent,
        "family_seen_count": family_count,
        "parent_seen_count": parent_count,
        "repeat_saturation_penalty": round(penalty, 4),
        "repeat_saturation_state": (
            "saturated"
            if penalty >= 0.40
            else "acceptable"
        )
    }
