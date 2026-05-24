from runtime.authority.registry import AuthorityRegistry

class DeliverableValidator:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "deliverable_contract"
        )

    def validate(self, report: dict):

        contract = self.contract()

        missing = []

        for section in contract[
            "required_sections"
        ]:

            if not report.get(section):
                missing.append(section)

        return {
            "valid": not missing,
            "missing_sections": missing,
            "manual_review_required": True,
            "autonomous_submission": False
        }
