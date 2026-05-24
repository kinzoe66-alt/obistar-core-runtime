import json
from pathlib import Path

class OutcomeHistory:

    def load(self, path="outcome_history/outcomes.sample.json"):
        source = Path(path)

        if not source.exists():
            return {}

        return json.loads(
            source.read_text(encoding="utf-8")
        )

    def outcomes_for(
        self,
        surface_id: str,
        path="outcome_history/outcomes.sample.json"
    ):
        return self.load(path).get(
            surface_id,
            []
        )
