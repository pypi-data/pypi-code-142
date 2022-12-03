#!/usr/bin/env python
"""Tests for `py_cover_letters` package."""

from click.testing import CliRunner

from py_cover_letters import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    result_details = result.output.split('\n')
    for i, r in enumerate(result_details):
        print(f'assert result_details[{i}] == \'{r}\'')
    assert result_details[0] == 'Usage: main [OPTIONS] COMMAND [ARGS]...'
    assert result_details[1] == ''
    assert result_details[2] == 'Options:'
    assert result_details[3] == '  --version  Show the version and exit.'
    assert result_details[4] == '  --help     Show this message and exit.'
    assert result_details[5] == ''
    assert result_details[6] == 'Commands:'
    assert result_details[7] == '  about   About this application.'
    assert result_details[8] == '  config  Configure the application.'
    assert result_details[9] == '  create  Create cover letters from master Excel file.'
    assert result_details[10] == '  email   Email cover letters.'
    assert result_details[11] == ''


def test_config_show():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['config', 'show'], input='\n'.join('N'))
    print('>>>', result.output)
