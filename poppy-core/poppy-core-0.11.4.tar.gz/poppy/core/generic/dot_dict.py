#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import collections

__all__ = ["DotDict", "SimpleDotDict"]


class DotDict(collections.OrderedDict):
    """
    A class to have ordered dictionary and also be able to access parameters
    inside nested dictionary easily through a dot syntax for the key.
    """
    def __getitem__(self, key):
        """
        Override to access recursively the nested dictionary through the
        dot syntax.
        """
        # separator not present, returns the default value of dict
        if "." not in key:
            return super(DotDict, self).__getitem__(key)

        # the separator is present, split the key
        first, rest = key.split(".", 1)

        # get the value
        value = super(DotDict, self).__getitem__(first)

        # check it is an instance of the class
        if not isinstance(value, DotDict):
            raise KeyError("Cannot get {0} in {1}".format(rest, first))

        # now call the get
        return value.__getitem__(rest)

    def __setitem__(self, key, value):
        """
        Override to set recursively the nested dictionary through the dot
        syntax.
        """
        # the dot is present in the key, split
        if "." in key:
            first, rest = key.split(".", 1)

            # get the element of the first key
            element = self[first]

            # check that it is a DotDict
            if not isinstance(element, DotDict):
                raise KeyError("Cannot set {0} in {1}".format(rest, first))

            # set the value
            element[rest] = value
        else:
            if isinstance(value, dict) and not isinstance(value, DotDict):
                for k, v in value.items():
                    self[k] = v
            super(DotDict, self).__setitem__(key, value)


class SimpleDotDict(dict):
    """
    A class to have dictionary and also be able to access parameters inside
    nested dictionary easily through a dot syntax for the key.
    """
    def __getitem__(self, key):
        """
        Override to access recursively the nested dictionary through the
        dot syntax.
        """
        # separator not present, returns the default value of dict
        if "." not in key:
            return super(SimpleDotDict, self).__getitem__(key)

        # the separator is present, split the key
        first, rest = key.split(".", 1)

        # get the value
        value = super(SimpleDotDict, self).__getitem__(first)

        # check it is an instance of the class
        if not isinstance(value, SimpleDotDict):
            raise KeyError("Cannot get {0} in {1}".format(rest, first))

        # now call the get
        return value.__getitem__(rest)

    def __setitem__(self, key, value):
        """
        Override to set recursively the nested dictionary through the dot
        syntax.
        """
        # the dot is present in the key, split
        if "." in key:
            first, rest = key.split(".", 1)

            # get the element of the first key
            element = self[first]

            # check that it is a SimpleDotDict
            if not isinstance(element, SimpleDotDict):
                raise KeyError("Cannot set {0} in {1}".format(rest, first))

            # set the value
            element[rest] = value
        else:
            if isinstance(value, dict) and not isinstance(
                value,
                SimpleDotDict,
            ):
                for k, v in value.items():
                    self[k] = v
            super(SimpleDotDict, self).__setitem__(key, value)


# vim: set tw=79 :
