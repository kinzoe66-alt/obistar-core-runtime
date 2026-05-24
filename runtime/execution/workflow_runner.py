from runtime.execution.planner import build_execution_plan

class WorkflowRunner:

    def __init__(self, surface="governed_validation"):
        self.plan = build_execution_plan(surface)

    def workflow(self):

        workflows = self.plan[
            "authority_stack"
        ]["workflow_contract"]

        return workflows[0]["document"]

    def execute(self):

        workflow = self.workflow()

        executed = []

        for step in workflow["steps"]:
            executed.append(step)

        return {
            "executed_steps": executed,
            "terminal_state": "manual_review"
        }
