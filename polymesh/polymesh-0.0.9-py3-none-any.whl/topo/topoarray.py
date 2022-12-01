# -*- coding: utf-8 -*-
from typing import Union

import numpy as np
from numpy import concatenate as join, ndarray
from numpy.lib.mixins import NDArrayOperatorsMixin

import awkward as ak
from awkward import unflatten as build, Array as akarray

from dewloosh.core import Wrapper
from neumann.linalg.sparse.jaggedarray import JaggedArray
from neumann.arraysetops import unique2d
from neumann.linalg.sparse.utils import count_cols


__all__ = ['TopologyArray']


HANDLED_FUNCTIONS = {}


class TopologyArrayBase(JaggedArray):

    def __init__(self, *topo, cuts=None, **kwargs):
        if cuts is None and len(topo) > 0:
            widths = list(map(lambda topo: topo.shape[1], topo))
            widths = np.array(widths, dtype=int)
            cN, cE = 0, 0
            for i in range(len(topo)):
                dE = topo[i].shape[0]
                cE += dE
                cN += dE * topo[i].shape[1]
            topo1d = np.zeros(cN, dtype=int)
            cuts = np.zeros(cE, dtype=int)
            cN, cE = 0, 0
            for i in range(len(topo)):
                dE = topo[i].shape[0]
                dN = dE * topo[i].shape[1]
                topo1d[cN:cN+dN] = topo[i].flatten()
                cN += dN
                cuts[cE:cE+dE] = np.full(dE, widths[i])
                cE += dE
            data = get_data(topo1d, cuts=cuts)
            super().__init__(data, **kwargs)
        else:
            super().__init__(*topo, cuts=cuts, **kwargs)


def shape(arr): return arr.shape[:2]
def cut(shp): return np.full(shp[0], shp[1], dtype=np.int64)
def flatten(arr): return arr.flatten()


def get_data(data, cuts=None):
    if isinstance(data, np.ndarray):
        nD = len(data.shape)
        assert nD <= 2, "Only 2 dimensional arrays are supported!"
        if nD == 1:
            assert isinstance(cuts, np.ndarray)
            data = build(data, cuts)
    elif isinstance(data, list):
        assert all(map(lambda arr: len(arr.shape) == 2, data)), \
            "Only 2 dimensional arrays are supported!"
        # NOTE - implementaion 1
        # > Through the back door, but this is probably the cleanest solution of all.
        # > It only requires to create one python list, without further operations on it.
        # NOTE This line is one of the most unreadable things I've ever done.
        data = build(join(list(map(flatten, data))),
                     join(list(map(cut, map(shape, data)))))
        # NOTE - implementaion 2
        #from operator import add
        #from functools import reduce
        # > This also works, but requires data to jump back and forth just to
        # > have a merged list of lists. It also requires to add nested python lists,
        # > which is probably not the quickest operation in the computational world.
        #data = ak.from_iter(reduce(add, map(lambda arr : ak.Array(arr).to_list(), data)))
        # NOTE - implementaion 3
        # > This also works at creation, but fails later at some operation due to
        # > the specific layout generated by ak.concatenate
        #data = ak.concatenate(list(map(lambda arr : ak.Array(arr), data)))
    return data


HANDLED_FUNCTIONS = {}


class TopologyArray(NDArrayOperatorsMixin, Wrapper):

    __array_base__ = TopologyArrayBase

    def __init__(self, *args, to_numpy=True, wrap=None, **kwargs):
        if wrap is None:
            if len(args) == 1:
                if isinstance(args[0], ndarray):
                    wrap = args[0]
                elif isinstance(args[0], akarray):
                    if to_numpy:
                        try:
                            wrap = args[0].to_numpy()
                        except Exception:
                            wrap = args[0]
                    else:
                        wrap = self.__class__.__array_base__(*args, **kwargs)
            else:
                wrap = self.__class__.__array_base__(*args, **kwargs)
        assert wrap is not None, "Invalid input, the constrtuctor must be fed properly!"
        self._array = wrap
        super(TopologyArray, self).__init__(wrap=wrap)

    def __repr__(self):
        return f"{self.__class__.__name__}\n({self._array})"

    def __array__(self):
        return self._array
            
    def __getitem__(self, key):
        return self._array.__getitem__(key)

    def __setitem__(self, key):
        return self._array.__setitem__(key)

    def __len__(self):
        return len(self._array)

    def to_ak(self) -> akarray:
        if isinstance(self._array, akarray):
            return self.__array__()
        else:
            return self.__class__.__array_base__(self.__array__())

    def to_numpy(self) -> ndarray:
        if isinstance(self._array, ndarray):
            return self.__array__()
        else:
            return TypeError("Background object cannot be converted to a `numpy` array.")

    def to_array(self) -> Union[akarray, ndarray]:
        return self.__array__()
    
    def to_list(self):
        if isinstance(self._array, ndarray):
            return self.__array__().tolist()
        else:
            return self.__array__().to_list()

    def unique(self, *args, **kwargs):
        return np.unique(self, *args, **kwargs)

    def is_jagged(self):
        widths = self.widths()
        return not np.all(widths == widths[0])

    def widths(self):
        return count_cols(self._array)

    def flatten(self, return_cuts=False):
        """
        Returns the flattened equivalent of the array.
        """
        if isinstance(self._array, akarray):
            if return_cuts:
                topo = ak.flatten(self._array).to_numpy()
                return self.widths(), topo
            else:
                topo = ak.flatten(self._array).to_numpy()
                return topo
        else:
            if return_cuts:
                return self.widths(), self.to_numpy().flatten()
            else:
                return self.to_numpy().flatten()

    @property
    def shape(self):
        if isinstance(self._array, ndarray):
            return self._array.shape
        else:
            return len(self), self.widths()
        
    def __array_function__(self, func, types, args, kwargs):
        if func not in HANDLED_FUNCTIONS:
            return func(*args[0], **kwargs)  # vstakc works well with this
        # Note: this allows subclasses that don't override
        # __array_function__ to handle DiagonalArray objects.
        if not all(issubclass(t, self.__class__) for t in types):
            return NotImplemented
        return HANDLED_FUNCTIONS[func](*args, **kwargs)


def implements(numpy_function):
    """Register an __array_function__ implementation for TopologyArray objects."""
    def decorator(func):
        HANDLED_FUNCTIONS[numpy_function] = func
        return func
    return decorator


@implements(np.unique)
def unique(*args, **kwargs):
    return unique2d(args[0]._array, **kwargs)


"""@implements(np.hstack)
def hstack(*args, **kwargs):
    return hstack2d(*args)"""


@implements(np.vstack)
def vstack(*args, **kwargs):
    data = np.concatenate(list(t.flatten() for t in args[0]))
    cuts = np.concatenate(list(t.widths() for t in args[0]))
    return TopologyArray(JaggedArray(data, cuts=cuts))
