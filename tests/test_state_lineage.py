from runtime.state.lineage import (
    StateLineageBuilder
)

def test_state_lineage():

    lineage = (
        StateLineageBuilder()
    )

    transition = lineage.transition(
        prior_state={"state": "a"},
        current_state={"state": "b"},
        workflow_step="execute_validator",
        authority_context={"scope": "test"}
    )

    assert (
        transition["workflow_step"]
        == "execute_validator"
    )

    assert (
        transition["manual_review_required"]
        is True
    )
