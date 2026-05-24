import pytest
from runtime.activation.fail_closed import require

def test_fail_closed_blocks_false():
    with pytest.raises(PermissionError):
        require(False, "blocked")

def test_fail_closed_allows_true():
    assert require(True, "allowed") is True
