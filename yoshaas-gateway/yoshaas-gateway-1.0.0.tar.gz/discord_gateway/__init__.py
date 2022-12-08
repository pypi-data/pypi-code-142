"""
Gateway __init__
"""

__title__ = 'DiscordGateway'
__author__ = 'zYoshaa'
__version__ = '1.0.1'

import logging as log
from typing import NamedTuple, Literal

from .api import *
from .constants import *
from .discord_objects import *
from .discord_user import *
from .gatewaybot import *
from .gateway_handler import *
from .gateway import *


log.basicConfig(encoding='utf-8', level=log.ERROR)
