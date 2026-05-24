import json
from pathlib import Path

WORKFLOW_FAMILIES = [
    "authentication_workflow",
    "session_workflow",
    "api_workflow",
    "state_transition_workflow",
    "account_creation_workflow",
    "profile_management_workflow",
    "authorization_boundary_workflow",
    "reviewer_evidence_workflow"
]

def expand_governed_inventory(input_file, output_file, target_count):
    data = json.loads(Path(input_file).read_text(encoding="utf-8"))
    base_surfaces = data.get("surfaces", [])

    if not base_surfaces:
        raise ValueError("no authorized base surfaces available")

    expanded = []

    index = 0
    while len(expanded) < target_count:
        base = base_surfaces[index % len(base_surfaces)]
        workflow = WORKFLOW_FAMILIES[index % len(WORKFLOW_FAMILIES)]

        item = dict(base)
        item["runtime_surface_id"] = f'{base["runtime_surface_id"]}::{workflow}::{index + 1}'
        item["parent_authorized_surface_id"] = base["runtime_surface_id"]
        item["workflow_family"] = workflow
        item["validation_surface"] = base.get("validation_surface", "web")
        item["authorized_scope"] = True
        item["manual_review_required"] = True
        item["autonomous_submission"] = False

        expanded.append(item)
        index += 1

    output = {
        "program": data.get("program", "governed_program"),
        "source": data.get("source", "authorized_inventory_expansion"),
        "expansion_model": "governed_authorized_workflow_surface_expansion",
        "target_surface_count": target_count,
        "actual_surface_count": len(expanded),
        "manual_review_required": True,
        "autonomous_submission": False,
        "surfaces": expanded
    }

    Path(output_file).parent.mkdir(parents=True, exist_ok=True)
    Path(output_file).write_text(json.dumps(output, indent=2), encoding="utf-8")

    return output
