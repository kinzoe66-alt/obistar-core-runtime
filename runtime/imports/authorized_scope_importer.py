import json
from pathlib import Path

from runtime.intake.surface_loader import GovernedSurfaceLoader

class AuthorizedScopeImporter:

    def import_file(self, path: str):
        source = Path(path)

        data = json.loads(
            source.read_text(encoding="utf-8")
        )

        admitted = GovernedSurfaceLoader().load(data)

        return {
            "source": str(source),
            "imported_count": len(admitted),
            "admitted_surfaces": admitted,
            "manual_review_required": True,
            "autonomous_submission": False
        }
