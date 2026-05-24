from runtime.reporting.contract_executor import ReportingContractExecutor

def test_reporting_contract_admissible():
    executor = ReportingContractExecutor()

    assert executor.admissible({
        "replay": True,
        "evidence_bundle": {"id": "evidence-1"},
        "confidence": 0.91,
        "manual_review": True
    }) is True

def test_reporting_contract_denies_without_replay():
    executor = ReportingContractExecutor()

    assert executor.admissible({
        "replay": False,
        "evidence_bundle": {"id": "evidence-1"},
        "confidence": 0.91,
        "manual_review": True
    }) is False
