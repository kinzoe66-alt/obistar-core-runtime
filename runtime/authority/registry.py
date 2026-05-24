from runtime.authority_loader import load_authority_tree
from runtime.resolution.resolver import resolve_authority_stack

class AuthorityRegistry:

    def __init__(self):

        docs = load_authority_tree("authority")

        self.stack = resolve_authority_stack(docs)

    def contracts(self, kind: str):

        return self.stack.get(kind, [])

    def contract(self, kind: str):

        contracts = self.contracts(kind)

        if not contracts:
            raise ValueError(
                f"missing authority kind: {kind}"
            )

        return contracts[0]["document"]
