from runtime.comparison.comparison_writer import ComparisonWriter

def test_comparison_writer(tmp_path):
    out = tmp_path / "comparison.json"
    path = ComparisonWriter().write(str(out))
    assert path.exists()
