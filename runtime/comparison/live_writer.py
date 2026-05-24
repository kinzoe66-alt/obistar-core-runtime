import json
from pathlib import Path

from runtime.comparison.live_runner import LiveGovernedRunner

class LiveGovernedWriter:

    def write(
        self,
        scope_file: str,
        output="reports/live/governed_live_result.json"
    ):
        result = LiveGovernedRunner().run(scope_file)

        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(result, indent=2),
            encoding="utf-8"
        )

        return path
