import json
from pathlib import Path

from runtime.operations.feedback import OperationalFeedbackBuilder

class OperationalFeedbackWriter:

    def write(
        self,
        scope_file: str,
        output="reports/operations/operational_feedback.json"
    ):
        result = OperationalFeedbackBuilder().build(scope_file)

        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(result, indent=2),
            encoding="utf-8"
        )

        return path
