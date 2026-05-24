from runtime.authority.registry import AuthorityRegistry

class ReproducibilityExecutor:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def contract(self):

        return self.registry.contract(
            "reproducibility_contract"
        )

    def evaluate(
        self,
        initial_validation: bool,
        live_validation: bool
    ):

        contract = self.contract()

        req = contract["requirements"]

        if (
            req["initial_validation_required"]
            != initial_validation
        ):
            return None

        if (
            req["live_validation_required"]
            != live_validation
        ):
            return None

        return contract["promotion"]["status"]
