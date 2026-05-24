def resolve_review_route(candidate, inventory):
    parent = (
        candidate.get("parent_authorized_surface_id")
        or candidate.get("surface_id", "").split("::")[0]
    )

    matched = None

    for surface in inventory.get("surfaces", []):
        if surface.get("runtime_surface_id") == parent:
            matched = surface
            break

    if not matched:
        return {
            "route_status": "unresolved",
            "manual_review_required": True,
            "autonomous_submission": False,
            "reason": "No matching authorized parent surface was found."
        }

    asset = matched.get("asset_reference") or matched.get("canonical_asset_name")

    return {
        "route_status": "resolved",
        "surface_id": candidate.get("surface_id"),
        "parent_authorized_surface_id": parent,
        "authorized_asset": asset,
        "start_url": "https://" + asset.replace("https://", "").replace("http://", ""),
        "workflow_family": candidate.get("workflow_family"),
        "plain_language_start": (
            "Start from the authorized asset shown here. If it redirects, "
            "record the redirect target and continue only if the destination "
            "remains within authorized scope."
        ),
        "manual_review_required": True,
        "autonomous_submission": False,
        "stop_conditions": [
            "Stop if the destination is outside authorized scope.",
            "Stop if the page requires activity outside the program rules.",
            "Stop if the workflow cannot be located manually.",
            "Stop if evidence cannot be captured clearly."
        ]
    }
