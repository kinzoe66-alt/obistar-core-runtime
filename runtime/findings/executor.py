from runtime.authority.registry import AuthorityRegistry

class FindingExecutor:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def contract(self):

        return self.registry.contract(
            "finding_contract"
        )

    def classify(self, score: float):

        contract = self.contract()

        rules = contract["classification"]

        if score >= rules["reproducible"]["minimum_score"]:
            return "reproducible"

        if score <= rules["insufficient_evidence"]["maximum_score"]:
            return "insufficient_evidence"

        return "requires_manual_review"
