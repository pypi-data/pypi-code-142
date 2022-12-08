import unittest

import ClusterMimsy.hello as hello

class TestHello(unittest.TestCase):
    def test_is_string(self):
        s = hello.hello_name('James')
        self.assertTrue(isinstance(s, str))

if __name__ == '__main__':
    unittest.main()