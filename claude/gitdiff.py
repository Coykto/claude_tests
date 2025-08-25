import os
import subprocess
from pathlib import Path


def write_git_diff(
    repo_path: str,
    output_file: Path,
    left_branch: str,
    right_branch: str = "main",
    file_extension: str = "py"
):
    with open(output_file.resolve(), "w") as file:
        os.chdir(repo_path)

        command = [f"git diff {left_branch} {right_branch} '*.{file_extension}'"]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()

        file.write(out.decode())
