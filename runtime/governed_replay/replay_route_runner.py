import json
from pathlib import Path

from runtime.governed_replay.single_route import (
    SingleRouteReplayExecutor
)

from runtime.governed_replay.replay_package import (
    ReplayRoutePackager
)


class GovernedReplayRouteRunner:

    def __init__(self):

        self.executor = (
            SingleRouteReplayExecutor()
        )

        self.packager = (
            ReplayRoutePackager()
        )

    def run(
        self,
        queue_path=(
            "reports/review_queue/"
            "governed_review_queue.json"
        ),
    ):

        queue = json.loads(
            Path(queue_path).read_text(
                encoding="utf-8"
            )
        )

        candidate = (
            queue["queue"][0]
        )

        replay = (
            self.executor.run(
                candidate
            )
        )

        package = (
            self.packager.build(
                candidate,
                replay,
            )
        )

        return {
            "candidate": candidate,

            "replay": replay,

            "package": package,

            "manual_review_required": True,

            "autonomous_submission": False,
        }
