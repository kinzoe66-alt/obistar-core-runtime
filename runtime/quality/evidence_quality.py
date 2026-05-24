from runtime.authority.registry import AuthorityRegistry

class EvidenceQualityScorer:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("evidence_quality_contract")

    def score(self, evidence: dict):
        contract = self.contract()
        total = 0.0

        for signal, rule in contract["signals"].items():
            if evidence.get(signal):
                total += rule["weight"]

        thresholds = contract["thresholds"]

        if total >= thresholds["strong"]:
            classification = "strong"
        elif total >= thresholds["acceptable"]:
            classification = "acceptable"
        else:
            classification = "weak"

        return {
            "classification": classification,
            "score": round(total, 4),
            "manual_review_required": True,
            "autonomous_submission": False
        }
