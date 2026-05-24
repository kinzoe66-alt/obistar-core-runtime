import json
from pathlib import Path

from runtime.comparison.comparison_runner import GovernedComparisonRunner
from runtime.meaning.translator import OperationalMeaningTranslator

class OperationalMeaningReport:

    def write(self, output="reports/meaning/operational_meaning.json"):
        comparison = GovernedComparisonRunner().run()
        translated = OperationalMeaningTranslator().translate_results(
            comparison["results"]
        )

        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(translated, indent=2),
            encoding="utf-8"
        )

        return path
