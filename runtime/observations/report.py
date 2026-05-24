import json
from pathlib import Path

from runtime.observations.selector import ObservationSelector

class ObservationSelectionReport:

    def write(self, output="reports/observations/observation_selection.json"):
        result = ObservationSelector().select()

        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(result, indent=2),
            encoding="utf-8"
        )

        return path
