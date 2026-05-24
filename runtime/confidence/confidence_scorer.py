from runtime.authority.registry import AuthorityRegistry

class ConfidenceScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "confidence_contract"
        )

    def score(self, item: dict):

        weights = self.contract()["weights"]

        total = 0.0

        if item.get(
            "replay_stability",
            {}
        ).get("classification") == "stable":
            total += weights["replay_stability"]

        if item.get(
            "evidence_quality",
            {}
        ).get("classification") == "strong":
            total += weights["evidence_quality"]

        if item.get(
            "report_quality",
            {}
        ).get("classification") == "high_quality":
            total += weights["report_quality"]

        if item.get(
            "remediation_quality",
            {}
        ).get("classification") == "strong":
            total += weights["remediation_quality"]

        if item.get(
            "outcome_learning",
            {}
        ).get("classification") == "high_signal":
            total += weights["outcome_learning"]

        dedupe = item.get(
            "deduplication",
            {}
        ).get("classification")

        if dedupe in [
            "unique",
            "possible_duplicate"
        ]:
            total += weights[
                "deduplication_uniqueness"
            ]

        thresholds = self.contract()[
            "thresholds"
        ]

        if total >= thresholds[
            "high_confidence"
        ]:
            classification = "high_confidence"

        elif total >= thresholds[
            "moderate_confidence"
        ]:
            classification = "moderate_confidence"

        else:
            classification = "low_confidence"

        return {
            "classification": classification,
            "score": round(total, 4),
            "manual_review_required": True,
            "autonomous_submission": False,
            "confirmed_issue": False
        }
