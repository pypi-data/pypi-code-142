from collections import OrderedDict


class Strictly:
    def __init__(
            self,
            *predicates,
            raise_message = f"Value doesn't match any of the predicates",
            default = None,
    ):
        self.predicates = predicates
        self.predicate_cache = OrderedDict()
        self.msg = raise_message
        if default is not None and not self.map(default):
            raise ValueError(raise_message)

    def __set_name__(self, owner, name):
        self.__name__ = name

    def cached_predicate_check(self, value):
        hashed = hash(value)
        if hashed not in self.predicate_cache:
            return self.predicate_cache.setdefault(hashed, self.map(value))
        self.predicate_cache.move_to_end(hashed)
        while len(self.predicate_cache) > 1000:
            self.predicate_cache.popitem(last = False)
        return self.predicate_cache[hashed]

    def __set__(self, instance, value):
        try:
            predicate_check = self.cached_predicate_check(value)
        except TypeError:
            predicate_check = self.map(value)
        if not predicate_check:
            raise ValueError(self.msg)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

    def bind(self, *funcs):
        self.predicates += funcs
        return self

    def map(self, value):
        return all(p(value) for p in self.predicates)

    def message(self, msg):
        self.msg = msg
        return self

    def __or__(self, other):
        if isinstance(other, Strictly):
            return Strictly(*(self.predicates + other.predicates))
        if isinstance(other, str):
            return self.message(other)
        return self.bind(other)

    def __ror__(self, other):
        return self.__or__(other)


def strict_annotations(cls):
    for name, val in (item for item in cls.__annotations__.items() if not hasattr(cls, item[0])):
        setattr(
                cls,
                name,
                Strictly(
                        lambda x: isinstance(x, val),
                        raise_message = f"{name} must be of type {val}",
                )
        )
        getattr(cls, name).__set_name__(cls, name)
    return cls


def strict_dataclass(cls = None, /, **kwargs):
    """
    A decorator that makes a dataclass with strict annotations.
    Parameters
    ----------
    cls : any class you want to make a dataclass
    kwargs :
    Any keyword arguments you would normally pass to dataclass

    Returns a dataclass with strict annotations
    -------
    """

    if "dataclass" not in globals():
        from dataclasses import dataclass

    def wrap(_cls):
        return strict_annotations(dataclass(**kwargs)(_cls))

    if cls is None:
        return wrap
    return wrap(cls)
