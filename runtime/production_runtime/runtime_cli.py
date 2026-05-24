import argparse
import json

from runtime.production_runtime.governed_runtime import (
    GovernedProductionRuntime,
)


def main():
    parser = argparse.ArgumentParser(
        description="Governed production runtime"
    )

    parser.add_argument(
        "--candidates",
        required=True,
    )

    parser.add_argument(
        "--review-memory",
        required=True,
    )

    args = parser.parse_args()

    result = (
        GovernedProductionRuntime()
        .run(
            args.candidates,
            args.review_memory,
        )
    )

    print(
        json.dumps(
            result,
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
