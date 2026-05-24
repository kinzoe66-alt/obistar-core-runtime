from runtime.authority.snapshot import write_authority_snapshot

def test_authority_snapshot(tmp_path):
    out = tmp_path / "authority_snapshot.json"

    snapshot = write_authority_snapshot(str(out))

    assert out.exists()
    assert "worldview" in snapshot["authority_kinds"]
    assert snapshot["contracts"]
