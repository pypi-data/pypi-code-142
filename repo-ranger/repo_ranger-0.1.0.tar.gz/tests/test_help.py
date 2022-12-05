import pytest
import io
import contextlib

from repo_ranger import help


def test_help():
    # Define the args
    args = ["-c", "/path/to/config.yml"]

    # Capture the output of the help function
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        help(args)

    # Assert that the correct usage message is printed
    expected_output = (
        "Usage: repo_ranger [OPTIONS] COMMAND [ARGS]...\n"
        "\n"
        "Commands:\n"
        "  init      Create a new configuration file\n"
        "  list      List the configured repositories\n"
        "  clone     Clone the specified repositories\n"
        "  pull      Pull the specified repositories\n"
        "  help      Show this message and exit\n"
        "\n"
        "Options:\n"
        "  -c, --config FILE\tPath to the configuration file\n"
        "\n"
    )
    assert output.getvalue() == expected_output
