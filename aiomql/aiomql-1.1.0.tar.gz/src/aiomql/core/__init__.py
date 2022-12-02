from typing import Iterable, Mapping
from functools import cache

import MetaTrader5


class Base:
    """
    Sets all arguments as class properties

    Args:
        **kwargs: Object attributes and values as keyword arguments
    """
    def __init__(self, **kwargs):
        self.set_attributes(**kwargs)

    def __repr__(self):
        values = ', '.join(f"{name}={value!r}" for name, value in self.__dict__.items())
        return f"{self.__class__.__name__}({values})"

    def set_attributes(self, **kwargs):
        """
        Set keyword arguments as object attributes
        Args:
            **kwargs: Object attributes and values as keyword arguments
        Returns:

        Raises:
            AttributeError: When assigning an attribute that does not belong to the class or any parent class
        """
        for i, j in kwargs.items():
            try:
                setattr(self, i, self.annotations[i](j))
            except KeyError:
                raise AttributeError(f"Attribute {i} does not belong to class {self.__class__.__name__}")

    @property
    @cache
    def annotations(self) -> dict:
        init = {}
        for base in self.__class__.__mro__[-3::-1]:
            init |= getattr(base, '__annotations__', {})
        return init

    def get_dict(self, exclude: set = None, include: set = None) -> dict:
        """
        Returns class attributes as a dict
        Keyword Args:
            exclude: A set of attributes to be excluded
            include: Specific attributes to be returned

        Returns:
             dict: A dictionary of specified class attributes


        Notes:
            You can only set either of include or exclude.
            If you set both, the values of include will take precedence

        """
        exclude, include = exclude or set(), include or set()
        filter = include or set(self.dict.keys()).difference(exclude)
        return {key: value for key, value in self.dict.items() if key in filter}

    @property
    @cache
    def class_vars(self):
        return {key: value for key, value in self.__class__.__dict__.items() if key in self.__class__.__annotations__}

    @property
    def dict(self) -> dict:
        """
        All class attributes as a dictionary, except those in the "Config.except" set
        Returns:
            dict: A dictionary of class attributes

        """
        return {key: value for key, value in self.__dict__.items() | self.class_vars.items() if key not in self.Config.exclude}

    @dict.setter
    def dict(self, value: Mapping | Iterable[Iterable]):
        """
        Update the dict property
        Args:
            value (Mapping | Iterable[Iterable]): Value should be a mapping or iterable of key value pairs

        Returns:

        """
        self.dict.update(value)

    class Config:
        """
        Config Object of the class

        Attributes:
            exclude (set): A set of class attributes that will be excluded from the dict property
        """
        exclude = {'retcode', 'comment', 'request', 'mt5', 'retcode_external', "Config", "request_id"}


class BaseMeta(type):
    def __new__(mcs, cls_name, bases, cls_dict):
        platform = cls_dict.get('platform')
        defaults = {} if platform is None else platform.__dict__
        defaults = {f'_{key}': value for key, value in defaults.items() if not key.startswith('_')}
        cls_dict |= defaults
        return super().__new__(mcs, cls_name, bases, cls_dict)


class Platform(metaclass=BaseMeta):
    platform: MetaTrader5 = MetaTrader5
