import pytest
from unittest import mock
import tempfile
import yaml
from argparse import Namespace
import os

from repo_ranger import clone


@mock.patch("subprocess.run")
def test_clone(mock_run):
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
        command="clone",
        config=f.name,
        include=None,
        exclude=None,
    )

    # Call the clone function
    clone(args)

    # Check that the subprocess.run function was called with the correct arguments
    mock_run.assert_has_calls(
        [
            mock.call(
                [
                    "git",
                    "clone",
                    "https://github.com/user/project-frontend.git",
                    os.path.join(temp_folder, "project/frontend"),
                ]
            ),
            mock.call(
                [
                    "git",
                    "clone",
                    "https://github.com/user/project-backend.git",
                    os.path.join(temp_folder, "project/backend"),
                ]
            ),
            mock.call(
                [
                    "git",
                    "clone",
                    "https://github.com/user/project-docs.git",
                    os.path.join(temp_folder, "project/docs"),
                ]
            ),
        ]
    )

    # Remove the temporary configuration file
    os.remove(args.config)
