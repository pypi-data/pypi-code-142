from collections import OrderedDict


class _StrictlyMeta(type):
    def __or__(cls, other):
        return cls(other)

    def __ror__(cls, other):
        return cls(other)


class StrictlyDescriptor(metaclass=_StrictlyMeta):
    predicate_cache = OrderedDict()

    def __init__(
        self,
        *predicates,
        msg="Value does not match any of the predicates",
    ):
        self.predicates = predicates
        self.msg = msg

    def __set_name__(self, owner, name):
        self.__name__ = name

    def __set__(self, instance, value):
        if not self.map(value):
            msg = f"attempted to set {self.__name__!r} to {value!r} but {self.msg}"
            raise ValueError(msg)

    def bind(self, *funcs):
        self.predicates += funcs
        return self

    def map(self, value):
        try:
            key = hash(value)
        except TypeError:
            """If the value is unhashable, we can't cache it"""
        else:
            if key in self.predicate_cache:
                self.predicate_cache.move_to_end(key)
                return self.predicate_cache[key]
        result = True
        for predicate in self.predicates:
            if not predicate(value):
                result = False
                break
        try:
            return self.predicate_cache.setdefault(key, result)  # NOQA
        except NameError:
            return result

    def message(self, msg):
        self.msg = msg
        return self

    def __call__(self, *args):
        self.bind(*args)
        return self

    def __or__(self, other):
        if isinstance(other, str):
            return self.message(other)
        elif isinstance(other, StrictPredicate):
            return self.bind(other)
        return self.bind(other)

    def __ror__(self, other):
        return self.__or__(other)


class StrictPredicate(metaclass=_StrictlyMeta):
    def __init__(self, func):
        self.func = func

    def __call__(self, value):
        return self.func(value)

    def __or__(self, other):
        if callable(other):
            return StrictPredicate(lambda x: self(x) and other(x))
        raise TypeError(f"Cannot combine {self} with {other}")


__all__ = ["StrictlyDescriptor", "StrictPredicate"]
