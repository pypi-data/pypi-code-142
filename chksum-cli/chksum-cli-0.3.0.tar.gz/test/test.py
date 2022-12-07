import unittest
from src.chksum_cli import chksum


class TestCompareHashes(unittest.TestCase):
    def test_Match(self):
        method = 'md5'
        hashes = ['123456789abcdef', '123456789abcdef']
        chksum.compareHashes()

    def test_NoMatch(self):
        method = 'md5'
        hashes = ['123475689abcdef', '12356789abc4def']
        chksum.compareHashes()
    
    def test_Larger1(self):
        method = 'md5'
        hashes = ['123456789abcdef', '123456789']
        chksum.compareHashes()
    
    def test_Larger2(self):
        method = 'md5'
        hashes = ['123456789', '123456789abcdef']
        chksum.compareHashes()
    
    def test_WayOff(self):
        method = 'md5'
        hashes = ['123475689abc', '12356789aBc4def']
        chksum.compareHashes()


class TestPocessing(unittest.TestCase):
    def test_MD5(self):
        actual = chksum.setAlgorithm('md5')
        self.assertEqual(actual, True)

    def test_SHA1(self):
        actual = chksum.setAlgorithm('sha1')
        self.assertEqual(actual, True)

    def test_SHA256(self):
        actual = chksum.setAlgorithm('sha256')
        self.assertEqual(actual, True)
    
    def test_junk(self):
        actual = chksum.setAlgorithm('junk')
        self.assertEqual(actual, False)