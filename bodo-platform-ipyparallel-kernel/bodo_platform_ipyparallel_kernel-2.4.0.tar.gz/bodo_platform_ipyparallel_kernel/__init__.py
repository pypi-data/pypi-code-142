"""A simple IPyParallel based wrapper around IPython Kernel"""


from .kernel import IPyParallelKernel
from .launcher import BodoPlatformMPIEngineSetLauncher

from . import _version

__version__ = _version.get_versions()["version"]
