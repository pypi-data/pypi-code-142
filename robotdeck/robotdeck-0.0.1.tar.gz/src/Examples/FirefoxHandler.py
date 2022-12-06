""" Firefox Handler Module
"""

import pyperclip as CLIP
import pyautogui as PAG

from RobotModules.LeagueOps.Libraries.Utilities.PAGObject import PAGObject

class FirefoxHandler (PAGObject):
    """ Firefox Handler class
    """

    # Position to get focus
    # Default = Firefox is available for click at top left of the screen
    pos_focusX = 15
    pos_focusY = 15

    assetLib = None

    fullscreen = True
    lastAction = ""

    #pylint: disable=no-self-use
    def displayInstructions(self):
        """ Displays instructions on how to use the class
        """

        PAG.alert("Please, make sure to :\n\
            - leave the top left area of the screen free)")

    def setAssetLib(self, assetLib):
        """ Set the asset library to use
        """

        self.assetLib = assetLib

    def getFocus(self, posX = pos_focusX, posY = pos_focusY):
        """ Acquire the focus of the Firefox application window
        """

        PAG.click(self.originX + posX, self.originY + posY)

    #pylint: disable=no-self-use
    def toggleFullscreen(self):
        """ Toggle Firefox fullscreen mode
        """

        # Moving cursor away from top left if it is there.
        PAG.moveTo(self.originX + 200, self.originY + 200)
        PAG.sleep(.01)

        PAG.press("f11")

        # To make sure we skip the animation -> Is it required ?
        PAG.sleep(.5)

    def newTab(self, url = ""):
        """ Add a new tab to Firefox
        """

        PAG.hotkey("ctrl", "t")

        if url :
            self._writeTextSafe(url)
            PAG.press("enter")

    #pylint: disable=no-self-use
    def closeTab(self, confirm = False):
        """ Close the current firefox tab
        """

        # Check if we're still in fullscreen !
        PAG.press("f11")
        PAG.sleep(.01)
        PAG.hotkey("ctrl", "w")

        if confirm :
            PAG.press("enter")

    def writeText(self, position, text):
        """ Write text at a given position
        """

        self.clickPosition(position)
        self._writeTextSafe(text)

    def clickPosition(self, position):
        """ Move the cursor to a give position and clicks with the mouse
        """

        pos = self.assetLib.positions[position]
        PAG.click(self.originX + pos[0], self.originY + pos[1])

    def checkRegion(self, region):
        """ Check if a region is similar to what it used to be.
        """

        # This code should probably move to the AssetLibrary class
        image = "RobotModules/LeagueOps/Libraries/Assets/" + \
            self.assetLib.libName + "/Images/" + region + ".png"

        region = self.assetLib.regions[region]

        return PAG.locateOnScreen(
            image,
            region = (self.originX + region[0], self.originY + region[1], region[2], region[3]),
            confidence=self.assetLib.imgConfidence)

    def _writeTextSafe(self, text):
        """ Write the text with a copy paste instead of hitting each key.
        It prevents international keyboard issues.
        """

        #! Adapt for MacOS using the check on "Darwin" !
        CLIP.copy(text)
        PAG.hotkey("ctrl", "v")
