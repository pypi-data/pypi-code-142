__version__ = "0.5.0"

from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.expanduser().resolve()

from torchsilk import distributions as distributions  # noqa: E402
from torchsilk.modules import FunctionalModule as FunctionalModule  # noqa: E402
from torchsilk.modules import (  # noqa: E402
    FunctionalModuleWithoutBuffers as FunctionalModuleWithoutBuffers,
)
from torchsilk.modules import Module as Module  # noqa: E402
from torchsilk.modules import TrainState as TrainState  # noqa: E402
from torchsilk.type_defs import BaseConfig as BaseConfig  # noqa: E402
from torchsilk.type_defs import EmptyModel as EmptyModel  # noqa: E402
