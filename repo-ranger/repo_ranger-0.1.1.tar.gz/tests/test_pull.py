import os
import tempfile
from unittest.mock import call, patch
from argparse import Namespace
import yaml

import pytest

from repo_ranger import pull


@patch("subprocess.run")
def test_pull(mock_run, capsys):
    # Set up the test configuration and arguments
    temp_folder = tempfile.mkdtemp()

    # Set up the test configuration and arguments
    config = {
        "root_folder": temp_folder,
        "repositories": [
            {
                "name": "project-frontend",
                "url": "https://github.com/user/project-frontend.git",
                "path": "project/frontend",
                "summary": "This repository contains the frontend code for the project.",
                "tags": ["web", "frontend"],
            },
            {
                "name": "project-backend",
                "url": "https://github.com/user/project-backend.git",
                "path": "project/backend",
                "summary": "This repository contains the backend code for the project.",
                "tags": ["api", "backend"],
            },
            {
                "name": "project-docs",
                "url": "https://github.com/user/project-docs.git",
                "path": "project/docs",
                "summary": "This repository contains the documentation for the project.",
                "tags": ["docs"],
            },
        ],
    }

    # Create a temporary configuration file
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        yaml.dump(config, f)

    args = Namespace(
        command="pull",
        config=f.name,
        include=None,
        exclude=None,
    )

    # Create the expected repository folders
    os.makedirs(os.path.join(temp_folder, "project/frontend"))
    os.makedirs(os.path.join(temp_folder, "project/backend"))
    os.makedirs(os.path.join(temp_folder, "project/docs"))

    # Call the pull function
    pull(args)

    # Check that the subprocess.run function was called with the correct arguments
    mock_run.assert_has_calls(
        [
            call(
                [
                    "git",
                    "-C",
                    os.path.join(temp_folder, "project/frontend"),
                    "pull",
                    "--rebase",
                ]
            ),
            call(
                [
                    "git",
                    "-C",
                    os.path.join(temp_folder, "project/backend"),
                    "pull",
                    "--rebase",
                ]
            ),
            call(
                [
                    "git",
                    "-C",
                    os.path.join(temp_folder, "project/docs"),
                    "pull",
                    "--rebase",
                ]
            ),
        ]
    )

    # Check that the correct log messages were printed
    out, err = capsys.readouterr()
    assert out == (
        "Pulling changes for repository project-frontend...\n"
        "Pulling changes for repository project-backend...\n"
        "Pulling changes for repository project-docs...\n"
    )

    # Clean up the temporary folder
    os.rmdir(os.path.join(temp_folder, "project/frontend"))
    os.rmdir(os.path.join(temp_folder, "project/backend"))
    os.rmdir(os.path.join(temp_folder, "project/docs"))
    os.rmdir(os.path.join(temp_folder, "project"))

    # Call the pull function
    pull(args)
    # Check that the correct log message was printed
    out, err = capsys.readouterr()
    assert out == (
        "Repository project-frontend not found at {}/project/frontend\n"
        "Repository project-backend not found at {}/project/backend\n"
        "Repository project-docs not found at {}/project/docs\n"
    ).format(temp_folder, temp_folder, temp_folder)


@patch("subprocess.run")
def test_pull_with_include(mock_run, capsys):
    # Set up the test configuration and arguments
    temp_folder = tempfile.mkdtemp()

    # Set up the test configuration and arguments
    config = {
        "root_folder": temp_folder,
        "repositories": [
            {
                "name": "project-frontend",
                "url": "https://github.com/user/project-frontend.git",
                "path": "project/frontend",
                "summary": "This repository contains the frontend code for the project.",
                "tags": ["web", "frontend"],
            },
            {
                "name": "project-backend",
                "url": "https://github.com/user/project-backend.git",
                "path": "project/backend",
                "summary": "This repository contains the backend code for the project.",
                "tags": ["api", "backend"],
            },
            {
                "name": "project-docs",
                "url": "https://github.com/user/project-docs.git",
                "path": "project/docs",
                "summary": "This repository contains the documentation for the project.",
                "tags": ["docs"],
            },
        ],
    }

    # Create a temporary configuration file
    with tempfile.NamedTemporaryFile("w", delete=False) as f:
        yaml.dump(config, f)
    # Create the expected repository folder
    os.makedirs(os.path.join(temp_folder, "project/frontend"))

    args = Namespace(
        command="pull",
        config=f.name,
        include=["frontend"],
        exclude=None,
    )

    # Call the pull function with include flag
    pull(args)

    # Check that the subprocess.run function was called with the correct arguments
    mock_run.assert_called_once_with(
        ["git", "-C", os.path.join(temp_folder, "project/frontend"), "pull", "--rebase"]
    )

    # Check that the correct log message was printed
    out, err = capsys.readouterr()
    assert out == "Pulling changes for repository project-frontend...\n"

    # Clean up the temporary folder
    os.rmdir(os.path.join(temp_folder, "project/frontend"))
    os.rmdir(os.path.join(temp_folder, "project"))
