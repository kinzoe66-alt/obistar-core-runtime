def workflow_family(method, path):
    normalized = f"{method}:{path}"

    if "/api/" in path:
        family = "api_workflow"
    elif "/auth/" in path:
        family = "authentication_workflow"
    elif "/session/" in path:
        family = "session_workflow"
    else:
        family = "general_workflow"

    return {
        "workflow_family": family,
        "normalized_signature": normalized
    }
