from runtime.tracing.trace_writer import (
    TraceWriter
)

def test_trace_writer(tmp_path):

    output = (
        tmp_path /
        "execution_trace.json"
    )

    path = (
        TraceWriter()
        .write(str(output))
    )

    assert path.exists()
