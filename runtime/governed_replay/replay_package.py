import json
from pathlib import Path


class ReplayRoutePackager:

    def build(
        self,
        candidate,
        replay_artifact,
        output_path=(
            "reports/replay/"
            "replay_route_package.json"
        ),
    ):

        package = {
            "candidate_id": (
                replay_artifact[
                    "candidate_id"
                ]
            ),

            "surface_id": (
                replay_artifact[
                    "surface_id"
                ]
            ),

            "replay_sequence": (
                replay_artifact[
                    "replay_sequence"
                ]
            ),

            "reproducible": (
                replay_artifact[
                    "reproducible"
                ]
            ),

            "deterministic": (
                replay_artifact[
                    "deterministic"
                ]
            ),

            "stdout": (
                replay_artifact[
                    "stdout"
                ]
            ),

            "stderr": (
                replay_artifact[
                    "stderr"
                ]
            ),

            "reviewer_ready": True,

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
                package,
                indent=2
            ),
            encoding="utf-8",
        )

        return package
