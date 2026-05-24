import json
from pathlib import Path

class OutcomeTracker:

    def write(
        self,
        surface_id: str,
        outcome: str,
        path="outcome_history/outcomes.sample.json"
    ):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)

        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
        else:
            data = {}

        data.setdefault(surface_id, [])
        data[surface_id].append(outcome)

        p.write_text(json.dumps(data, indent=2), encoding="utf-8")

        return {
            "surface_id": surface_id,
            "outcome": outcome,
            "manual_review_required": True,
            "autonomous_submission": False
        }
