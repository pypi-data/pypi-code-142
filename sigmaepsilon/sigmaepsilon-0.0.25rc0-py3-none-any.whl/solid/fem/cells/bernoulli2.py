# -*- coding: utf-8 -*-
from neumann.numint import GaussPoints as Gauss
from polymesh.cells import L2 as Line

from .bernoulli import BernoulliBase as Bernoulli
from .gen.b2 import (shape_function_values_bulk, 
                     shape_function_derivatives_bulk)
from .elem import FiniteElement
from .metaelem import ABCFiniteElement as ABC

__all__ = ['Bernoulli2']


class Bernoulli2(ABC, Bernoulli, Line, FiniteElement):
    """
    Finite element class to handle 2-noded Bernoulli beams.
    """

    qrule = 'full'
    quadrature = {
        'full': Gauss(2),
        'selective': {
            (0, 1): 'full',
            (2): 'reduced'
        },
        'reduced': Gauss(1),
        'mass' : Gauss(4)
    }
    shpfnc = shape_function_values_bulk
    dshpfnc = shape_function_derivatives_bulk