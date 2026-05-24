def build_reviewer_deliverable(candidate, playbook=None):

    workflow = candidate.get("workflow_family", "general_workflow")

    return {
        "title": (
            "Governed manual review observation for "
            + workflow.replace("_", " ")
        ),

        "surface_id": candidate.get("surface_id"),

        "workflow_family": workflow,

        "status": "manual_review_required",

        "confirmed_issue": False,

        "autonomous_submission": False,

        "plain_language_summary": (
            "This candidate points to a workflow that should be manually "
            "reviewed because it is stable, unique, and operationally relevant."
        ),

        "what_was_reviewed": (
            "The reviewer should inspect the listed authorized surface and "
            "focus only on the named workflow family."
        ),

        "why_it_matters": (
            "Stable and repeatable workflow behavior helps reviewers decide "
            "whether the observation is meaningful enough for deeper review."
        ),

        "how_to_reproduce": (
            playbook.get("manual_steps", [])
            if playbook
            else []
        ),

        "what_evidence_to_collect": [
            "Timestamp of each manual review attempt.",
            "Screenshots showing each important workflow step.",
            "Short notes describing expected behavior.",
            "Short notes describing observed behavior.",
            "Any relevant request or response details that can be safely included.",
            "Clear indication whether the behavior reproduced more than once."
        ],

        "reviewer_quality_checks": [
            "Can another reviewer understand the workflow?",
            "Can another reviewer repeat the same steps?",
            "Is the observation described without overclaiming?",
            "Is the evidence clear enough to support manual review?",
            "Is the observation still inside authorized scope?"
        ],

        "recommended_next_action": (
            "Perform the manual review steps, collect evidence, and only "
            "prepare a report if the behavior remains reproducible and clear."
        )
    }
