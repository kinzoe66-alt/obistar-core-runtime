from runtime.authority.registry import AuthorityRegistry

class ReportQualityScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "quality_contract"
        )

    def score(self, report: dict):

        contract = self.contract()

        score = 0.0

        for key, rule in contract[
            "quality_signals"
        ].items():

            if report.get(key):
                score += rule["weight"]

        thresholds = contract["thresholds"]

        if score >= thresholds[
            "high_quality"
        ]:
            classification = "high_quality"

        elif score >= thresholds[
            "acceptable"
        ]:
            classification = "acceptable"

        else:
            classification = "insufficient"

        return {
            "classification": classification,
            "score": round(score, 4),
            "manual_review_required": True,
            "autonomous_submission": False
        }
