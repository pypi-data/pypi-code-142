import unittest
import random
from dfac.core.ArrayGenerator import ArrayGenerator 

class ArrayGeneratorTestMethods(unittest.TestCase):
    def test_AllArrayGenerators(self):
        types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5, 'Integer':6,'Decimal':7, 'Symbolic':8}
        for x in types:
            length=random.randint(1,100)
            high=random.randint(50,100)
            low=random.randint(1,50)
            argen=ArrayGenerator(length,x,low,high)
            print(x)
            print(argen.generate())
            print()
