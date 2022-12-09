from __future__ import annotations

import builtins
from typing import Optional, Sequence

import numpy as np
import pandas as pd


def _rescale(data, min_, max_):
    # Handle nan values
    rng = max_ - min_
    if rng == 0:
        return np.ones_like(data)
    return (data.astype(float) - min_) / rng


class _UNSPECIFIED_DEFAULT:
    pass


class OptionsDict:
    comparator = str
    """
    Function for determining equality when comparing to another object
    """

    def __init__(
        self, name: str, value=None, type: Optional[str] = None, tip="", **opts
    ):
        """
        Encapsulates parameter information use within the main application

        Parameters
        ----------
        name
            Display name of the parameter
        value
            Initial value of the parameter. This is used within the program to infer
            parameter type, shape, comparison methods, etc.
        type
            Type of the variable if not easily inferrable from the value itself. For
            instance, class:`ShortcutParameter<shortcuts.ShortcutParameter>` is
            indicated with string values (e.g. 'Ctrl+D'), so the user must explicitly
            specify that such an :class:`OptionsDict` is of type 'shortcut' (as defined
            in :class:`ShortcutParameter<pgregistered.shortcut.ShortcutParameter>`) If
            the type *is* easily inferrable, this may be left blank.
        tip
            Additional documentation for this parameter.
        **opts
            Additional options associated with this parameter
        """
        if opts is None:
            opts = {}
        if type is None:
            # Infer from value
            type = builtins.type(value).__name__.lower()
        self.name = name
        self.value = value
        self.type = type
        self.tip = tip or opts.get("tip", "")

        self.opts = opts

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}: <{self.type}>"

    def __lt__(self, other):
        """
        Required for sorting by value in component table. Defer to alphabetic
        sorting

        Parameters
        ----------
        other
            Other :class:`OptionsDict` member for comparison
        """
        return self.comparator(self) < self.comparator(other)

    def __eq__(self, other):
        # TODO: Highly naive implementation. Be sure to make this more robust if
        #  it needs to be for now assume only other prjparamss will be passed in
        return self.comparator(self) == self.comparator(other)

    def __hash__(self):
        # Since every parameter within a group will have a unique name, just the name is
        # sufficient to form a proper hash
        return hash(
            self.comparator(self),
        )

    def toNumeric(self, data: Sequence, rescale=False, returnMapping=False):
        """
        Useful for converting string-like or list-like parameters to integer
        representations.

        If self's `value` is non-numeric data (e.g. strings):
           - First, the parameter is searched for a 'limits' property. This will
             contain all possible values this field could be.
           - If no limits exist, unique values in the input data will be considered
             the limits

        Parameters
        ----------
        data
            Array-like data to be turned into numeric values according to the parameter
            type
        rescale
            If *True*, values will be rescaled to the range 0-1
        returnMapping
            Whether to also return a series of the unique values within ``data``
            in the form {numericVal: label}.
        """
        numericVals = np.asarray(data).copy()
        if len(data) == 0:
            mapping = pd.Series(name=self, dtype=object)
            if returnMapping:
                return numericVals, mapping
            return numericVals
        if not np.issubdtype(type(self.value), np.number):
            # Check for limits that indicate the exhaustive list of possible values.
            # Otherwise, just use the unique values of this set as the limits
            if "limits" in self.opts:
                listLims = list(self.opts["limits"])
                numericVals = np.array([listLims.index(v) for v in numericVals])
                mapping = pd.Series(listLims, np.arange(len(listLims), dtype=int))
            else:
                listLims, numericIdxs, numericVals = np.unique(
                    numericVals, return_index=True, return_inverse=True
                )
                mapping = pd.Series(listLims, numericVals[numericIdxs], name=self)
        elif returnMapping:
            # Potentially expensive, only compute if requested
            uniques = np.unique(numericVals)
            mapping = pd.Series(uniques, uniques, name=self)
        else:
            # Dummy mapping to allow ops
            class mapping:
                index = np.array([numericVals.max(), numericVals.min()])

        if rescale:
            min_, max_ = mapping.index.min(), mapping.index.max()
            # Make sure to reduce min to account for offset in reverse direction
            numericVals = _rescale(numericVals, min_, max_)
            mapping.index = _rescale(mapping.index, min_, max_)
        if returnMapping:
            return numericVals, mapping
        return numericVals

    def __getitem__(self, item):
        if item in self._fields:
            return getattr(self, item)
        return self.opts[item]

    def __setitem__(self, key, value):
        if key in self._fields:
            setattr(self, key, value)
        else:
            self.opts[key] = value

    def __contains__(self, item):
        return item in [*self._fields, *self.opts.keys()]

    def __delitem__(self, key):
        del self.opts[key]

    def get(self, item, default=None):
        try:
            return self[item]
        except KeyError:
            if default is _UNSPECIFIED_DEFAULT:
                raise
            return default

    @property
    def _fields(self):
        excludeFields = {"opts"}
        return [field for field in self.__dict__ if field not in excludeFields]

    def keys(self):
        return self._fields + list(self.opts.keys())

    def __contains__(self, item):
        return item in self._fields or item in self.opts

    def addHelpText(self, prependText="", postfixText="", replace=True, newline="<br>"):
        helpText = self.tip
        if len(prependText) > 0 and len(helpText) > 0 or len(postfixText) > 0:
            prependText += newline
        curText = prependText + self.tip
        if len(postfixText) > 0:
            curText += newline + postfixText
        if replace:
            self.tip = curText
        return curText
