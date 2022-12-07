import unittest
from dfac.inout.FileGenerator import FileGenerator

class FileGeneratorTestMethods(unittest.TestCase):
    
    def test_filegeneration(self):
        FileGenerator().print_out("Test Message","test_print") 