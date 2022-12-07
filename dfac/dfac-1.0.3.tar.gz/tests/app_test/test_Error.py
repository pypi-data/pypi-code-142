import unittest
from dfac.app.Error import Error 

class ErrorTestMethod(unittest.TestCase):

    def test_print_error(self):
        val=1
        with self.assertRaises(TypeError):
            Error().print_error(val)
    
