from runtime.tracing.execution_trace import (
    ExecutionTraceBuilder
)

def test_execution_trace():

    trace = (
        ExecutionTraceBuilder()
        .build()
    )

    assert "trace" in trace

    assert trace["trace"]

    first = trace["trace"][0]

    assert (
        "state_transition"
        in first
    )

    assert (
        trace["terminal_state"]
        == "manual_review"
    )
