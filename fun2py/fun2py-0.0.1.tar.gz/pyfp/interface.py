def val(obj):
    return obj.__value__()

class Valuable:
    def __value__(self):
        raise NotImplementedError


class Immutable:
    def __getattr__(self, item):
        return self.__data__[item]

    def __setattr__(self, key, value):
        if key != '__data__':
            raise TypeError(f'{self.__class__} has no attribute {key}.')
        try:
            self.__data__
        except:
            super(Immutable, self).__setattr__(key, value)
            return
        raise TypeError('Cannot reassign.')