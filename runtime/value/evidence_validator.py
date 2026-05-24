from runtime.authority.registry import AuthorityRegistry

class ValueEvidenceValidator:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("value_evidence_contract")

    def validate(self, observation: dict):
        requirements = self.contract()["required_value_evidence"]

        missing = []

        for signal, rule in requirements.items():
            if observation.get(signal):
                key = rule["evidence_key"]
                if key not in observation.get("evidence", {}):
                    missing.append(key)

        return {
            "valid": not missing,
            "missing_evidence": missing,
            "manual_review_required": True,
            "autonomous_submission": False
        }
