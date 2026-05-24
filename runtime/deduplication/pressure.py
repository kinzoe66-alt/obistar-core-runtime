from runtime.authority.registry import AuthorityRegistry

class DuplicatePressure:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def contract(self):
        return self.registry.contract(
            "duplicate_pressure_contract"
        )

    def apply(self, classification: str):

        levels = self.contract()[
            "pressure_levels"
        ]

        multiplier = levels.get(
            classification,
            {"multiplier": 1.0}
        )["multiplier"]

        return {
            "classification": classification,
            "multiplier": multiplier,
            "manual_review_required": True,
            "autonomous_rejection": False
        }
