""" Mixin to a dict interface to a dataclass """


class DictionaryMixin(dict):
    """Add to a Dataclass inheritance

    Attributes will be accessible like a dictionary.

    >>> from dataclasses import dataclass
    >>> @dataclass
    >>> class MyDataclass(DictionaryMixin):
    ...     attribute: str
    ...
    >>> instance = MyDataclass(attribute="attr")
    >>> _ = instance["attribute"]
    >>> _ = instance.attribute
    """

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as exc:
            raise AttributeError from exc

    def __delattr__(self, key):
        del self[key]
