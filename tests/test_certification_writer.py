from runtime.certification.certification_writer import (
    CertificationWriter
)

def test_certification_writer(tmp_path):

    output = (
        tmp_path /
        "replay_certification.json"
    )

    path = (
        CertificationWriter()
        .write(str(output))
    )

    assert path.exists()
