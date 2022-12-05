"""
@author axiner
@version v1.0.0
@created 2022/12/5 12:12
@abstract
@description
@history
"""
import unittest

from rbt import here


class TestDebug(unittest.TestCase):

    def test_001(self):
        print(here)
