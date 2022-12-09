import pyqtgraph as pg
from pyqtgraph.Qt import QtWidgets

import qtextras.widgets.easywidget
from qtextras import ParameterEditor


def dockgrouping(directory):
    pes = [ParameterEditor(name=str(ii)) for ii in range(3)]
    # grp = ParameterEditorDockGroup(pes, "Test Group")
    window = qtextras.widgets.easywidget.EasyWidget.buildMainWindow(
        [QtWidgets.QTextEdit(), QtWidgets.QPushButton("Test")]
    )
    # window.addDockWidget(QtCore.Qt.DockWidgetArea.RightDockWidgetArea, grp)
    pe = ParameterEditor(name="test", directory=directory)

    def myfunc(a=1):
        print("Test", a)
        return a

    pe.registerFunction(
        myfunc, runOptions="action", runActionTemplate=dict(shortcut="Ctrl+C")
    )
    pes.append(pe)
    for pe in pes:
        pe.createWindowDock(window)

    return window


def test_dockgrouping(tmp_path):
    assert dockgrouping(tmp_path)


if __name__ == "__main__":
    pg.mkQApp()
    win = dockgrouping(".")
    win.raise_()
    win.show()
    pg.exec()
