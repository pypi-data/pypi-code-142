import os
import pytest
import yaml

from repo_ranger import init


@pytest.fixture
def args():
    """
    Fixture that returns the parsed arguments for the "init" command.
    """
    return {"command": "init", "config": None, "exclude": None, "include": None}


def test_init(tmp_path):
    # Create a temporary directory for the test
    tmp_dir = tmp_path / "repo_ranger"
    tmp_dir.mkdir()

    # Change the current working directory to the temporary directory
    os.chdir(tmp_dir)

    # Create the default configuration file
    init(None)

    # Check if the configuration file was created
    config_file = tmp_dir / "repo_ranger.yaml"
    assert config_file.exists()

    # Check if the default configuration was written to the file
    with open(config_file, "r") as f:
        config = f.read()

    expected_config = (
        "# Configuration file for the repo_ranger app\n"
        "# See https://github.com/user/repo_ranger for details\n"
        "\n"
        "repositories: []\n"
        "root: repos\n"
    )

    assert config == expected_config


def test_init_creates_config_file(args):
    """
    Test that the "init" subcommand creates the default configuration file.
    """
    # Run the "init" subcommand
    init(args)

    # Assert that the configuration file was created
    assert os.path.exists("repo_ranger.yaml")


def test_init_writes_default_config(args):
    """
    Test that the "init" subcommand writes the default configuration to the
    configuration file.
    """
    # Run the "init" subcommand
    init(args)

    # Read the configuration file
    with open("repo_ranger.yaml") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # Assert that the default configuration was written to the file
    assert config == {"root": "repos", "repositories": []}
