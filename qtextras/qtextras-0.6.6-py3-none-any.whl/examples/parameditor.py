from functools import wraps

import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets

from qtextras import ParameterEditor, RunOptions, bindInteractorOptions as bind


class LAST_RESULT:
    """
    Just for testing purposes
    """

    value = None


def printResult(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        # False positive: nullptr / None is allowed
        # noinspection PyTypeChecker
        QtWidgets.QMessageBox.information(
            None,
            "Function Run!",
            f"Func result: {LAST_RESULT.value}",
        )

    return wrapper


@printResult
def funcOutsideClassUpdateOnBtn(a=5, b=6):
    """
    Function description. This will appear in the hover menu.
    """
    LAST_RESULT.value = a + b


class MyClass(ParameterEditor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registerFunction(
            funcOutsideClassUpdateOnBtn, runOptions=RunOptions.ON_BUTTON
        )

        self.registerFunction(self.updateOnChanging, runOptions=RunOptions.ON_CHANGING)
        self.registerFunction(self.updateOnChanged, runOptions=RunOptions.ON_CHANGED)
        self.registerFunction(
            self.updateOnBtnOrChanged,
            runOptions=[
                RunOptions.ON_BUTTON,
                RunOptions.ON_CHANGING,
                RunOptions.ON_CHANGED,
            ],
        )
        self.registerFunction(
            self.updateOnBtnOrShortcut,
            runActionTemplate={"shortcut": "Ctrl+C"},
            runOptions=RunOptions.ON_BUTTON,
        )

    @printResult
    @bind(a=dict(type="slider", limits=[0, 15], step=0.15))
    def updateOnChanging(self, a=5, b=6, c="string"):
        LAST_RESULT.value = f"a={a}, b={b}, c={c}"

    @printResult
    def updateOnBtnOrShortcut(self, boolOp=False):
        LAST_RESULT.value = str(boolOp)

    @printResult
    @bind(f=dict(limits=[0, 17], step=3), g=dict(type="text"))
    def updateOnChanged(self, f=5, g="six\nseven"):
        LAST_RESULT.value = f"f={f}, g={g}"

    @printResult
    @bind(lstOp=dict(type="list", limits=["five", "six", "seven"]))
    def updateOnBtnOrChanged(self, lstOp="five"):
        LAST_RESULT.value = lstOp

    @printResult
    @bind(fileOp=dict(type="file"))
    def updateOnApply(self, fileOp="./"):
        """
        Parameters
        ----------
        fileOp
            File picker can either select existing or non-existing files, folders,
            or multiple files depending on specified configurations.
        """
        LAST_RESULT.value = fileOp


def run():
    app = pg.mkQApp()

    editor = MyClass(directory="./")
    editor.show()
    app.exec_()


if __name__ == "__main__":
    run()
