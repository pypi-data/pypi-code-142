#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from poppy.core.logger import logger

from poppy.core.generic.dot_dict import SimpleDotDict

__all__ = ["Properties"]




class Properties(SimpleDotDict):
    """
    Class for storing parameters used in the pipeline. Tasks in the pipeline
    should share parameters and targets through this dictionary like.
    """
    def __init__(self, *args, **kwargs):
        # init as usual
        super(Properties, self).__init__(*args, **kwargs)

    def __getattr__(self, item):
        return self.__getitem__(item)

    def __setattr__(self, item, value):
        return self.__setitem__(item, value)

    def __add__(self, other):
        """
        To be able to merge two properties by adding them to each other.
        """
        self.update(other)
        return self

    def __radd__(self, other):
        """
        Same as __add__ but in the other order. The properties at most right in
        the merging is preponderant.
        """
        other.update(self)
        return other

    def __iadd__(self, other):
        """
        Incrementation.
        """
        self.update(other)
        return self

    def to_bag(self):
        """
        Transform the data inside the properties into a bag instance containing
        the top level properties.
        """
        class Bag:
            pass

        bag = Bag()

        for key, value in self.items():
            setattr(bag, key, value)

        return bag
