class StateLineageBuilder:

    def transition(
        self,
        prior_state: dict,
        current_state: dict,
        workflow_step: str,
        authority_context: dict
    ):

        return {
            "prior_state": prior_state,
            "current_state": current_state,
            "workflow_step": workflow_step,
            "authority_context": authority_context,
            "manual_review_required": True
        }
