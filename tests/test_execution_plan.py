from runtime.execution.planner import build_execution_plan
from runtime.execution.workflow_validator import validate_workflow_contract

def test_build_execution_plan():
    plan = build_execution_plan("governed_validation")

    record = plan["activation_record"]

    assert plan["surface"] == "governed_validation"
    assert record["execution_surface"] == "governed_validation"
    assert record["scope"]["name"] == "governed_validation_scope"
    assert "governed_validation" in record["scope"]["allowed_surfaces"]
    assert record["terminal_state"] == "manual_review"
    assert record["autonomous_submission"] is False
    assert record["admitted_authority"]
    assert record["composition"]["composition_order"]

def test_workflow_contract_validates():
    plan = build_execution_plan("governed_validation")
    workflows = plan["authority_stack"]["workflow_contract"]

    for workflow in workflows:
        assert validate_workflow_contract(workflow["document"])
