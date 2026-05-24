def diversity_metrics(candidates):
    families = {
        candidate.get("workflow_family", "unknown")
        for candidate in candidates
    }

    parents = {
        candidate.get("parent_authorized_surface_id") or candidate.get("surface_id", "").split("::")[0]
        for candidate in candidates
    }

    total = len(candidates)

    return {
        "candidate_count": total,
        "unique_workflow_families": len(families),
        "unique_parent_surfaces": len(parents),
        "workflow_family_diversity_ratio": 0.0 if total == 0 else round(len(families) / total, 4),
        "parent_surface_diversity_ratio": 0.0 if total == 0 else round(len(parents) / total, 4)
    }
