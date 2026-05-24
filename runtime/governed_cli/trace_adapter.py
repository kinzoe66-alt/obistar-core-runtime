from runtime.governed_cli.executor import GovernedCLIExecutor


class GovernedCLITraceAdapter:

    def __init__(self, executor=None):
        self.executor = executor or GovernedCLIExecutor()

    def run_for_trace(self, command, step_name="governed_cli_validation"):
        result = self.executor.execute(command)

        return {
            "step": step_name,
            "command": result.command,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "manual_review_required": True,
            "autonomous_submission": False,
        }
