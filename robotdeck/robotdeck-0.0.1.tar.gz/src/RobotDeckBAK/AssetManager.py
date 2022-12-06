""" Asset Manager Module
"""

import time
import pyperclip

#pylint: disable=no-name-in-module
from PySide2.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
    QAction
)

from PySide2.QtCore import (
    Slot,
    Qt,
    QPoint
)

from PySide2.QtGui import (
    QKeySequence
)
#pylint: enable=no-name-in-module

from RobotDeck.AssetLibrary import (
    AssetLibrary
)

from RobotDeck.Tools import (
    AssetNameModal,
    PopupMenu,
    saveImage,
    getAssetManagerImageFolder
)

# TODO : We need to implement a setting system to handle those !
# PROJ_PATH = "/home/maximeg/AntWorkspace/Synergy/ValidationFramework/RobotTests/"
# ASSET_PATH = "LeagueOpsProject/Libraries/Assets"

PROJ_PATH = "/home/maximeg/AntWorkspace/Synergy/ValidationFramework/Projects/LeagueOps/"
ASSET_PATH = "Assets"

CURRENT_SCREEN = "currentScreen.png"

class AssetManager(QWidget):
    """ Asset Manager Class
    """

    def __init__(self):
        QWidget.__init__(self)

        self._generateLayout()
        self._generateDialogs()
        self._defineActions()
        self._setAreaCursor()
        self._connectSignals()

        # To manage asset
        self.assetName = ""
        self.assetStartPos = None
        self.assetEndPos = None
        self.imageMode = False
        self.areaMode = False

        self.assetLibrary = AssetLibrary(PROJ_PATH + ASSET_PATH)

    def mouseReleaseEvent(self, event):
        """ What happens when a mouse button is released
        """

        if event.button() == Qt.MouseButton.LeftButton :
            self._setAreaCursor(False)

            if self.imageMode :
                self._saveImage()

            elif self.areaMode :
                self._saveArea()

            self.imageMode = False
            self.areaMode = False

    def mousePressEvent(self, event):
        """ What happens when a mouse button has been pressed
        """
        if not self.imageMode and not self.areaMode :
            if event.button() == Qt.MouseButton.LeftButton :
                self._setAreaCursor(False)

                # If a menu option was chosen :
                if self.imageMode :
                    self._saveImage()

                elif self.areaMode :
                    self._saveArea()

                # Or when we're not coming from the menu :
                elif QApplication.keyboardModifiers() == Qt.NoModifier :
                    self.setPositionTriggered()

                elif QApplication.keyboardModifiers() == Qt.ShiftModifier :
                    self.setImageTriggered()

                elif QApplication.keyboardModifiers() == Qt.ControlModifier :
                    self.setAreaTriggered()

            elif event.button() == Qt.MouseButton.RightButton :
                self.menu.showMenu(event.globalPos())

    def keyPressEvent(self, event):
        """ Allows for Keyboard shortcuts
        """

        if event.key() == Qt.Key_F1 :
            self.setPositionTriggered()

        elif event.key() == Qt.Key_F2 :
            self.setImageTriggered()

        elif event.key() == Qt.Key_F3 :
            self.setAreaTriggered()

        elif event.key() == Qt.Key_F5 :
            if QApplication.keyboardModifiers() == Qt.ShiftModifier :
                self.delayedRefreshScreenTriggered()
            else :
                self.refreshScreenTriggered()

    @Slot()
    def setPositionTriggered(self):
        """ aze
        """

        self.assetStartPos = self.mapFromGlobal(self.cursor().pos())

        self._savePosition()

    @Slot()
    def setImageTriggered(self):
        """ aze
        """

        self.assetStartPos = self.mapFromGlobal(self.cursor().pos())

        self.imageMode = True
        self._setAreaCursor(True)

    @Slot()
    def setAreaTriggered(self):
        """ aze
        """

        self.assetStartPos = self.mapFromGlobal(self.cursor().pos())

        self.areaMode = True
        self._setAreaCursor(True)

    def _savePosition(self):
        if self._setAssetName("Position Name : ") :
            self.assetLibrary.setPosition(
                self.assetDialog.getAssetName(),
                self.assetStartPos,
                self.assetDialog.getAssetDesc()
            )

            # Should we save each time ?
            # If yes, then the backup mechanism needs to change !
            self.assetLibrary.saveAssetLibrary()

    def _saveImage(self):
        self.assetEndPos = self.mapFromGlobal(self.cursor().pos())

        if self._setAssetName("Image Name : ") :
            self.assetLibrary.setImage(
                str(getAssetManagerImageFolder().joinpath(CURRENT_SCREEN)),
                self.assetDialog.getAssetName(),
                self.assetStartPos,
                self.assetEndPos,
                self.assetDialog.getAssetDesc()
            )

            # Should we save each time ?
            # If yes, then the backup mechanism needs to change !
            self.assetLibrary.saveAssetLibrary()

    def _saveArea(self):
        self.assetEndPos = self.mapFromGlobal(self.cursor().pos())

        if self._setAssetName("Area Name : ") :
            self.assetLibrary.setArea(
                self.assetDialog.getAssetName(),
                self.assetStartPos,
                self.assetEndPos,
                self.assetDialog.getAssetDesc()
            )

            # Should we save each time ?
            # If yes, then the backup mechanism needs to change !
            self.assetLibrary.saveAssetLibrary()

    def _setAssetName(self, dialogTitle):
        self.assetDialog.setAssetName(pyperclip.paste())

        self.assetDialog.showDialog(dialogTitle)
        self.assetName = self.assetDialog.getAssetName()

        pyperclip.copy(self.assetName)

        return self.assetDialog.result() and self.assetName

    @Slot()
    def refreshScreenTriggered(self):
        """ Refresh the screen with a new screenshot
        """

        imgPath = str(getAssetManagerImageFolder().joinpath(CURRENT_SCREEN))

        saveImage(imgPath, QPoint(2560,0), QPoint(2560+1920, 1080))

        self.imgLabel.setPixmap(imgPath)

    @Slot()
    def delayedRefreshScreenTriggered(self):
        """ Refresh the screen with a new screenshot after a short delay.
        """

        time.sleep(2)
        self.refreshScreenTriggered()

    @Slot()
    def setLibraryTriggered(self):
        """ IMPLEMENTME
        """

        print(self.libName)

        #TODO : Implement this feature

    def _generateLayout(self):
        self.layout = QVBoxLayout()
        self.layout.setMargin(0)

        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(str(getAssetManagerImageFolder().joinpath(CURRENT_SCREEN)))
        self.layout.addWidget(self.imgLabel)

        self.setLayout(self.layout)

    def _generateDialogs(self):
        self.assetDialog = AssetNameModal()

    def _setAreaCursor(self, area = False):
        if not area :
            cursor = self.cursor()
            cursor.setShape(Qt.CursorShape.CrossCursor)
            self.setCursor(cursor)
        else :
            cursor = self.cursor()
            cursor.setShape(Qt.CursorShape.DragMoveCursor)
            self.setCursor(cursor)

    def _defineActions(self):
        self.actionPosition = QAction("Set Position")
        self.actionPosition.setShortcut(QKeySequence(Qt.Key_F1))

        self.actionImage = QAction("Set Image")
        self.actionImage.setShortcut(QKeySequence(Qt.Key_F2))

        self.actionSearchArea = QAction("Set Search Area")
        self.actionSearchArea.setShortcut(QKeySequence(Qt.Key_F3))

        self.actionRefreshScreen = QAction("Refresh Screen")
        self.actionRefreshScreen.setShortcut(QKeySequence(Qt.Key_F5))

        self.actionChangeLibrary = QAction("Change Library")

        self.menu = PopupMenu({
            "actionPosition" : self.actionPosition,
            "actionImage" : self.actionImage,
            "actionArea" : self.actionSearchArea,
            "actionRefresh" : self.actionRefreshScreen,
            "actionLibrary" : self.actionChangeLibrary
        })

    def _connectSignals(self):
        self.actionPosition.triggered.connect(self.setPositionTriggered)
        self.actionImage.triggered.connect(self.setImageTriggered)
        self.actionSearchArea.triggered.connect(self.setAreaTriggered)
        self.actionRefreshScreen.triggered.connect(self.refreshScreenTriggered)
        self.actionChangeLibrary.triggered.connect(self.setLibraryTriggered)
