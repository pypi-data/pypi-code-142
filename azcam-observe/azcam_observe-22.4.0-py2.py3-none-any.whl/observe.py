"""
Contains the Observe class for Qt usage.
"""

import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication

import azcam
from azcam_observe.observe_qt.observe_qt import ObserveQt


def start():
    """
    Start observe for installed command "observe".
    """

    if azcam.db.get("qtapp") is None:
        app = QCoreApplication.instance()
        print(app)
        if app is None:
            app = QApplication(sys.argv)
        azcam.db.qtapp = app

    observe=ObserveQt()
    observe.start()
    sys.exit(azcam.db.qtapp.exec())

if __name__ == "__main__":
    start()