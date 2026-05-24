from runtime.resolution.composer import (
    AuthorityComposer
)

def test_authority_composition():

    composer = AuthorityComposer()

    ordered = composer.ordered_contracts()

    assert ordered

    assert ordered[0]["kind"] == "worldview"
