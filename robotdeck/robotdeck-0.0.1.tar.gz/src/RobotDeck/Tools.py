""" Asset Manager Tools module

Copyright 2020 - 2021 Ant Solutions SRL (info@ant-solutions.be)

"""

import os

from pathlib import (
    Path
)

from PIL import (
    Image,
    ImageGrab
)

#------------------------------------------
# To fix the .VSCode issue with Pylint
#pylint: disable=unused-import
#pylint: disable=import-error
#pylint: disable=no-name-in-module
#------------------------------------------
from PySide2.QtWidgets import (
    QMenu,
    QDialog,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit
)
#------------------------------------------
# To fix the .VSCode issue with Pylint
#pylint: disable=unused-import
#pylint: disable=import-error
#pylint: disable=no-name-in-module
#------------------------------------------

def getAssetManagerImageFolder():
    """ Will return the folder in which AssetManager images are stored.
    Also, the function will create the folder if it doesn't exist.
    """

    path = Path(str(Path.home()) + "/.robotlab/AssetManager/Images/")
    path.mkdir(parents=True, exist_ok=True)

    return path

def getRobotLabConfigFolder():
    """ Will return the folder in which the RobotLab will store its config file.
    Also, the function will create the folder if it doesn't exist.
    """

    path = Path(str(Path.home()) + "/.robotlab/Configs/")
    path.mkdir(parents=True, exist_ok=True)

    return path


class PopupMenu(QMenu) :
    """ Popup Menu for the Asset Manager
    """

    def __init__( self, actions):

        QMenu.__init__(self)
        self.buildMenu(actions)

    def showMenu(self, position):
        """ Displays the menu at the requested position
        """

        self.exec_(position)

    def buildMenu(self, actions):
        """ Build the menu with the given action
        """

        self.clear()

        self.addAction(actions["actionPosition"])
        self.addAction(actions["actionImage"])
        self.addAction(actions["actionArea"])

        self.addSeparator()

        self.addAction(actions["actionRefresh"])
        self.addAction(actions["actionLibrary"])

class AssetNameModal(QDialog) :
    """ Asset Name Modal Class
    """

    def __init__(self):
        QDialog.__init__(self)

        self._generateLayout()
        self._connectSignals()

        self.setWindowTitle("Saving Asset ...")
        self.setModal(True)

    def showDialog(self, assetTitle = "Choose a name : "):
        """ Reinitialize & show the dialog
        """

        self.assetLab.setText(assetTitle)

        QDialog.exec_(self)

    def setAssetName(self, assetName = "") :
        """ Specifies a proposition for the asset name
        """

        self.assetEdit.setText(assetName)

    def getAssetName(self):
        """ Returns the chosen asset name
        """

        return self.assetEdit.text()

    def setAssetDesc(self, assetDesc = "") :
        """ Specifies a proposition for the asset description
        """

        self.descEdit.setText(assetDesc)

    def getAssetDesc(self):
        """ Returns the chosen asset description
        """

        return self.descEdit.text()

    def _generateLayout(self):
        # Asset Name Line
        self.assetLab = QLabel()
        self.assetEdit = QLineEdit()

        nameLayout = QHBoxLayout()
        nameLayout.addWidget(self.assetLab)
        nameLayout.addWidget(self.assetEdit)

        # Decription Line
        self.descLab = QLabel("Desc : ")
        self.descEdit = QLineEdit()
        self.descEdit.setPlaceholderText("optional description ...")

        descLayout = QHBoxLayout()
        descLayout.addWidget(self.descLab)
        descLayout.addWidget(self.descEdit)

        # Confirm Button
        self.assetBut = QPushButton()
        self.assetBut.setText("Confirm")

        butLayout = QHBoxLayout()
        butLayout.addStretch()
        butLayout.addWidget(self.assetBut)

        # General Layout
        diagLayout = QVBoxLayout()
        diagLayout.addLayout(nameLayout)
        diagLayout.addLayout(descLayout)
        diagLayout.addLayout(butLayout)

        self.setLayout(diagLayout)

    def _connectSignals(self):
        self.assetBut.clicked.connect(self.accept)

def arrangeCoords(origX, origY, destX, destY):
    """ Will rearrange coordinates to make sure origin is smaller than destination !
    """

    if origX > destX :
        origX, destX = destX, origX

    if origY > destY :
        origY, destY = destY, origY

    return (origX, origY, destX, destY)

def saveImage(fileUri, origin, dest, fromUri = ""):
    """ Will take a screenshot with the top left
    """

    if not fromUri :
        fromUri = str(getAssetManagerImageFolder().joinpath(".TEMP_IMAGE.png"))

        try :
            os.remove(fromUri)
        except FileNotFoundError :
            pass

        screenshot = ImageGrab.grab()
        screenshot.save(fromUri)

    origX, origY, destX, destY = arrangeCoords(origin.x(), origin.y(), dest.x(), dest.y())

    image = Image.open(fromUri)
    image = image.crop((origX, origY, destX, destY))
    image.save(fileUri)
