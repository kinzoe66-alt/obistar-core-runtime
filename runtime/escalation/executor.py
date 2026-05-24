from runtime.authority.registry import AuthorityRegistry

class EscalationExecutor:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def contract(self):

        return self.registry.contract(
            "escalation_contract"
        )

    def evaluate(self, score: float, replay_consistent=True):

        policy = self.contract()

        required = policy[
            "escalation_requirements"
        ]

        if score < required[
            "minimum_confidence"
        ]:
            return "deny"

        if (
            required["replay_consistent"]
            and not replay_consistent
        ):
            return "deny"

        return "manual_review_required"
