def validate_workflow_contract(workflow: dict) -> bool:
    steps = workflow.get("steps", [])
    blocked = set(workflow.get("blocked_steps", []))

    overlap = set(steps) & blocked
    if overlap:
        raise ValueError(f"workflow contains blocked steps: {sorted(overlap)}")

    terminal = workflow.get("terminal_state", {})
    if terminal.get("manual_review") is not True:
        raise ValueError("workflow must terminate at manual_review")

    return True
