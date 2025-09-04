import subprocess
from typing import Optional
from subprocess import PIPE

__all__ = [
    "git_path_setting",
]


def git_path_setting() -> Optional[str]:
    with subprocess.Popen(
        "git rev-parse --show-toplevel",
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    ) as p:
        assert p.stdout is not None, (
            "the directory (or any of the parent) seems not to be a git repository"  # noqa: E501
        )
        return p.stdout.read().strip()
