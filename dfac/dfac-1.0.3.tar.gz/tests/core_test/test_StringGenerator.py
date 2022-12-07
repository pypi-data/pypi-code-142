import unittest

from dfac.core.StringGenerator import StringGenerator
import random

class StingGeneratorTestMethods(unittest.TestCase):

    __types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5}


    def test_print_all_Generation_and_test_length(self):
        for x in self.__types:
            i=random.randint(1,100)
            gen = StringGenerator(i,x)
            genstring= gen.generate()
            self.assertEqual(i,len(genstring))
            print(x,end=' -> ')
            print(genstring)

    def test_for_string_type(self):
        for x in self.__types:
            i=random.randint(1,200)
            gen = StringGenerator(i,x)
            genstring= gen.generate()
            self.assertEqual(type(genstring),type('str'))

    

