import json
from pathlib import Path


class ReviewQueueExporter:

    def export(
        self,
        routes,
        packages,
        export_path="operational_outputs/latest/review_queue/export.json",
    ):
        output = {
            "route_count": len(routes),
            "package_count": len(packages),
            "routes": routes,
            "packages": packages,
            "manual_review_required": True,
            "confirmed_issue": False,
        }

        path = Path(export_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            json.dumps(
                output,
                indent=2,
                sort_keys=True
            )
        )

        return {
            "exported": True,
            "export_path": str(path),
            "route_count": len(routes),
            "package_count": len(packages),
            "manual_review_required": True,
            "confirmed_issue": False,
        }
