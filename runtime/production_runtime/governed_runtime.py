import json
from pathlib import Path

from runtime.operational_loop.governed_operational_loop import (
    GovernedOperationalLoop,
)


class GovernedProductionRuntime:

    def run(
        self,
        candidate_path,
        review_memory_path,
    ):
        candidates = json.loads(
            Path(candidate_path).read_text()
        )

        review_memory = json.loads(
            Path(review_memory_path).read_text()
        )

        result = (
            GovernedOperationalLoop()
            .execute(
                candidates,
                review_memory,
            )
        )

        output_path = Path(
            "operational_outputs/latest/runtime/runtime_execution.json"
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        output_path.write_text(
            json.dumps(
                result,
                indent=2,
                sort_keys=True,
            )
        )

        return {
            "runtime_completed": True,
            "output_path": str(output_path),
            "candidate_count": len(candidates),
            "manual_review_required": True,
            "confirmed_issue": False,
        }
