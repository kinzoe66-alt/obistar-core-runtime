from runtime.authority.registry import AuthorityRegistry

class ReproductionValidator:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "reproduction_contract"
        )

    def validate(self, reproduction: dict):

        required = self.contract()[
            "required_replay_elements"
        ]

        missing = []

        for item in required:
            if not reproduction.get(item):
                missing.append(item)

        return {
            "valid": not missing,
            "missing_elements": missing,
            "manual_review_required": True,
            "autonomous_submission": False
        }
