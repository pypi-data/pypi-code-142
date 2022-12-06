from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from .utils import set_default_palette

set_default_palette()

from .paramscan import ParamscanTearsheet  # noqa: F401
from .perf import AggregateDailyPerformance, DailyPerformance  # noqa: F401
from .shortfall import ShortfallTearsheet  # noqa: F401
from .tearsheet import Tearsheet  # noqa: F401
