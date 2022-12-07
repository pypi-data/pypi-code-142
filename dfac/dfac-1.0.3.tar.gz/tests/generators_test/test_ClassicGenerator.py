import unittest
import random
from dfac.generators.ClassicGenerator import ClassicGenerator

class ClassicGeneratorTestMethods(unittest.TestCase):
    def test_default_init(self):
         default = ClassicGenerator()
         self.assertEqual(default.getLength(),10)
         self.assertEqual(default.getType(),1)
    
    def test_defined_init(self):
        __types=['Integer','String','Decimal']
        length=random.randint(0,100)
        dtype=random.randint(1,3)
        defined = ClassicGenerator(length,__types[dtype-1])
        self.assertEqual(defined.getLength(),length)
        self.assertEqual(defined.getType(),dtype)
