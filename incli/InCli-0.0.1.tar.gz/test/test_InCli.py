
#python3 -m unittest

import unittest
from src import InCli
from src.SFAPI import restClient

class Test_Main(unittest.TestCase):
    def test_main(self):
        InCli.main()
        self.assertEqual(1,1)

