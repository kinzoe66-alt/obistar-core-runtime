from runtime.authority.registry import AuthorityRegistry

class AuthorityComposer:

    def __init__(self, registry=None):

        self.registry = registry or AuthorityRegistry()

    def inheritance_policy(self):

        return self.registry.contract(
            "inheritance_contract"
        )

    def ordered_contracts(self):

        policy = self.inheritance_policy()

        ordered = []

        for kind in policy["priority_order"]:

            for entry in self.registry.contracts(kind):
                ordered.append({
                    "kind": kind,
                    "name": entry["name"],
                    "document": entry["document"]
                })

        return ordered
