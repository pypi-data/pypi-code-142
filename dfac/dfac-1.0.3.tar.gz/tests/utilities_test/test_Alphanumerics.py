import unittest

from dfac.utilities.Alphanumerics import Alphanumerics

class AlphanumericsTestMethoods(unittest.TestCase):
    def test_ASCII_decimals(self):
        ascii = Alphanumerics()
        self.assertEqual(ascii.lowercase_ascii_start,97)
        self.assertEqual(ascii.lowercase_ascii_end,122)
        self.assertEqual(ascii.uppercase_ascii_start,65)
        self.assertEqual(ascii.uppercase_ascii_end,90)
        self.assertEqual(ascii.ascii_symbols,[[32,47],[91,96],[123,126]])

    
    def test_alphalower(self):
        lower = Alphanumerics()
        l=lower.alphalower()
        self.assertEqual(l[0],'a')
        self.assertEqual(l[12],'m')
        self.assertEqual(l[25],'z')
        print("test_alphalower")
        print(l)

    def test_alphaupper(self):
        upper = Alphanumerics()
        l=upper.alphaupper()
        self.assertEqual(l[0],'A')
        self.assertEqual(l[12],'M')
        self.assertEqual(l[25],'Z')
        print("test_alphaupper")
        print(l)
    
    def test_symbols(self):
        sym = Alphanumerics()
        l=sym.symbols()
        self.assertEqual(l[0],chr(32))
        self.assertEqual(l[19],chr(94))
        self.assertEqual(l[25],chr(126))
        print("test_symbols")
        print(l)
    
    def test_numeric(self):
        sym = Alphanumerics()
        l=sym.numeric()
        self.assertEqual(l[0],'0')
        self.assertEqual(l[5],'5')
        self.assertEqual(l[9],'9')
        print("test_numeric")
        print(l)
