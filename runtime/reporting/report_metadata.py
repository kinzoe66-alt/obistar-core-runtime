from runtime.execution.planner import (
    build_execution_plan
)

from runtime.authority.snapshot import (
    write_authority_snapshot
)

from runtime.certification.replay_certification import (
    ReplayCertificationBuilder
)

class ReportMetadataBuilder:

    def build(self):

        plan = build_execution_plan(
            "governed_validation"
        )

        snapshot = write_authority_snapshot()

        certification = (
            ReplayCertificationBuilder()
            .build()
        )

        return {
            "activation_record": (
                plan["activation_record"]
            ),

            "authority_snapshot": snapshot,

            "replay_certification": (
                certification
            ),

            "manual_review_required": True,

            "autonomous_submission": False,
        }
