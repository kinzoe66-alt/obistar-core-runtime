import json
from pathlib import Path

from runtime.governed_cli.executor import (
    GovernedCLIExecutor
)

from runtime.governed_replay.replay_template import (
    ReplayTemplateBuilder
)


class SingleRouteReplayExecutor:

    def __init__(self, executor=None):

        self.executor = (
            executor
            or GovernedCLIExecutor()
        )

        self.templates = (
            ReplayTemplateBuilder()
        )

    def run(
        self,
        candidate,
        output_path=(
            "reports/replay/"
            "single_route_replay.json"
        ),
    ):

        template = (
            self.templates.build(
                candidate
            )
        )

        command = template["command"]

        result = self.executor.execute(
            command
        )

        artifact = {
            "candidate_id": (
                template[
                    "observation_id"
                ]
            ),

            "surface_id": (
                template[
                    "surface_id"
                ]
            ),

            "replay_sequence": [
                {
                    "step": 1,

                    "command": command,

                    "returncode": (
                        result.returncode
                    ),
                }
            ],

            "stdout": result.stdout,

            "stderr": result.stderr,

            "deterministic": (
                template[
                    "deterministic"
                ]
            ),

            "reproducible": (
                result.returncode
                == 0
            ),

            "manual_review_required": True,

            "autonomous_submission": False,
        }

        path = Path(output_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            json.dumps(
                artifact,
                indent=2
            ),
            encoding="utf-8",
        )

        return artifact
