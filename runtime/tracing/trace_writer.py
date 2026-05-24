import json

from pathlib import Path

from runtime.tracing.execution_trace import (
    ExecutionTraceBuilder
)

class TraceWriter:

    def write(
        self,
        output=(
            "reports/"
            "execution_trace.json"
        )
    ):

        artifact = (
            ExecutionTraceBuilder()
            .build()
        )

        path = Path(output)

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            json.dumps(
                artifact,
                indent=2
            ),
            encoding="utf-8"
        )

        return path
