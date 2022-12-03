#
# Copyright 2019 Stephan Müller
#
# Licensed under the MIT license

"""Tests for ``pylint_gitlab.reporter``."""

import json
import os
from io import StringIO

import pytest
from pylint.lint import PyLinter


@pytest.mark.parametrize("reporter_name", ["gitlab-pages-html", "pylint_gitlab.GitlabPagesHtmlReporter"])
def test_gitlab_pages_html_reporter(reporter_name):
    """Tests for ``pylint_gitlab.reporter.GitlabPagesHtmlReporter()``."""

    output = StringIO()
    linter = PyLinter()

    linter.load_plugin_modules(["pylint_gitlab"])
    linter.set_option("output-format", reporter_name)
    linter.set_option("persistent", False)
    linter.load_default_plugins()

    reporter = linter.reporter
    reporter.out = output
    reporter.CI_PROJECT_URL = "https://example.org"
    reporter.CI_COMMIT_REF_NAME = "branch"

    linter.open()

    linter.set_current_module("b")
    linter.add_message("line-too-long", line=2, args=(1, 2))
    linter.add_message("line-too-long", line=1, args=(1, 2))

    linter.set_current_module("a")
    linter.add_message("line-too-long", line=1, args=(1, 2))

    # we call this method because we didn't actually run the checkers
    reporter.display_messages(None)

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "report.html"), "r", encoding="UTF-8") as file:
        expected_result = file.read()
    assert output.getvalue() == expected_result


@pytest.mark.parametrize("reporter_name", ["gitlab-codeclimate", "pylint_gitlab.GitlabCodeClimateReporter"])
def test_gitlab_code_climate_reporter(reporter_name):
    """Tests for ``pylint_gitlab.reporter.GitlabCodeClimateReporter()``."""

    output = StringIO()
    linter = PyLinter()

    linter.load_plugin_modules(["pylint_gitlab"])
    linter.set_option("output-format", reporter_name)
    linter.set_option("persistent", False)
    linter.load_default_plugins()

    reporter = linter.reporter
    reporter.out = output

    linter.open()

    linter.set_current_module("0123")
    linter.add_message("line-too-long", line=1, args=(1, 2))

    # we call this method because we didn't actually run the checkers
    reporter.display_messages(None)

    expected_result = [{
        "type": "issue",
        "check_name": "C0301",
        "description": "C0301: Line too long (1/2)",
        "categories": ["Style"],
        "severity": "minor",
        "location": {
            "path": "0123",
            "lines": {
                "begin": 1,
            }
        },
        "fingerprint": "53f7bfa250a245d85c191a637c555e04743644af0a1756687a6db8695eab9f86"
    }]
    report_result = json.loads(output.getvalue())
    assert report_result == expected_result


@pytest.mark.parametrize(
    "reporter_name",
    ["gitlab-codeclimate-nohash", "pylint_gitlab.GitlabCodeClimateReporterNoHash"]
)
def test_gitlab_code_climate_reporter_no_hash(reporter_name):
    """Tests for ``pylint_gitlab.reporter.GitlabCodeClimateReporterNoHash()``."""

    output = StringIO()
    linter = PyLinter()

    linter.load_plugin_modules(["pylint_gitlab"])
    linter.set_option("output-format", reporter_name)
    linter.set_option("persistent", False)
    linter.load_default_plugins()

    reporter = linter.reporter
    reporter.out = output

    linter.open()

    linter.set_current_module("0123")
    linter.add_message("line-too-long", line=1, args=(1, 2))

    # we call this method because we didn't actually run the checkers
    reporter.display_messages(None)

    expected_result = [{
        "type": "issue",
        "check_name": "C0301",
        "description": "C0301: Line too long (1/2)",
        "categories": ["Style"],
        "severity": "minor",
        "location": {
            "path": "0123",
            "lines": {
                "begin": 1,
            }
        },
        "fingerprint": "0123:1:C0301"
    }]
    report_result = json.loads(output.getvalue())
    assert report_result == expected_result
