from runtime.authority_loader import load_yaml
from runtime.resolution.normalizer import normalize_contract
from runtime.contract_validator import validate_contract

def test_contract_normalization():
    doc = load_yaml("authority/foundation/worldview.yaml")
    normalized = normalize_contract(doc)

    assert validate_contract(normalized)
    assert "manual_review" in normalized
    assert "allowed_runtime_behavior" in normalized
    assert "blocked_runtime_behavior" in normalized
