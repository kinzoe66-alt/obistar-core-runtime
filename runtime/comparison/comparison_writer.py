import json
from pathlib import Path

from runtime.comparison.comparison_runner import GovernedComparisonRunner

class ComparisonWriter:

    def write(self, output="reports/comparison/governed_comparison.json"):
        result = GovernedComparisonRunner().run()
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        return path
