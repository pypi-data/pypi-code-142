#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT


import logging
from unittest import mock
import pytest
from test.test_builder import MockedStdout
from tuxtrigger import yamlload

from tuxtrigger.exceptions import TuxtriggerException
from tuxtrigger.inputvalidation import YamlValidator
from tuxtrigger.yamlload import (
    yaml_file_read,
    yaml_file_write,
    compare_sha,
    create_repo_list,
    create_dynamic_configuration,
)
from pathlib import Path

# from tuxtrigger.exceptions import TuxtriggerException

BASE = (Path(__file__) / "..").resolve()

ERROR_PATH = BASE / "./test_files/error_path.yaml"
HAPPY_PATH = BASE / "./test_files/happy_path.yaml"
FILE_TO_CREATE = BASE / "./test_files/new_file.yaml"
SCRIPT = BASE / ".test_files/test_script.sh"

VALUE_DICT = {
    "v5.19": {
        "sha": "2437f53721bcd154d50224acee23e7dbb8d8c622",
        "ref": "refs/tags/v5.19",
    }
}
VALUE = "v5.19"
RIGHT_KEY = "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git"
WRONG_KEY = "/linux-not-existing"

DYNAMIC_CONFIG = {
    "repositories": [
        {
            "url": "https://git.kernel.org/pub/scm/linux/kernel/git/tomba/linux.git",
            "squad_group": "~non.existing",
            "branches": [
                {
                    "name": "master",
                    "squad_project": "example_project",
                    "plan": "stable.yaml",
                },
                {
                    "name": "for-laurent",
                    "squad_project": "example_project",
                    "plan": "stable-next.yaml",
                },
            ],
        },
        {
            "url": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
            "squad_group": "~non.existing",
            "regex": "for-next/*",
            "default_plan": "default_plan",
            "squad_project_prefix": "testing",
            "branches": [
                {
                    "name": "master",
                    "squad_project": "example_project",
                    "plan": "stable.yaml",
                },
                {
                    "name": "v5.19",
                    "squad_project": "example_project",
                    "plan": "stable-next.yaml",
                },
                {
                    "name": "heads/test-next",
                    "squad_project": "testing-linux-heads-test-next",
                    "plan": "default_plan",
                },
            ],
        },
    ]
}


def test_yaml_file_read():
    assert type(yaml_file_read(ERROR_PATH)) == dict


def test_create_repo_list(repo_setup_good):
    assert isinstance(next(repo_setup_good), YamlValidator) is True
    assert repo_setup_good is not None
    with pytest.raises(TuxtriggerException) as exc:
        next(create_repo_list(None))
    assert "Data input is none" in str(exc)


def test_yaml_file_write(tmpdir):
    test_input = yaml_file_read(ERROR_PATH)
    yaml_file_write(test_input, (tmpdir / "test.yaml"))
    assert (tmpdir / "test.yaml").exists()


def test_compare_sha_correct(correct_archive_read):
    with pytest.raises(KeyError):
        compare_sha(WRONG_KEY, VALUE, VALUE_DICT, correct_archive_read)
    assert compare_sha(RIGHT_KEY, VALUE, VALUE_DICT, correct_archive_read) is True


def test_compare_sha_wrong(wrong_archive_read, correct_archive_read):
    assert compare_sha(WRONG_KEY, VALUE, VALUE_DICT, wrong_archive_read) is False
    assert compare_sha(RIGHT_KEY, VALUE, VALUE_DICT, wrong_archive_read) is False
    assert (
        compare_sha(RIGHT_KEY, "non_existing_value", VALUE_DICT, correct_archive_read)
        is False
    )


@mock.patch("tuxtrigger.yamlload.subprocess.run")
def test_run_lsremote(mock_run):
    ls_remote = MockedStdout(
        returncode=0,
        stdout="0066f1b0e27556381402db3ff31f85d2a2265858        refs/heads/master",
    )
    mock_run.return_value = ls_remote
    assert yamlload.run_lsremote(
        "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git", "master"
    ) == {
        "master": {
            "ref": "refs/heads/master",
            "sha": "0066f1b0e27556381402db3ff31f85d2a2265858",
        }
    }
    ls_remote_error = MockedStdout(returncode=1, stdout="", stderr="Serious Error")
    mock_run.return_value = ls_remote_error
    assert yamlload.run_lsremote(
        "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git", "master"
    ) == {"master": {"sha": "", "ref": ""}}


def test_pre_tux_run_none(correct_archive_read, caplog):
    with caplog.at_level(logging.INFO):
        yamlload.pre_tux_run(
            None,
            "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
            "v5.19",
            VALUE_DICT,
            correct_archive_read,
        )

    assert "No script path provided" in caplog.text


@mock.patch("tuxtrigger.yamlload.subprocess.run")
def test_pre_tux_run(mock_run, caplog, correct_archive_read):
    ls_remote = MockedStdout(returncode=0, stdout="Success")
    mock_run.return_value = ls_remote
    with caplog.at_level(logging.INFO):
        yamlload.pre_tux_run(
            "dummy_path", RIGHT_KEY, VALUE, VALUE_DICT, correct_archive_read
        )
    assert "performed astonishingly wonderful" in caplog.text

    ls_remote_not_zero = MockedStdout(returncode=1, stdout="", stderr="Failure")
    mock_run.return_value = ls_remote_not_zero
    with pytest.raises(TuxtriggerException) as exc:
        yamlload.pre_tux_run(
            "dummy_path", RIGHT_KEY, VALUE, VALUE_DICT, correct_archive_read
        )
    assert "Script was not invoked properly" in str(exc)


@mock.patch("tuxtrigger.yamlload.subprocess.run")
def test_run_lsremote_regex(mock_run):
    mocked_run = MockedStdout(
        returncode=0,
        stdout="0066f1b0e27556381402db3ff31f85d2a2265858\trefs/heads/test-next",
    )
    mock_run.return_value = mocked_run
    assert yamlload.run_lsremote_regex("example_repository", "example_regex*") == {
        "test-next": "0066f1b0e27556381402db3ff31f85d2a2265858"
    }

    mocked_run = MockedStdout(
        returncode=0,
        stdout="0066f1b0e27556381402db3ff31f85d2a2265858\trefs/heads/for/test-next",
    )
    mock_run.return_value = mocked_run
    assert yamlload.run_lsremote_regex("example_repository", "example_regex*") == {
        "for/test-next": "0066f1b0e27556381402db3ff31f85d2a2265858"
    }
    failed_run = MockedStdout(returncode=1, stdout="", stderr="ls remote failure")
    mock_run.return_value = failed_run
    assert yamlload.run_lsremote_regex("example_repository", "example_regex*") == {}


def test_create_dynamic_configuration_none():
    with pytest.raises(TuxtriggerException) as exc:
        create_dynamic_configuration(None)
    assert "Not able to generate data - config file not read" in str(exc)


@mock.patch("tuxtrigger.yamlload.run_lsremote_regex")
def test_create_dynamic_configuration(mock_run):
    mock_run.return_value = {
        "heads/test-next": "0066f1b0e27556381402db3ff31f85d2a2265858"
    }
    assert (
        yamlload.create_dynamic_configuration(yaml_file_read(HAPPY_PATH))
        == DYNAMIC_CONFIG
    )
