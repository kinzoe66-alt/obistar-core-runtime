from runtime.authority.registry import AuthorityRegistry

class HumanReadableExplanationBuilder:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "explanation_contract"
        )

    def build(self, inferred_patterns):

        contract = self.contract()
        explanations = []

        for pattern in inferred_patterns:

            if pattern["strength"] == "weak_inference":
                continue

            pattern_id = pattern["pattern_id"]

            templates = (
                contract["patterns"]
                .get(pattern_id, {})
                .get("templates", [])
            )

            if not templates:
                continue

            explanations.append({
                "pattern_id": pattern_id,
                "strength": pattern["strength"],
                "summary": templates[0],
                "manual_review_required": True,
                "confirmed_issue": False
            })

        return explanations
