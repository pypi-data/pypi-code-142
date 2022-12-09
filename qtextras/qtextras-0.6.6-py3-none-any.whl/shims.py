import pyqtgraph as pg
from pkg_resources import parse_version
from pyqtgraph.parametertree import registerParameterType
from pyqtgraph.parametertree.parameterTypes import actiongroup as ag

parsed = parse_version(pg.__version__)

__all__ = ["ActionGroupParameter"]

if parsed < parse_version("0.13.1"):
    raise ImportError("pyqtgraph >= 0.13.1 is required")


if not hasattr(ag, "ActionGroupParameter"):
    # Make compatible with 0.13.2 definition
    class ActionGroupParameter(ag.ActionGroup):
        sigActivated = pg.QtCore.Signal(object)

        def activate(self):
            self.sigActivated.emit(self)
            self.emitStateChanged("activated", None)

    registerParameterType("_actiongroup", ActionGroupParameter, override=True)

else:
    ActionGroupParameter = ag.ActionGroupParameter
