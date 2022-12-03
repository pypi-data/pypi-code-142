import unittest

import ClusterMimsy as cm

class TestHello(unittest.TestCase):
    def test_is_string(self):
        s = cm.hello.hello_name('James')
        self.assertTrue(isinstance(s, str))

if __name__ == '__main__':
    unittest.main()