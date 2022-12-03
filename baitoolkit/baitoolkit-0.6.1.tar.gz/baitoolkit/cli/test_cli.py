# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import unittest

import click


@click.group()
def test_group():
    """Execute unit test and generate reports."""


def run_tests(directory, pattern='test_*.py', verbosity=2):
    """run unit test cases under directory."""
    tests = unittest.TestLoader().discover(directory, pattern=pattern)
    unittest.TextTestRunner(verbosity=verbosity).run(tests)


@test_group.command(name='run')
@click.option('-d', '--directory', default=None, help='Locale directory of babel.')
@click.option('-p', '--pattern', default='test_*.py', help='The discovery pattern to be testing.')
@click.option('-v', '--verbosity', default=2, help='Test verbosity, 0-Silent, 1-Default, 2-Detailed.',
              show_default=True)
def run(directory, pattern, verbosity):
    run_tests(directory, pattern=pattern, verbosity=verbosity)


@test_group.command(name='coverage')
@click.option('-d', '--directory', default=None, help='Locale directory of babel.')
@click.option('-p', '--pattern', default='test_*.py', help='The discovery pattern to be testing.')
@click.option('-v', '--verbosity', default=2, help='Test verbosity, 0-Silent, 1-Default, 2-Detailed.',
              show_default=True)
@click.option('-s', '--source_pkgs', default=None, help='Source packages of coverage.', show_default=False)
@click.option('-m', '--show_missing', default=True, help='Show missing lines of coverage.', show_default=True)
def coverage(directory, pattern, verbosity, source_pkgs, show_missing):
    """Run unit tests and generate coverage report."""
    import coverage
    cov = coverage.Coverage(cover_pylib=False, source_pkgs=source_pkgs)
    cov.start()
    run_tests(directory, pattern=pattern, verbosity=verbosity)
    cov.stop()
    cov.report(show_missing=show_missing)
    cov.html_report()
