from runtime.human_language.workflow_names import human_workflow_name

def humanize_deliverable(deliverable):
    workflow = deliverable.get("workflow_family", "general_workflow")
    readable_workflow = human_workflow_name(workflow)

    return {
        "title": readable_workflow.title(),

        "review_context": (
            "This review focuses on a specific authorized workflow that the "
            "system ranked as worth checking manually."
        ),

        "plain_language_summary": (
            "The workflow looked consistent enough during replay to deserve "
            "a closer manual review. The next step is to repeat the workflow "
            "carefully and save clear evidence if the behavior can be reproduced."
        ),

        "why_this_is_being_reviewed": (
            "This item was selected because it was stable, not repetitive, "
            "and different enough from the other review items to be useful."
        ),

        "what_to_do_next": [
            "Open the authorized workflow.",
            "Follow the steps slowly and consistently.",
            "Write down what you expected to happen.",
            "Write down what actually happened.",
            "Repeat the same steps to see if the behavior happens again.",
            "Save only clear evidence that another reviewer could understand."
        ],

        "evidence_to_save": deliverable.get(
            "what_evidence_to_collect",
            []
        ),

        "safe_review_boundary": (
            "Do not make a final claim from this item alone. Use it only as "
            "a guided manual review path until the behavior is clearly reproduced."
        ),

        "internal_reference": {
            "surface_id": deliverable.get("surface_id"),
            "workflow_family": workflow,
            "status": deliverable.get("status")
        },

        "manual_review_required": True,
        "autonomous_submission": False,
        "confirmed_issue": False
    }
