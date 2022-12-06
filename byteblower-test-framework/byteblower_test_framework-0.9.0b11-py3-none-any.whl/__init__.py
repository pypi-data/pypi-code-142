"""Test Framework for the ByteBlower Traffic Generator."""
import logging

from ._version import version as __version__  # verion info
# `Flow` is not really needed, but it might be useful for type hinting:
from .flow import Flow
from .frame import Frame
from .frameblastingflow import FrameBlastingFlow
from .gamingflow import GamingFlow
from .httpflow import HTTPFlow
from .imix import Imix, ImixFrameConfig
from .ipv4 import IPv4Frame, IPv4Port
from .ipv4.nat import NattedPort
from .ipv6 import IPv6Frame, IPv6Port
from .port import Port
from .scenario import Scenario
from .server import Server
from .videoflow import VideoFlow
from .voiceflow import VoiceFlow


def configure_logging():
    """Configure logging for the used (low-level) frameworks."""
    for framework in ('scapy.runtime', ):
        framework_logger = logging.getLogger(framework)
        framework_logger.setLevel(logging.ERROR)
