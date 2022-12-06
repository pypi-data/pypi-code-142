#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from poppy.core.logger import logger
from poppy.core.target.base_target import BaseTarget

__all__ = ['PyObjectTarget']

NoDefault = type(
    'NoDefault',
    (object,),
    {
        '__str__': lambda s: 'NoDefault',
        '__repr__': lambda s: 'NoDefault'
    }
)()


class PyObjectTargetException(Exception):
    pass

class EmptyPyObjectTarget(Exception):
    pass


class PyObjectTarget(BaseTarget):
    """
    PyObjectTarget is target class used to pass and track python object through the pipeline
    """

    def __init__(self, *args, value=NoDefault, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = value

    def update(self, *args, value=NoDefault, **kwargs):
        """
        Update the python object target instance with the given args/kwargs

        Updated attributes:
          - value

        :return:
        """

        super().update(*args, **kwargs)

        # update the value only if a value is given
        if value is not NoDefault:
            try:
                if self.value != value:
                    logger.warning(f"Content of PyObjectTarget '{self.id}' was defined multiple times")
            except EmptyPyObjectTarget:
                pass
            finally:
                self.value = value

    @property
    def value(self):
        if self._value is NoDefault:
            raise EmptyPyObjectTarget(f"Content of PyObjectTarget '{self.id}' is not defined")
        else:
            return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __iter__(self):
        if not self._is_multi_target:
            raise PyObjectTargetException("Simple targets are not iterable, use the 'many=True' flag to generate "
                                          "multi-target objects")

        for idx, value in enumerate(self.value):
            # TODO: add parametrization of the target id
            yield PyObjectTarget(f"__{self.id}__{idx}__", self._pipeline, value=value)
