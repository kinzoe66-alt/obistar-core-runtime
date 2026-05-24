from runtime.activation.scope_validator import (
    ScopeValidator
)

def test_scope_validator():

    validator = ScopeValidator()

    assert validator.validate(
        "governed_validation"
    ) is True
