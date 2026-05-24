import subprocess
from dataclasses import dataclass
from typing import List


ALLOWED_COMMANDS = {
    "curl",
    "python",
}


@dataclass
class CommandResult:
    command: List[str]
    returncode: int
    stdout: str
    stderr: str


class GovernedCLIExecutor:

    def validate(self, command: List[str]):

        if not command:
            raise ValueError("empty command")

        root = command[0]

        if root not in ALLOWED_COMMANDS:
            raise ValueError(
                f"disallowed command: {root}"
            )

    def execute(self, command: List[str]):

        self.validate(command)

        proc = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30
        )

        return CommandResult(
            command=command,
            returncode=proc.returncode,
            stdout=proc.stdout,
            stderr=proc.stderr,
        )
