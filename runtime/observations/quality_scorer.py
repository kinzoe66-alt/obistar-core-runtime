from runtime.authority.registry import AuthorityRegistry

class ObservationQualityScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "observation_quality_contract"
        )

    def score(self, item: dict):
        contract = self.contract()
        weights = contract["quality_weights"]

        total = 0.0

        if item.get("replay_stability", {}).get("classification") == "stable":
            total += weights["reproducible"]["weight"]

        if item.get("report_quality", {}).get("classification") == "high_quality":
            total += weights["understandable"]["weight"]

        if item.get("deduplication", {}).get("classification") in ["unique", "possible_duplicate"]:
            total += weights["low_duplicate_pressure"]["weight"]

        if item.get("value_classification") == "high_value_candidate":
            total += weights["operationally_meaningful"]["weight"]

        thresholds = contract["thresholds"]

        if total >= thresholds["strongest_candidate"]:
            classification = "strongest_candidate"
        elif total >= thresholds["review_candidate"]:
            classification = "review_candidate"
        else:
            classification = "hold"

        return {
            "classification": classification,
            "score": round(total, 4),
            "manual_review_required": True,
            "autonomous_submission": False
        }
