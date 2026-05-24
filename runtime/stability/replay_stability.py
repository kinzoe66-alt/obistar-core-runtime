from runtime.authority.registry import AuthorityRegistry

class ReplayStabilityScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("stability_contract")

    def score(self, observation: dict):

        contract = self.contract()

        score = 0.0

        for key, rule in contract[
            "stability_signals"
        ].items():

            if observation.get(key):
                score += rule["weight"]

        thresholds = contract["thresholds"]

        if score >= thresholds["stable"]:
            classification = "stable"

        elif score >= thresholds[
            "review_required"
        ]:
            classification = "review_required"

        else:
            classification = "unstable"

        return {
            "classification": classification,
            "score": round(score, 4),
            "manual_review_required": True,
            "autonomous_submission": False
        }
