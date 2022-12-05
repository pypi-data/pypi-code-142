from pyqtgraph.dockarea import DockArea, Dock
from PyQt6 import QtWidgets,QtGui,QtCore
import numpy as np

class DescriptionDataDock(Dock):
    def __init__(self,keyEventHandler, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyEventHandler = keyEventHandler
        self.textArea = QtWidgets.QPlainTextEdit('')
        self.textArea.setReadOnly(True)
        self.textArea.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.addWidget(self.textArea)
        self.stateHidden = False
    def setText(self,text:str):
        self.textArea.setPlainText(text)
    def clearText(self):
        self.textArea.setPlainText(0)
    def updateStyle(self):
        Dock.updateStyle(self)
        self.setOrientation("horizontal")
    def keyPressEvent(self,event):
        self.keyEventHandler(event)
    def mhide(self):
        self.stateHidden = True
        Dock.hide(self)
    def mshow(self):
        self.stateHidden = False
        Dock.show(self)
    def hide(self):
        if self.stateHidden:
            Dock.hide(self)
    def show(self):
        if not self.stateHidden:
            Dock.show(self)