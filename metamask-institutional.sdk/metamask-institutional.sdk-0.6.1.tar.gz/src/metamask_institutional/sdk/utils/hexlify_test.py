
import unittest

from metamask_institutional.sdk.utils.hexlify import hexlify


class HexlifyTest(unittest.TestCase):
    def test_hexlify_should_convert_hex_string_to_decimal_string(self):
        self.assertEqual(hexlify('0'), "0x0")
        self.assertEqual(hexlify('1'), "0x1")
        self.assertEqual(hexlify('42'), "0x2a")
        self.assertEqual(hexlify('89494464'), "0x55593c0")

    def test_hexlify_should_support_longs(self):
        self.assertEqual(hexlify('100000000000000000000000000000000000'), "0x13426172c74d822b878fe800000000")

    def test_hexlify_should_return_none_when_passed_none(self):
        self.assertEqual(hexlify(None), None)


if __name__ == "__main__":
    unittest.main()
