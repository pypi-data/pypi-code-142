from __future__ import annotations

import logging
import signal
import sys
import typing as t
import warnings

from pyqtgraph import QtCore, QtWidgets

from qtextras.constants import PrjEnums
from qtextras.widgets.loghandlers import DialogHandler


class AppLogger(logging.Logger):
    nonCriticalErrors = ()

    old_showwarning = None
    old_sys_excepthook = None

    def logLater(self, msg, *args, **kwargs):
        # Define local function to avoid uncollected garbage on pyside2
        def doLog():
            self.log(msg, *args, **kwargs)

        QtCore.QTimer.singleShot(0, doLog)

    def attention(self, msg, *args, **kwargs):
        return self.log(PrjEnums.LOG_LVL_ATTN, msg, *args, **kwargs)

    def registerExceptions(
        self,
        win: QtWidgets.QMainWindow = None,
        nonCriticalErrors: t.Sequence[t.Type[Exception] | t.Type[Warning]] = (),
    ):
        self.old_sys_excepthook = sys.excepthook
        self.addHandler(DialogHandler(logging.WARNING, win))
        self.nonCriticalErrors = tuple(nonCriticalErrors)

        signal.signal(signal.SIGINT, signal.SIG_DFL)
        sys.excepthook = self.exceptWithLog

    def deregisterExceptions(self):
        sys.excepthook = self.old_sys_excepthook

    def registerWarnings(self):
        warnings.simplefilter("always", UserWarning)
        self.old_showwarning = warnings.showwarning
        warnings.showwarning = self.warnWithLog

    def warnWithLog(self, message, category, filename, lineno, file=None, line=None):
        """
        Copied logic from logging.captureWarnings implementation, but with short and
        long messages enabled
        """
        if file is not None:
            if self.old_showwarning is not None:
                self.old_showwarning(message, category, filename, lineno, file, line)
        else:
            detailedMsg = warnings.formatwarning(
                message, category, filename, lineno, line
            )
            self.warning(message, extra={"detailed": detailedMsg})

    def exceptWithLog(self, etype, evalue, tb):
        # Allow sigabort to kill the app
        app = QtWidgets.QApplication.instance()
        if etype in [KeyboardInterrupt, SystemExit]:
            app.exit(1)
            app.processEvents()
            raise

        if issubclass(etype, self.nonCriticalErrors):
            level = PrjEnums.LOG_LVL_ATTN
        else:
            level = logging.CRITICAL
        self.log(level, "", exc_info=(etype, evalue, tb))

    @classmethod
    def getAppLogger(cls, name=""):
        """
        logging.getLogger only can spawn Logger classes, so this method includes a
        temporary override of the spawned class so that an AppLogger can be registered
        instead.
        """
        oldCls = logging.getLoggerClass()
        try:
            logging.setLoggerClass(cls)
            # False positive, logger class is overridden
            # noinspection PyTypeChecker
            logger: cls = logging.getLogger(name)
        finally:
            logging.setLoggerClass(oldCls)
        return logger
