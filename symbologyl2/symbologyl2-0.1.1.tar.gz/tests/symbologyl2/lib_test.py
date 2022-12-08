# pylint: disable=missing-docstring

import unittest

import symbologyl2


class TestLib(unittest.TestCase):
    def test_from_any_to_root(self):
        self.assertEqual("TEST", symbologyl2.from_any_to_root("TEST A"))

    def test_from_any_to_cms(self):
        self.assertEqual("TEST A", symbologyl2.from_any_to_cms("TEST.A"))

    def test_from_any_to_cqs(self):
        self.assertEqual("TEST.A", symbologyl2.from_any_to_cqs("TEST A"))

    def test_from_any_to_nasdaq_integrated(self):
        self.assertEqual("TEST.A", symbologyl2.from_any_to_nasdaq_integrated("TEST A"))

    def test_from_any_to_cms_suffix(self):
        self.assertEqual("A", symbologyl2.from_any_to_cms_suffix("TEST.A"))

    def test_from_any_to_cqs_suffix(self):
        self.assertEqual(".A", symbologyl2.from_any_to_cqs_suffix("TEST A"))

    def test_from_any_to_nasdaq_suffix(self):
        self.assertEqual(".A", symbologyl2.from_any_to_nasdaq_suffix("TEST A"))
