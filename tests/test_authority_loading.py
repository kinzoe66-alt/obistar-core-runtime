from runtime.authority_loader import load_authority_tree
from runtime.contract_validator import validate_contract

def test_authority_contracts_load():
    docs = load_authority_tree("authority")
    assert docs
    for path, doc in docs.items():
        assert validate_contract(doc, path)
