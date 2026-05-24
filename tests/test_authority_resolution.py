from runtime.authority_loader import load_authority_tree
from runtime.resolution.resolver import resolve_authority_stack

def test_authority_resolution_stack():
    docs = load_authority_tree("authority")
    stack = resolve_authority_stack(docs)

    assert "worldview" in stack
    assert "validator_contract" in stack
    assert "scoring_contract" in stack
    assert "workflow_contract" in stack
