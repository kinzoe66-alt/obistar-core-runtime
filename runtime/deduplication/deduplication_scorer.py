from runtime.authority.registry import AuthorityRegistry

class DeduplicationScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("deduplication_contract")

    def compare(self, current: dict, prior: dict):
        contract = self.contract()
        signals = contract["similarity_signals"]

        score = 0.0
        matched = []

        checks = {
            "same_surface_type": current.get("surface_type") == prior.get("surface_type"),
            "same_validation_surface": current.get("validation_surface") == prior.get("validation_surface"),
            "same_issue_class": current.get("issue_class") == prior.get("issue_class"),
            "same_workflow": current.get("workflow") == prior.get("workflow"),
            "same_cognition_focus": bool(
                set(current.get("cognition_focus", []))
                & set(prior.get("cognition_focus", []))
            )
        }

        for key, is_match in checks.items():
            if is_match:
                score += signals[key]["weight"]
                matched.append(key)

        thresholds = contract["thresholds"]

        if score >= thresholds["duplicate"]:
            classification = "duplicate"
        elif score >= thresholds["possible_duplicate"]:
            classification = "possible_duplicate"
        else:
            classification = "unique"

        return {
            "classification": classification,
            "score": round(score, 4),
            "matched_signals": matched,
            "manual_review_required": True,
            "autonomous_rejection": False
        }
