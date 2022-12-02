'''
ArrayGenerator generates array of types
'''

from dfac.generators.ClassicGenerator import ClassicGenerator
from dfac.utilities.Alphanumerics import Alphanumerics
from dfac.core.StringGenerator import StringGenerator
import random

class ArrayGenerator(ClassicGenerator):

    def __init__(self,length=10, type='Integer',low=0,high=9) -> None:
        __types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5, 'Integer':6,'Decimal':7, 'Symbolic':8}
        super().__init__(length,'String')
        self.__type=__types[type]
        self.low=low
        self.high=high
    
    def generateInteger(self):
        arr=[]
        for x in range(self.length):
            arr.append(random.randint(self.low,self.high))
        return arr

    def generateAlphaNumeric(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            gAN= StringGenerator(rint,'AlphaNumeric')
            l.append(gAN.generate())
        return l
        

    def generateAlphabet(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            gAN= StringGenerator(rint,'Alphabet')
            l.append(gAN.generate())
        return l

    def generateAlphabet_Upper(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            gAN= StringGenerator(rint,'Alphabet_Upper')
            l.append(gAN.generate())
        return l


    def generateAlphabet_Lower(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            gAN= StringGenerator(rint,'Alphabet_Lower')
            l.append(gAN.generate())
        return l

    def generateAlphaSymbolic(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            gAN= StringGenerator(rint,'AlphaSymbolic')
            l.append(gAN.generate())
        return l

    # def generateInteger(self):
    #     l=[]
    #     for i in range(self.length):
    #         rint=random.randint(self.low,self.high)
    #         gAN= StringGenerator(rint,'Integer')
    #         l.append(gAN.generate())
    #     return l

    def generateDecimal(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            num=round(random.random()*10,rint)
            l.append(num)
        return l

    def generateSymbolic(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            sym=random.choices(Alphanumerics().symbols(),k=rint)
            sym=''.join(sym)
            l.append(sym)
        return l


    def generate(self):
        if self.__type == 1:
            return self.generateAlphaNumeric()
        elif self.__type == 2:
            return self.generateAlphabet()
        elif self.__type == 3:
            return self.generateAlphabet_Upper()
        elif self.__type == 4:
            return self.generateAlphabet_Lower()
        elif self.__type == 5:
            return self.generateAlphaSymbolic()
        elif self.__type == 6:
            return self.generateInteger()
        elif self.__type == 7:
            return self.generateDecimal()
        elif self.__type == 8:
            return self.generateSymbolic()