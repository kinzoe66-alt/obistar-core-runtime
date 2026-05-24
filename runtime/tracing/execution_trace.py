from runtime.execution.workflow_runner import (
    WorkflowRunner
)

from runtime.execution.planner import (
    build_execution_plan
)

from runtime.state.lineage import (
    StateLineageBuilder
)

class ExecutionTraceBuilder:

    def build(self):

        runner = WorkflowRunner()

        workflow = runner.execute()

        plan = build_execution_plan(
            "governed_validation"
        )

        lineage = (
            StateLineageBuilder()
        )

        trace = []

        prior = {
            "state": "initialized"
        }

        for index, step in enumerate(
            workflow["executed_steps"]
        ):

            current = {
                "state": step
            }

            transition = lineage.transition(
                prior_state=prior,
                current_state=current,
                workflow_step=step,
                authority_context=(
                    plan["activation_record"]
                )
            )

            trace.append({
                "sequence": index + 1,
                "step": step,
                "execution_surface": (
                    plan["surface"]
                ),
                "scope": (
                    plan["activation_record"]
                    ["scope"]["name"]
                ),
                "state_transition": transition,
                "manual_review_required": True
            })

            prior = current

        return {
            "trace": trace,
            "terminal_state": (
                workflow["terminal_state"]
            )
        }
