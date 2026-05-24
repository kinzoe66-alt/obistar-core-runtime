def build_reviewer_playbook(candidate):
    workflow = candidate.get("workflow_family", "general_workflow")
    surface_id = candidate.get("surface_id")

    return {
        "surface_id": surface_id,
        "workflow_family": workflow,
        "manual_review_required": True,
        "autonomous_submission": False,
        "plain_language_goal": (
            "Manually check whether this workflow behaves consistently "
            "when repeated under the same authorized conditions."
        ),
        "manual_steps": [
            "Open the authorized surface listed in the candidate.",
            "Start from a normal signed-in or expected user state if the workflow requires it.",
            "Perform the workflow once and write down what happened.",
            "Repeat the same workflow again under the same conditions.",
            "Compare whether the behavior stayed consistent.",
            "Save simple evidence: timestamps, screenshots, notes, and relevant response details.",
            "Do not submit anything automatically.",
            "Mark the candidate as ready for deeper manual review only if the behavior is reproducible."
        ],
        "what_to_look_for": [
            "Unexpected differences between repeated runs.",
            "Session state changing when it should stay consistent.",
            "Workflow steps behaving differently for the same user state.",
            "Authorization or access boundaries behaving inconsistently.",
            "Evidence that can be explained clearly to another reviewer."
        ],
        "stop_conditions": [
            "Stop if the surface is outside authorized scope.",
            "Stop if the workflow cannot be reproduced.",
            "Stop if evidence is unclear.",
            "Stop if continuing would require unsafe or unauthorized activity."
        ]
    }
