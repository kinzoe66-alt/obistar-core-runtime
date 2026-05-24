from runtime.authority.registry import AuthorityRegistry

class ScoringExecutor:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def load_policy(self):

        return self.registry.contract(
            "scoring_contract"
        )

    def classify(self, score: float):

        policy = self.load_policy()

        thresholds = policy["thresholds"]

        if score >= thresholds["queue_for_manual_review"]:
            return "queue_for_manual_review"

        if score >= thresholds["require_more_evidence"]:
            return "require_more_evidence"

        return "reject_as_insufficient"
