#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ["CachedProperty"]


class CachedProperty(object):
    """
    A descriptor to cache the execution of a property, and sending the computed
    value again and again.
    """

    def __init__(self, method):
        """
        Store the wrapped method, and its name.
        """
        self.name = method.__name__
        self.func = method

    def __get__(self, instance, owner):
        """
        When getting the attribute the first time, the descriptor is called and
        then compute the method (no arguments) as usual. Then the method in
        the instance is replaced by an attribute containing the cached value.
        """
        # compute the method as usual
        result = self.func(instance)

        # replace the method by the attribute, avoiding to call the descriptor
        # again !
        setattr(instance, self.name, result)

        # return the result
        return result
