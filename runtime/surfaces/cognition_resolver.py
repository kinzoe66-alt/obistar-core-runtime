from runtime.authority.registry import AuthorityRegistry

class SurfaceCognitionResolver:

    def __init__(self, registry=None):
        self.registry = registry or AuthorityRegistry()

    def cognition_contracts(self):
        return self.registry.contracts(
            "cognition_contract"
        )

    def resolve(self, surface_type: str):

        matched = []

        for entry in self.cognition_contracts():

            doc = entry["document"]

            if surface_type in doc["applies_to"]:

                matched.append({
                    "name": doc["name"],
                    "validator_focus": (
                        doc["validator_focus"]
                    ),
                    "reporting_focus": (
                        doc["reporting_focus"]
                    )
                })

        return matched
