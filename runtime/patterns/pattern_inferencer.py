from runtime.authority.registry import AuthorityRegistry

class PatternInferencer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "pattern_inference_contract"
        )

    def infer(self, observation: dict):
        contract = self.contract()
        results = []

        for pattern_id, pattern in contract["patterns"].items():
            score = 0.0
            matched = []

            for signal, weight in pattern["signals"].items():
                if observation.get(signal):
                    score += weight
                    matched.append(signal)

            thresholds = contract["thresholds"]

            if score >= thresholds["strong_inference"]:
                strength = "strong_inference"
            elif score >= thresholds["moderate_inference"]:
                strength = "moderate_inference"
            else:
                strength = "weak_inference"

            results.append({
                "pattern_id": pattern_id,
                "label": pattern["label"],
                "strength": strength,
                "score": round(score, 4),
                "matched_signals": matched,
                "confirmed_issue": False,
                "manual_review_required": True,
                "autonomous_submission": False
            })

        return sorted(
            results,
            key=lambda item: item["score"],
            reverse=True
        )
