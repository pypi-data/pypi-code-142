import unittest
from dfac.inout.Display import Display

class DisplatTestMethods(unittest.TestCase):
    
    def test_Print(self):
        print("test_Print")
        Display().print_out("Test Message")