import json
from pathlib import Path


class ReviewerCalibrationPersistence:

    def write(self, calibration, path="review_outcomes/reviewer_calibration.json"):

        payload = {
            "calibration": calibration,
            "manual_review_required": True,
            "autonomous_submission": False,
        }

        out = Path(path)
        out.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        out.write_text(
            json.dumps(payload, indent=2),
            encoding="utf-8",
        )

        return payload

    def read(self, path="review_outcomes/reviewer_calibration.json"):

        p = Path(path)

        if not p.exists():
            return {
                "calibration": {},
                "manual_review_required": True,
                "autonomous_submission": False,
            }

        return json.loads(
            p.read_text(encoding="utf-8")
        )
