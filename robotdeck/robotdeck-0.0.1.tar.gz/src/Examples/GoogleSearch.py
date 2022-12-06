"""

Example showing how to use a library with a simple Google Search.
Of course, depending on your machine, it is required to modify/create the asset Library.

Please find more info on the official website.
"""

#pylint: disable=unused-import
import PySide2.QtWidgets            # To fix the .VSCode issue with Pylint
#pylint: enable=unused-import

from Browser import (
    Firefox
)

if __name__ == "__main__" :
    gui = Firefox(originX = 2560)
    gui.loadLibrary("/home/maximeg/AntWorkspace/RobotProjects/Assets/")

    gui.focus()
    gui.newTab()
    gui.sleep(.5)
    gui.writeText("http://www.google.com", "address")
    gui.enter()
    gui.sleep(.5)

    #Should be true
    print (gui.checkImage("google") is not None)

    gui.writeText("Robot Framework", "searchBar")
    gui.click("closeSuggestions")
    gui.click("searchBut")
    gui.closeTab()

    #Should be false
    print (gui.checkImage("google") is None)
