def human_workflow_name(workflow_family):
    names = {
        "session_workflow": "session continuity review",
        "authentication_workflow": "sign-in and account access review",
        "api_workflow": "API behavior review",
        "state_transition_workflow": "workflow state review",
        "account_creation_workflow": "account creation review",
        "profile_management_workflow": "profile update review",
        "authorization_boundary_workflow": "access boundary review",
        "reviewer_evidence_workflow": "evidence quality review"
    }

    return names.get(
        workflow_family,
        "workflow review"
    )
