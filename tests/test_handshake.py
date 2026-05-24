from runtime.authority_loader import load_yaml
from runtime.activation.handshake import AuthorityHandshake

def test_handshake_admission():

    worldview = load_yaml(
        "authority/foundation/worldview.yaml"
    )

    handshake = AuthorityHandshake(
        runtime_surface="replay"
    )

    result = handshake.admit(worldview)

    assert result["admitted"] is True
