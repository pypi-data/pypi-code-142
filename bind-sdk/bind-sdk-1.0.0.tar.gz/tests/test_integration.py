import unittest

from bind_sdk.sdk import Sdk


class TestIntegration(unittest.TestCase):
    def test_get_transfers(self):
        sdk = Sdk()
        t = sdk.get_transfers("21-1-99999-4-6")
        self.assertTrue(type(t) == list)

    def test_get_transfer(self):
        sdk = Sdk()
        t = sdk.get_transfer("1-31252804-015114433092974-0", "21-1-99999-4-6")
        self.assertTrue(type(t) == dict)
