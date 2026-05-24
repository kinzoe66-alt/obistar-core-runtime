from runtime.reporting.report_metadata import (
    ReportMetadataBuilder
)

def test_report_metadata():

    builder = (
        ReportMetadataBuilder()
    )

    metadata = builder.build()

    assert (
        "activation_record"
        in metadata
    )

    assert (
        "authority_snapshot"
        in metadata
    )

    assert (
        "replay_certification"
        in metadata
    )

    assert metadata[
        "manual_review_required"
    ] is True
