from runtime.authority.registry import AuthorityRegistry

class ReportingContractExecutor:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract("reporting_contract")

    def admissible(self, context: dict):
        contract = self.contract()
        rules = contract["admissibility"]

        if rules["replay_required"] and not context.get("replay"):
            return False

        if rules["evidence_bundle_required"] and not context.get("evidence_bundle"):
            return False

        if context.get("confidence", 0.0) < rules["confidence_threshold"]:
            return False

        if rules["manual_review_required"] and not context.get("manual_review"):
            return False

        return True
