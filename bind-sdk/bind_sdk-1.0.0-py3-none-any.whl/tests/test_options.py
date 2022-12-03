import unittest

from bind_sdk.options.concept import Concept
from bind_sdk.options.currency import Currency


class TestOptions(unittest.TestCase):
    def test_concepts(self):
        self.assertEqual(Concept.ALQ, "ALQ")
        self.assertEqual(len(Concept), 9)
        self.assertTrue("VAR" in dir(Concept))
        self.assertFalse(False in [len(i.value) == 3 for i in Concept])

    def test_currencies(self):
        self.assertEqual(Currency.ARS, "ARS")
        self.assertEqual(len(Currency), 2)
        self.assertTrue("USD" in dir(Currency))
        self.assertFalse(False in [len(i.value) == 3 for i in Currency])
