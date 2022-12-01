#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring

import importlib_metadata

from .glitch import INJECTION_POINTS

from .glitch import Glitch
from .glitch import StepGlitch
from .glitch import RectangleGlitch
from .glitch import OneSidedDoubleExpGlitch
from .glitch import IntegratedOneSidedDoubleExpGlitch
from .glitch import TwoSidedDoubleExpGlitch
from .glitch import IntegratedTwoSidedDoubleExpGlitch
from .glitch import ShapeletGlitch
from .glitch import IntegratedShapeletGlitch
from .glitch import TimeSeriesGlitch
from .glitch import HDF5Glitch
from .glitch import LPFLibraryGlitch
from .glitch import LPFLibraryModelGlitch

try:
    metadata = importlib_metadata.metadata('lisaglitch').json
    __version__ = importlib_metadata.version('lisaglitch')
    __author__ = metadata['author']
    __email__ = metadata['author_email']
except importlib_metadata.PackageNotFoundError:
    pass
