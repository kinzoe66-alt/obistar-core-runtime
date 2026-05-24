def novelty_score(candidate, seen_families, seen_parents):
    family = candidate.get("workflow_family", "unknown")
    parent = candidate.get("parent_authorized_surface_id") or candidate.get("surface_id", "").split("::")[0]

    score = 0.0

    if family not in seen_families:
        score += 0.55

    if parent not in seen_parents:
        score += 0.45

    return {
        "workflow_family": family,
        "parent_authorized_surface_id": parent,
        "novelty_score": round(score, 4),
        "novelty_classification": "novel" if score >= 0.55 else "repetitive"
    }
