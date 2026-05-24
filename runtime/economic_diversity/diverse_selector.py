from runtime.economic_diversity.novelty_score import novelty_score
from runtime.economic_diversity.repeat_saturation import repeat_saturation_penalty

def select_diverse_candidates(candidates, limit=12):
    selected = []
    seen_families = set()
    seen_parents = set()
    family_counts = {}
    parent_counts = {}

    ordered = sorted(
        candidates,
        key=lambda item: (
            item.get("priority", {}).get("score", 0.0),
            item.get("outcome_learning", {}).get("score", 0.0),
            item.get("replay_stability", {}).get("score", 0.0)
        ),
        reverse=True
    )

    for candidate in ordered:
        novelty = novelty_score(candidate, seen_families, seen_parents)
        saturation = repeat_saturation_penalty(
            candidate,
            family_counts,
            parent_counts
        )

        enriched = dict(candidate)
        enriched["economic_novelty"] = novelty
        enriched["repeat_saturation"] = saturation

        if (
            novelty["novelty_classification"] == "novel"
            and saturation["repeat_saturation_state"] == "acceptable"
        ):
            selected.append(enriched)
            seen_families.add(novelty["workflow_family"])
            seen_parents.add(novelty["parent_authorized_surface_id"])
            family_counts[novelty["workflow_family"]] = (
                family_counts.get(novelty["workflow_family"], 0) + 1
            )
            parent_counts[novelty["parent_authorized_surface_id"]] = (
                parent_counts.get(novelty["parent_authorized_surface_id"], 0) + 1
            )

        if len(selected) >= limit:
            break

    if len(selected) < limit:
        for candidate in ordered:
            if any(existing.get("surface_id") == candidate.get("surface_id") for existing in selected):
                continue

            novelty = novelty_score(candidate, seen_families, seen_parents)
            saturation = repeat_saturation_penalty(
                candidate,
                family_counts,
                parent_counts
            )

            if saturation["repeat_saturation_state"] == "saturated":
                continue

            enriched = dict(candidate)
            enriched["economic_novelty"] = novelty
            enriched["repeat_saturation"] = saturation
            selected.append(enriched)

            family_counts[novelty["workflow_family"]] = (
                family_counts.get(novelty["workflow_family"], 0) + 1
            )
            parent_counts[novelty["parent_authorized_surface_id"]] = (
                parent_counts.get(novelty["parent_authorized_surface_id"], 0) + 1
            )

            if len(selected) >= limit:
                break

    return {
        "selected_count": len(selected),
        "selected_candidates": selected,
        "manual_review_required": True,
        "autonomous_submission": False
    }
