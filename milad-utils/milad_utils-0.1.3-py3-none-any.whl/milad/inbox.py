import subprocess


def save_repo_status(path):
    with open(path / "git_commit.txt", "w") as f:
        subprocess.run(["git", "rev-parse", "HEAD"], stdout=f)

    with open(path / "workspace_changes.diff", "w") as f:
        subprocess.run(["git", "diff"], stdout=f)
