""" Launcher for the Robot Deck project. Opens on the TestManager.

Copyright 2020 - 2021 Ant Solutions SRL (mgilles@ant-solutions.be)

TODO : Implement the PIP checks in here instead of the bash script.

"""

import site
import sys

#------------------------------------------
# To fix the .VSCode issue with Pylint
#pylint: disable=unused-import
#pylint: disable=import-error
#pylint: disable=no-name-in-module
#------------------------------------------
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
#------------------------------------------
# To fix the .VSCode issue with Pylint
#pylint: enable=unused-import
#pylint: enable=import-error
#pylint: enable=no-name-in-module
#------------------------------------------

# Set up the application
app = QGuiApplication(sys.argv)

# Load the Interface
interface = QQmlApplicationEngine()
interface.load(site.getsitepackages()[0] + "/RobotDeck/Interface/TestManager.qml")

# Start the Application
app.exec()
