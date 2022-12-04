"""
SPDX-FileCopyrightText: 2022. Thomas Mahe <contact@tmahe.dev>
SPDX-License-Identifier: MIT

This work is licensed under the terms of the MIT license.
For a copy, see <https://opensource.org/licenses/MIT>.
"""

import io
from unittest import TestCase

from volunor.core.cli import Cli


class CliTestCase(TestCase):
    cli: Cli = None
    descriptor = None

    stderr: io.StringIO
    stdout: io.StringIO

    @classmethod
    def setUpClass(cls):
        cls.cli = Cli(prog=cls.__name__, descriptor=cls.descriptor)

    def setUp(self):
        self.stdout = io.StringIO()
        self.stderr = io.StringIO()

    def assertStdoutEqual(self, expected):
        self.assertEqual(expected, self.stdout.getvalue())

    def flush_stdout(self):
        self.stdout = io.StringIO()
