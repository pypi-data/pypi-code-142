"""Enable function chaining for any object"""
import builtins
import operator


class Contained:

    def __init__(self, contain):
        self.__contain = contain

    def __call__(self):
        return self.__contain

    def __getattr__(self, fn):
        if (chain_method := getattr(self.__contain, fn, None)) is not None:
            def __chained_method(*args, **kwargs):
                if (result := chain_method(*args, **kwargs)) is not None:
                    self.__contain = result
                # else assume this was an in-place mutation
                return result
            return __chained_method
        if (chain_method := getattr(builtins, fn, getattr(operator, fn, None))) is not None:
            def __chained_method(*args, **kwargs):
                if (result := chain_method(self.__contain, *args, **kwargs)) is not None:
                    self.__contain = result
                # else assume this was an in-place mutation
                return result
            return __chained_method
        raise AttributeError(f"'{fn}' is not an attribute of type object {type(self.__contain)} or a builtin or an operator")
