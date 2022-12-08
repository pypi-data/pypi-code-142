__title__ = 'discordsimplimised'
__author__ = 'Sheep26'
__license__ = 'MIT'
__copyright__ = 'Copyright 2022-present Sheep26'
__version__ = '1.3'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from discordsimplimised import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=2, minor=1, micro=0, releaselevel='final', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, NamedTuple, Literal, VersionInfo
