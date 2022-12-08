from .para import *
from .tensor_scaling import rescale_lambda_centerized_workhorse
from .tensor_scaling import rescale_lambda_centerized

from .models import *
from .hdf5_io import *
from .coil import *
from .expio import *
from .util import *
from .freesurfer import *
from .roi import *
from .subject import *
from .opt import *
from .neuron import *
from .mesh import *
from .regression import *
from .util.plot import *
from .tms_pulse import *

try:
    from .pckg import libeep
except (ImportError, SyntaxError):
    pass
try:
    from paraview.simple import *
except ImportError:
    pass

__version__ = "0.2022.12"

# when pipped, datadir is under pynibs
__testdatadir__ = os.path.join(os.path.dirname(__file__), '..', 'tests', 'data')
__datadir__ = os.path.join(os.path.dirname(__file__), '..', 'data')
if not os.path.exists(__testdatadir__):
    __testdatadir__ = os.path.join(os.path.dirname(__file__), 'tests', 'data')
    __datadir__ = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(__testdatadir__):
    warnings.warn(f"Cannot find pynibs.__testdatadir__='{__testdatadir__}'")
