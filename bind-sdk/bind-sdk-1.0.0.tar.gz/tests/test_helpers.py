import unittest

from bind_sdk.helpers.is_alias import is_alias


class TestOptions(unittest.TestCase):
    def test_is_alias(self):
        self.assertTrue(is_alias("ELBARBACAJADEAHORRO"))
        self.assertFalse(is_alias("3220001801000020816200"))
