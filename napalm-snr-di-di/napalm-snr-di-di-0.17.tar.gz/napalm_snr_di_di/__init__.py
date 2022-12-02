"""napalm_ros package."""

# Import stdlib
import pkg_resources

# Import local modules
from napalm_snr_di_di.snr import NapalmSnrDriver

try:
    __version__ = pkg_resources.get_distribution('napalm-snr-di-di').version
except pkg_resources.DistributionNotFound:
    __version__ = "Not installed"

__all__ = ('NapalmSnrDriver', )
