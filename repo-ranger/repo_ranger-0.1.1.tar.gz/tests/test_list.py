import io
import os
import pytest
import yaml
import sys
import tempfile

from argparse import Namespace
from repo_ranger import list_repos


@pytest.fixture
def args():
    """
    Fixture that returns the parsed arguments for the "list" command.
    """
    return Namespace(
        command="list", config="repo_ranger.yaml", exclude=None, include=None
    )


@pytest.fixture
def empty_config():
    """
    Fixture that returns the content of an empty configuration file.
    """
    return {"root": "repos", "repositories": []}


@pytest.fixture
def filled_config():
    """
    Fixture that returns the content of a configuration file with some
    repositories.
    """
    return {
        "root": "repos",
        "repositories": [
            {
                "path": "repos/org1",
                "name": "repo1",
                "summary": "A repository with some code",
                "tags": ["tag1", "tag2"],
            },
            {
                "path": "repos/org1/suborg1",
                "name": "repo2",
                "summary": "Another repository with some code",
                "tags": ["tag2", "tag3"],
            },
        ],
    }


def test_empty_config(args, empty_config):
    # Create a temporary configuration file
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        yaml.dump(empty_config, f)

    # Update the config path in the arguments
    args.config = f.name

    # Capture the standard output
    out = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = out

    # Call the "list" subcommand
    list_repos(args)

    # Restore the standard output
    sys.stdout = old_stdout
    result = out.getvalue()

    # Assert that the list of repositories is empty
    assert result == ""

    # Remove the temporary configuration file
    os.remove(args.config)


def test_filled_config(args, filled_config):
    # Create a temporary configuration file
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        yaml.dump(filled_config, f)

    # Update the config path in the arguments
    args.config = f.name

    # Capture the standard output
    out = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = out

    # Call the "list" subcommand
    list_repos(args)

    # Restore the standard output
    sys.stdout = old_stdout
    result = out.getvalue()

    # Assert that the list of repositories is not empty
    assert result != ""

    # Parse the output into lines
    lines = result.strip().split("\n")

    # Assert that the number of lines is equal to the number of repositories
    assert len(lines) == len(filled_config["repositories"])

    # Assert that each line matches the expected format
    for line, repo in zip(lines, filled_config["repositories"]):
        assert line == (
            f"{repo['path']} {repo['name']} - {repo['summary']} "
            f"[{', '.join(repo['tags'])}]"
        )

    # Remove the temporary configuration file
    os.remove(args.config)
