# -*- coding: utf-8 -*-
from typing import Iterable

import numpy as np
from numpy import ndarray as Array
import awkward as ak

from polymesh.topo import TopologyArray

import axisvm
from .core.wrap import AxisVMModelItem, AxisVMModelItems
from .core.utils import RMatrix3x3toNumPy
from .attr import AxisVMAttributes
from .axline import get_line_attributes


class IAxisVMMember(AxisVMModelItem):
    """Wrapper for the `IAxisVMMember` COM interface."""

    @property
    def tr(self) -> Array:
        return self.transformation_matrix()

    @property
    def frame(self) -> Array:
        return self.transformation_matrix()
    
    @property
    def attributes(self):
        return self.parent.get_attributes(self.Index)

    @property
    def member_attributes(self):
        return self.parent.get_member_attributes(self.Index)

    def topology(self):
        lIDs = np.array(self.GetLines()[0]).flatten()
        lines = self.model.Lines.wrapped
        def foo(i): return [lines.Item[i].StartNode, lines.Item[i].EndNode]
        return np.squeeze(np.array(list(map(foo, lIDs)), dtype=int))

    def _get_attrs(self):
        """Return the representation methods (internal helper)."""
        attrs = []
        attrs.append(("Name", self.Name, "{}"))
        attrs.append(("Index", self.Index, "{}"))
        attrs.append(("UID", self._wrapped.UID, "{}"))
        attrs.append(("N Lines", len((self.GetLines()[0])), "{}"))
        attrs.append(("Length", self.Length, axisvm.FLOAT_FORMAT))
        attrs.append(("Volume", self.Volume, axisvm.FLOAT_FORMAT))
        attrs.append(("Weight", self.Weight, axisvm.FLOAT_FORMAT))
        return attrs

    def transformation_matrix(self):
        return RMatrix3x3toNumPy(self.GetTrMatrix()[0])
    
    def record(self):
        return self.parent.records(self.Index)


class IAxisVMMembers(AxisVMModelItems):
    """Wrapper for the `IAxisVMMembers` COM interface."""

    __itemcls__ = IAxisVMMember

    @property
    def tr(self) -> Array:
        return self.transformation_matrices()

    @property
    def frames(self) -> Array:
        return self.transformation_matrices()
    
    @property
    def attributes(self):
        return self.get_attributes()

    @property
    def member_attributes(self):
        return self.get_member_attributes()

    def topology(self, *args, i=None):
        axm = self.model.wrapped
        lines = axm.Lines
        members = self.wrapped
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            inds = [i]
        if isinstance(i, np.ndarray):
            inds = i
        else:
            if isinstance(i, Iterable):
                inds = np.array(i, dtype=int)
            else:
                inds = np.array(list(range(members.Count))) + 1

        def fnc(i): return list(members.Item[i].GetLines()[0])
        nodelist = list(map(fnc, inds))
        arr = TopologyArray(ak.Array(nodelist))
        lIDs = arr.flatten()
        def fnc(i): return [lines.Item[i].StartNode, lines.Item[i].EndNode]
        return TopologyArray(ak.Array(list(map(fnc, lIDs))))

    def transformation_matrices(self, *args, i=None) -> Array:
        m = self._wrapped
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            return RMatrix3x3toNumPy(self[i].GetTrMatrix()[0])
        if isinstance(i, np.ndarray):
            ids = i
        else:
            if isinstance(i, Iterable):
                ids = np.array(i, dtype=int)
            else:
                ids = np.array(list(range(m.Count))) + 1
        rec = list(map(lambda i: m.Item[i].GetTrMatrix()[0], ids))
        return np.array(list(map(RMatrix3x3toNumPy, rec)), dtype=float)

    def _get_attributes_raw(self, *args, i=None, **kwargs) -> Iterable:
        i = i if len(args) == 0 else args[0]
        if isinstance(i, int):
            ids = np.array([i])
        elif isinstance(i, np.ndarray):
            ids = i
        else:
            if isinstance(i, Iterable):
                ids = np.array(i, dtype=int)
            else:
                ids = np.array(list(range(self.Count))) + 1
        return self.BulkGetMembers(ids)
        
    def get_member_attributes(self, *args, **kwargs) -> AxisVMAttributes:
        return get_line_attributes(self, *args, **kwargs)

    def get_attributes(self, *args, **kwargs) -> AxisVMAttributes:
        return self.get_member_attributes(*args, **kwargs)
    
    def records(self, *args, **kwargs):
        return self.get_member_attributes(*args, raw=True, **kwargs)
