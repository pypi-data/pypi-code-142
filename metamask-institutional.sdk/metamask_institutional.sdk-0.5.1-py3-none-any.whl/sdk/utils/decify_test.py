
import unittest

from metamask_institutional.sdk.utils.decify import decify


class DecifyTest(unittest.TestCase):
    def test_decify_should_convert_hex_string_to_decimal_string(self):
        self.assertEqual(decify('0x0'), "0")
        self.assertEqual(decify('0x1'), "1")
        self.assertEqual(decify('0x2a'), "42")
        self.assertEqual(decify('0x55593c0'), "89494464")

    def test_decify_should_support_longs(self):
        self.assertEqual(decify('0x13426172c74d822b878fe800000000'), "100000000000000000000000000000000000")

    def test_decify_should_return_none_when_passed_none(self):
        self.assertEqual(decify(None), None)


if __name__ == "__main__":
    unittest.main()
