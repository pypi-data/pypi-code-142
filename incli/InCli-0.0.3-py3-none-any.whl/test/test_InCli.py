
#python3 -m unittest

import unittest
from InCli import InCli
from InCli.SFAPI import restClient

class Test_Main(unittest.TestCase):
    def test_main(self):
        InCli.main()
        self.assertEqual(1,1)

