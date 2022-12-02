import _sepl_light_lib

from .pkginfo import __author__, __version__

assert _sepl_light_lib.__version__ == __version__, \
    ImportError(f"sepl_light_lib {__version__} and _sepl_light_lib {_sepl_light_lib.__version__} version mismatch!")

import sepl_light_lib.color as color
import sepl_light_lib.wave as wave

from sepl_light_lib.const import *
