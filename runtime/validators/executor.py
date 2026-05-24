from runtime.authority.registry import AuthorityRegistry

class ValidatorExecutor:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def load_validator(self, name: str):

        validators = self.registry.contracts(
            "validator_contract"
        )

        for validator in validators:

            doc = validator["document"]

            if doc["name"] == name:
                return doc

        raise ValueError(
            f"validator not found: {name}"
        )

    def execute(self, name: str, evidence: dict):

        validator = self.load_validator(name)

        required = validator.get(
            "evidence_expectations",
            {}
        ).get("required", [])

        missing = [
            item for item in required
            if item not in evidence
        ]

        if missing:
            return {
                "valid": False,
                "missing_evidence": missing,
                "validator": name
            }

        return {
            "valid": True,
            "validator": name,
            "evidence_complete": True
        }
