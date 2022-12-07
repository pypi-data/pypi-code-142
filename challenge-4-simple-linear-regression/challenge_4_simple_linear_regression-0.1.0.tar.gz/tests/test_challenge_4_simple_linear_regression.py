#!/usr/bin/env python

"""Tests for `challenge_4_simple_linear_regression` package."""


import unittest
from click.testing import CliRunner

from challenge_4_simple_linear_regression import challenge_4_simple_linear_regression
from challenge_4_simple_linear_regression import cli


class TestChallenge_4_simple_linear_regression(unittest.TestCase):
    """Tests for `challenge_4_simple_linear_regression` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'challenge_4_simple_linear_regression.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
