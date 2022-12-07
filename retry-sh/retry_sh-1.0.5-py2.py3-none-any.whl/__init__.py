__all__ = ['retry', 'retry_call']
__version__ = "1.0.5"

import logging

from .api import retry, retry_call


# Set default logging handler to avoid "No handler found" warnings.
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())
