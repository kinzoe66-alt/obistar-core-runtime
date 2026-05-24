from runtime.execution.planner import (
    build_execution_plan
)

from runtime.authority.snapshot import (
    write_authority_snapshot
)

from runtime.tracing.execution_trace import (
    ExecutionTraceBuilder
)

class ReplayCertificationBuilder:

    def build(self):

        plan = build_execution_plan(
            "governed_validation"
        )

        snapshot = write_authority_snapshot()

        trace = (
            ExecutionTraceBuilder()
            .build()
        )

        return {
            "certified": True,

            "execution_surface": (
                plan["surface"]
            ),

            "activation_record": (
                plan["activation_record"]
            ),

            "authority_snapshot": (
                snapshot
            ),

            "execution_trace": trace,

            "manual_review_required": True,

            "autonomous_submission": False
        }
