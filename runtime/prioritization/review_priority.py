from runtime.authority.registry import AuthorityRegistry

from runtime.cognition_damping.priority_damping import damp_priority

class ReviewPriorityScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("priority_contract")

    def score(self, result: dict):
        contract = self.contract()
        weights = contract["priority_weights"]
        penalties = contract["penalties"]

        score = 0.0

        if result.get("value_classification") == "high_value_candidate":
            score += weights["high_value_candidate"]

        if result.get("replay_stability", {}).get("classification") == "stable":
            score += weights["stable_replay"]

        if result.get("report_quality", {}).get("classification") == "high_quality":
            score += weights["high_quality_report"]

        if result.get("outcome_learning", {}).get("classification") in ["high_signal", "medium_signal"]:
            score += weights["positive_outcome_signal"]

        if result.get("deduplication", {}).get("classification") == "unique":
            score += weights["unique_or_low_duplicate_risk"]

        dedupe_class = result.get("deduplication", {}).get("classification")
        if dedupe_class in penalties:
            score += penalties[dedupe_class]

        if result.get("outcome_learning", {}).get("classification") == "weak_signal":
            score += penalties["weak_outcome_signal"]

        workflow_weight = float(
            result.get(
                "workflow_weight",
                {}
            ).get(
                "workflow_weight_score",
                0.25
            )
        )

        evidence_weight = float(
            result.get(
                "evidence_history",
                {}
            ).get(
                "evidence_history_score",
                0.25
            )
        )

        score += workflow_weight * 0.20
        score += evidence_weight * 0.15

        score = max(0.0, min(1.0, score))

        thresholds = contract["thresholds"]

        if score >= thresholds["highest_priority"]:
            classification = "highest_priority"
        elif score >= thresholds["priority_review"]:
            classification = "priority_review"
        else:
            classification = "hold"

        damped = damp_priority(
            score,
            result.get("outcome_learning", {}).get("classification", "weak_signal")
        )

        return {
            "classification": damped["damped_priority_classification"],
            "score": damped["damped_priority_score"],
            "undamped_classification": classification,
            "undamped_score": round(score, 4),
            "manual_review_required": True,
            "autonomous_submission": False,
            "autonomous_rejection": False
        }
