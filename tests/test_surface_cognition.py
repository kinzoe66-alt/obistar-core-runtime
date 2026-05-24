from runtime.surfaces.cognition_resolver import (
    SurfaceCognitionResolver
)

def test_surface_cognition():

    resolver = (
        SurfaceCognitionResolver()
    )

    cognition = resolver.resolve("api")

    assert cognition

    assert cognition[0]["validator_focus"]
