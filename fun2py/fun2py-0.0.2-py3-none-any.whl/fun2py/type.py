from typing import Union, Iterable
from .interface import *





class String(str):
    def __init__(self, text: str) -> None:
        super().__init__()

    def __value__(self):
        return self


class Numeral(Immutable,Valuable):
    def __init__(self, num: Union[int, float]):
        super().__init__()
        self.__data__ = dict(num=num)

    def __value__(self):
        return self.num

    def __str__(self):
        return str(self.__data__['num'])

    def __repr__(self):
        return str(self.__data__['num'])

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Numeral) and val(self) == val(o):
            return True
        return False

    def __ne__(self, o):
        if isinstance(o, Numeral) and val(self) != val(o):
            return True
        return False

    def __le__(self, o):
        if isinstance(o, Numeral) and val(self) <= val(o):
            return True
        return False

    def __ge__(self, o):
        if isinstance(o, Numeral) and val(self) >= val(o):
            return True
        return False

    def __lt__(self, o):
        if isinstance(o, Numeral) and val(self) < val(o):
            return True
        return False

    def __gt__(self, o):
        if isinstance(o, Numeral) and val(self) >= val(o):
            return True
        return False

    def __add__(self, o):
        if isinstance(o, Numeral):
            return self.__class__(val(self) + val(o))
        else:
            raise TypeError('The object must be a Numeral.')

    def __sub__(self, o):
        if isinstance(o, Numeral):
            return self.__class__(val(self) - val(o))
        else:
            raise TypeError('The object must be a Numeral.')

    def __mul__(self, o):
        if isinstance(o, Numeral):
            return self.__class__(val(self) * val(o))
        else:
            raise TypeError('The object must be a Numeral.')

    def __truediv__(self, o):
        if isinstance(o, Numeral):
            return self.__class__(val(self) / val(o))
        else:
            raise TypeError('The object must be a Numeral.')

    def __floordiv__(self, o):
        if isinstance(o, Numeral):
            return self.__class__(val(self) // val(o))
        else:
            raise TypeError('The object must be a Numeral.')

    def __pow__(self, o, modulo=None):
        if isinstance(o, Numeral):
            return self.__class__(val(self) ** val(o))
        else:
            raise TypeError('The object must be a Numeral.')


class List(Immutable):
    def __init__(self, elements: Iterable):

        tmp = []
        for i in elements:
            if isinstance(i, int) or isinstance(i,float):
                tmp.append(Numeral(i))
            elif isinstance(i, Numeral):
                tmp.append(i)
            else:
                tmp.append(String(str(i)))
        self.__data__ = tmp

    def __getitem__(self, item):
        return self.__data__[item]

    def __setitem__(self, key, value):
        raise NotImplementedError('Cannot assign values to list')

    def __iter__(self):
      return self.__data__.__iter__()

    def __len__(self):
        return self.__data__.__len__()

    def __str__(self):return self.__data__.__str__()
    def __repr__(self):return self.__data__.__repr__()




