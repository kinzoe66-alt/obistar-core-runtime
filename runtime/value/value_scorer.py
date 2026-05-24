from runtime.authority.registry import AuthorityRegistry
from runtime.value.evidence_validator import ValueEvidenceValidator

class ValueScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()
        self.evidence_validator = ValueEvidenceValidator(self.registry)

    def contract(self):
        return self.registry.contract("value_contract")

    def score(self, observation: dict):
        evidence_result = self.evidence_validator.validate(observation)

        if not evidence_result["valid"]:
            return {
                "classification": "rejected",
                "score": 0.0,
                "reason": "missing_value_evidence",
                "missing_evidence": evidence_result["missing_evidence"],
                "manual_review_required": True,
                "autonomous_submission": False
            }

        contract = self.contract()
        indicators = contract["value_indicators"]

        if not observation.get("replay_stable"):
            return {"classification": "rejected", "score": 0.0, "reason": "replay_missing"}

        if not observation.get("evidence_complete"):
            return {"classification": "rejected", "score": 0.0, "reason": "evidence_missing"}

        if not observation.get("manual_review"):
            return {"classification": "rejected", "score": 0.0, "reason": "manual_review_missing"}

        score = 0.0

        for key, data in indicators.items():
            if observation.get(key):
                score += data["weight"]

        thresholds = contract["thresholds"]

        if score >= thresholds["high_value_candidate"]:
            classification = "high_value_candidate"
        elif score >= thresholds["review_candidate"]:
            classification = "review_candidate"
        else:
            classification = "insufficient_value"

        return {
            "classification": classification,
            "score": round(score, 4),
            "manual_review_required": True,
            "autonomous_submission": False
        }
