from __future__ import annotations

import html
import logging
import sys
import typing as t
import weakref
from textwrap import wrap
from traceback import format_exception

import numpy as np
from pyqtgraph import QtCore, QtWidgets

from qtextras import fns


class ScrollableMessageDialog(QtWidgets.QDialog):
    def __init__(
        self,
        parent: QtWidgets.QWidget = None,
        messageType="Information",
        msg="",
        detailedMsg="",
    ):
        super().__init__(parent)
        style = self.style()
        self.setModal(True)

        styleIcon = getattr(
            QtWidgets.QStyle.StandardPixmap, f"SP_MessageBox{messageType}"
        )
        self.setWindowTitle(messageType)
        self.setWindowIcon(style.standardIcon(styleIcon))

        verticalLayout = QtWidgets.QVBoxLayout(self)

        scrollArea = QtWidgets.QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollAreaWidgetContents = QtWidgets.QWidget()

        scrollLayout = QtWidgets.QVBoxLayout(scrollAreaWidgetContents)

        # Set to message with trace first so sizing is correct
        msgLbl = QtWidgets.QLabel(detailedMsg, scrollAreaWidgetContents)
        msgLbl.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextSelectableByMouse
            | QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard
        )
        msgLbl.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        scrollLayout.addWidget(
            msgLbl,
            0,
            QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop,
        )
        scrollArea.setWidget(scrollAreaWidgetContents)
        verticalLayout.addWidget(scrollArea)

        btnLayout = QtWidgets.QHBoxLayout()
        ok = QtWidgets.QPushButton("Ok", self)
        toggleTrace = QtWidgets.QPushButton("Toggle Details", self)
        btnLayout.addWidget(ok)
        btnLayout.addWidget(toggleTrace)
        spacerItem = QtWidgets.QSpacerItem(
            ok.width(),
            ok.height(),
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum,
        )
        ok.clicked.connect(self.close)

        sh = self.sizeHint()
        newWidth = max(sh.width(), self.width())
        newHeight = max(sh.height(), self.height())
        self.resize(newWidth, newHeight)

        showDetailedMsg = False

        def updateTxt():
            nonlocal showDetailedMsg
            if showDetailedMsg:
                newText = detailedMsg.replace("\n", "<br>")
                msgLbl.setTextFormat(QtCore.Qt.TextFormat.RichText)
            else:
                newLines = msg.splitlines()
                allLines = []
                for line in newLines:
                    if line == "":
                        line = [line]
                    else:
                        line = wrap(line)
                    allLines.extend(line)
                newText = "<br>".join(allLines)
                msgLbl.setTextFormat(QtCore.Qt.TextFormat.RichText)
            showDetailedMsg = not showDetailedMsg
            msgLbl.setText(newText)

        self.msgLbl = msgLbl
        toggleTrace.clicked.connect(lambda: updateTxt())

        btnLayout.addItem(spacerItem)
        verticalLayout.addLayout(btnLayout)
        self.toggleTrace = toggleTrace
        ok.setFocus()
        updateTxt()


class QtAppHandler(logging.Handler):
    _weakWindow: weakref.ReferenceType = None

    def __init__(
        self, level, win: QtWidgets.QMainWindow = None, exceptionsOnly=False
    ) -> None:
        super().__init__(level)
        self.attachToWindow(win)
        self.exceptionsOnly = exceptionsOnly

    def attachToWindow(self, win=None):
        if win is not None:
            win = weakref.ref(win)
        self._weakWindow = win

    def getWindow(self) -> t.Optional[QtWidgets.QMainWindow]:
        if self._weakWindow is None:
            return None
        return self._weakWindow()


class DialogHandler(QtAppHandler):
    def emit(self, record: logging.LogRecord):
        if record.exc_info:
            msg = html.escape(str(record.exc_info[1]))
            excStr = "".join(format_exception(*record.exc_info))
            detailed = html.escape(excStr)
        else:
            msg = super().format(record)
            detailed = getattr(record, "detailed", msg)
        dlgType = "Critical" if record.levelno == logging.CRITICAL else "Information"

        dlg = ScrollableMessageDialog(self.getWindow(), dlgType, msg, detailed)

        def doExec():
            dlg.exec()

        # Using function instead of directly connecting to dlg.exec keeps garbage from
        # being collected just long enough
        QtCore.QTimer.singleShot(0, doExec)

    def filter(self, record: logging.LogRecord):
        """
        Optionally only activates this handler if the message came from an exception
        """
        if not self.exceptionsOnly:
            return super().filter(record)
        try:
            return len(record.exc_info) > 1
        except Exception:
            return False


class TimedMessageHandler(QtAppHandler):
    def __init__(
        self, *args, defaultMsgtimeout_ms=3000, maxLevel=None, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.defaultMsgTimeout = defaultMsgtimeout_ms
        if maxLevel is None:
            maxLevel = sys.maxsize
        self.maxLevel = maxLevel

    def emit(self, record: logging.LogRecord):
        win = self.getWindow()
        if win is None:
            return
        if hasattr(record, "msgTimeout"):
            msgTimeout = record.msgTimeout
        else:
            msgTimeout = self.defaultMsgTimeout
        self.makeNotification(self.format(record), msgTimeout)

    def filter(self, record: logging.LogRecord):
        return record.levelno <= self.maxLevel and logging.Handler.filter(self, record)

    def makeNotification(self, msg: str, timeout_ms: int = None):
        raise NotImplementedError


class StatusBarHandler(TimedMessageHandler):
    def makeNotification(self, msg: str, timeout_ms: int = None):
        self.getWindow().statusBar().showMessage(msg, timeout_ms)


class FadeNotifyHandler(TimedMessageHandler):
    updateFps = 10

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If references aren't kept to labels, they will caused wrapped c++ deletion
        # errors List instead of single ref since multiple messages can exist at once
        # Dict to also associate animations with their window
        self.msgRefs = {}

    def makeNotification(self, msg: str, timeout_ms: int = None):
        """
        Creates a fading green dialog that shows the message and disappears after
        timeout
        """
        style = """\
    QLabel {
      background-color: #0f0;
      border: 1px solid #000;
      color: #000;
    };
    """
        fadeMsg = QtWidgets.QLabel(msg, self.getWindow())
        fadeMsg.setStyleSheet(style)
        # For some reason, width doesn't set properly here
        fadeMsg.setFixedWidth(fadeMsg.sizeHint().width())
        fadeMsg.setAlignment(QtCore.Qt.AlignCenter)
        fadeMsg.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        parent: QtWidgets.QMainWindow = self.getWindow()
        if parent is not None:
            metrics = fadeMsg.fontMetrics()
            padding = (parent.width() - metrics.width(msg)) // 2
            msgX = padding
            # Make sure multiple messages don't overlap
            msgY = int(0.05 * parent.height())
            msgY += self.getUniqueLblOffset(msgY)
            fadeMsg.move(msgX, msgY)
        anim = self.makeAnimation(fadeMsg, timeout_ms)
        # 10 fps
        anim.start(1000 // self.updateFps)
        fadeMsg.show()

    def getUniqueLblOffset(self, constHeight):
        allYPos = np.array([label.pos().y() - constHeight for label in self.msgRefs])
        if not len(allYPos):
            return 0
        height = next(iter(self.msgRefs)).height()
        offset = 0
        recalc = True
        while recalc:
            offset += 0.8 * height
            recalc = np.min(np.abs(allYPos - offset)) < 0.01
        return offset

    def closeMsgWidget(self, msgWidget):
        """
        Closes the specified messages and deletes corresponding references
        """
        msgWidget.hide()
        msgWidget.deleteLater()
        self.msgRefs[msgWidget].deleteLater()
        del self.msgRefs[msgWidget]

    def makeAnimation(self, widget, timeout_ms):
        """
        The default method of using a PropertyAnimation doesn't repaint the widget,
        so do it a quick and dirty way using timers manually
        """

        def changeOpacity():
            for opacity in np.linspace(1, 0, int(timeout_ms / 1000 * self.updateFps)):
                effect.setOpacity(opacity)
                # widget.update()
                yield
            # Animation done, wait one tick to prevent overlaps
            yield
            self.closeMsgWidget(widget)

        # Don't start right away
        effect = QtWidgets.QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        anim = fns.timedExec(changeOpacity, interval_ms=0)
        self.msgRefs[widget] = anim
        return anim
