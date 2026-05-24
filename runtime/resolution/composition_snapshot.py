from runtime.resolution.composer import (
    AuthorityComposer
)

def build_composition_snapshot():

    composer = AuthorityComposer()

    ordered = composer.ordered_contracts()

    return {
        "composition_order": [
            {
                "kind": item["kind"],
                "name": item["name"]
            }
            for item in ordered
        ]
    }
