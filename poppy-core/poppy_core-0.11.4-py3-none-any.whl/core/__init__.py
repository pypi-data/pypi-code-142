#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pkg_resources

# interrogate version string of already-installed distribution
__version__ = pkg_resources.require('poppy-core')[0].version

from poppy.core.tools.exceptions import MissingArgument, \
    MissingProperty, TargetFileNotSaved, MissingInput
