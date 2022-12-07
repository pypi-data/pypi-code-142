'''
First Parent generator class for all basic generator sub types to derive from.

Members:
1. __types [dict]: Type of data you need to generate
2. __type  [int]: an integer represening the above
    2.a Types available are: Interger, String, Decimal
Methods:
1. getLength(None) [return int]
2. getType(None) [return int]

'''

class ClassicGenerator:

    def __init__(self, length=10, type='Integer') -> None:
        __types={'Integer':1,'String':2,'Decimal':3}
        self.__type=__types[type]
        self.length=length

    def getLength(self):
        return self.length
    
    def getType(self):
        return self.__type

    def generate(self):
        pass

        