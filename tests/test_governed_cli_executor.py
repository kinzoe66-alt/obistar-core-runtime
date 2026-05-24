import pytest

from runtime.governed_cli.executor import (
    GovernedCLIExecutor
)


def test_rejects_disallowed_command():

    executor = GovernedCLIExecutor()

    with pytest.raises(ValueError):
        executor.execute(["rm", "-rf", "/"])


def test_executes_allowed_command():

    executor = GovernedCLIExecutor()

    result = executor.execute([
        "python",
        "--version"
    ])

    assert result.returncode == 0
