import pytest

from runtime.activation.scope_validator import (
    ScopeValidator
)

def test_scope_denial():

    validator = ScopeValidator()

    with pytest.raises(PermissionError):
        validator.validate(
            "unauthorized_surface"
        )
