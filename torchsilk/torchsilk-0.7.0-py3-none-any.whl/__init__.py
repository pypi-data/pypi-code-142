__version__ = "0.7.0"

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.expanduser().resolve()

from torchsilk import distributions as distributions  # noqa: E402
from torchsilk.modules import FunctionalModule as FunctionalModule  # noqa: E402
from torchsilk.modules import (  # noqa: E402
    FunctionalModuleWithBuffers as FunctionalModuleWithBuffers,
)
from torchsilk.modules import LossFunction as LossFunction  # noqa: E402
from torchsilk.modules import Module as Module  # noqa: E402
from torchsilk.modules import TrainState as TrainState  # noqa: E402
from torchsilk.modules import make_functional as make_functional  # noqa: E402
from torchsilk.modules import (  # noqa: E402
    make_functional_with_buffers as make_functional_with_buffers,
)
from torchsilk.type_defs import BaseConfig as BaseConfig  # noqa: E402
from torchsilk.type_defs import EmptyModel as EmptyModel  # noqa: E402
