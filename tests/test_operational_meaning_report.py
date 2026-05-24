from runtime.meaning.report import OperationalMeaningReport

def test_operational_meaning_report(tmp_path):
    out = tmp_path / "meaning.json"

    path = OperationalMeaningReport().write(str(out))

    assert path.exists()
