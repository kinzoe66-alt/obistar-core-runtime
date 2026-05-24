import argparse
import json
from pathlib import Path

from runtime.review_adjudication.outcome_ingestion import (
    ReviewOutcomeIngestor,
)

from runtime.review_adjudication.review_memory import (
    ReviewMemoryBuilder,
)


def main():
    parser = argparse.ArgumentParser(
        description="Governed review adjudication loop"
    )

    parser.add_argument(
        "command",
        choices=[
            "ingest-outcome",
            "build-memory",
        ],
    )

    parser.add_argument(
        "--file",
        required=False,
    )

    args = parser.parse_args()

    if args.command == "ingest-outcome":
        if not args.file:
            raise SystemExit("--file is required for ingest-outcome")

        record = json.loads(Path(args.file).read_text())

        result = ReviewOutcomeIngestor().ingest(record)

        print(json.dumps(result, indent=2, sort_keys=True))

    if args.command == "build-memory":
        result = ReviewMemoryBuilder().build()

        Path("review_outcomes").mkdir(parents=True, exist_ok=True)

        Path("review_outcomes/review_memory.json").write_text(
            json.dumps(result, indent=2, sort_keys=True)
        )

        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
