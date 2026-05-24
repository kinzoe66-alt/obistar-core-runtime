from runtime.authority.registry import AuthorityRegistry

def test_authority_registry():

    registry = AuthorityRegistry()

    worldview = registry.contract(
        "worldview"
    )

    assert worldview["name"] == (
        "governed_validation_runtime"
    )
