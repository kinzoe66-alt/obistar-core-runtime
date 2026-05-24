from runtime.reporting.contract_executor import (
    ReportingContractExecutor
)

from runtime.reporting.explanation_executor import (
    ExplanationExecutor
)

from runtime.reporting.report_metadata import (
    ReportMetadataBuilder
)

class GovernedReportBuilder:

    def __init__(self):

        self.contract = (
            ReportingContractExecutor()
        )

        self.explainer = (
            ExplanationExecutor()
        )

        self.metadata = (
            ReportMetadataBuilder()
        )

    def build(self, context: dict):

        if not self.contract.admissible(
            context
        ):
            return {
                "admissible": False,
                "reason": (
                    "reporting_contract_not_satisfied"
                )
            }

        validated = context["evidence_bundle"]

        return {
            "admissible": True,

            "summary": self.explainer.summarize(
                validated
            ),

            "affected_surface": (
                validated.get(
                    "affected_surface"
                )
            ),

            "evidence": validated.get(
                "evidence"
            ),

            "replayability": context.get(
                "replay"
            ),

            "impact": validated.get(
                "impact"
            ),

            "remediation": validated.get(
                "remediation"
            ),

            "manual_review_status": (
                "required"
            ),

            "governance": self.metadata.build()
        }
