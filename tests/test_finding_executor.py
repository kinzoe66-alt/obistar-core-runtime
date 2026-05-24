from runtime.findings.executor import FindingExecutor

def test_finding_executor():

    executor = FindingExecutor()

    result = executor.classify(0.91)

    assert result == "reproducible"
