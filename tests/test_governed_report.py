from runtime.reporting.governed_report import (
    GovernedReportBuilder
)

def test_governed_report_builder():

    builder = GovernedReportBuilder()

    report = builder.build({

        "replay": True,

        "confidence": 0.91,

        "manual_review": True,

        "evidence_bundle": {

            "affected_surface": (
                "account workflow"
            ),

            "issue": (
                "a state consistency problem"
            ),

            "impact": "high",

            "evidence": {
                "trace": "present"
            },

            "remediation": (
                "Review state transition enforcement."
            )
        }
    })

    assert report["admissible"] is True

    assert report[
        "manual_review_status"
    ] == "required"

    assert "summary" in report

    assert "governance" in report

    assert (
        "activation_record"
        in report["governance"]
    )
