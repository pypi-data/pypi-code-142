"""
The Virtual User Interface is used to enable Robot to interact with its environment
    through virtual controls :

 * Mouse interaction : mouvements and clicks.
 * Keyboard interaction
 * Text interaction (copy & paste)
 * Visual comparison (with Image & OpenCV)
 *


Copyright 2020 - 2021 Ant Solutions SRL (info@ant-solutions.be)

"""

import pyautogui as PAG

from pyperclip import copy

# ------------------------------------------
# To fix the .VSCode issue with Pylint
# pylint: disable=unused-import
# pylint: disable=import-error
# pylint: disable=no-name-in-module
# ------------------------------------------
from RobotDeck.AssetLibrary import (
    AssetLibrary
)
#------------------------------------------
# To fix the .VSCode issue with Pylint
#pylint: enable=unused-import
#pylint: enable=import-error
#pylint: enable=no-name-in-module
#------------------------------------------

###---------------------------------------------------------------------------------------
### Basic Virtual Interface
###

class VirtualUserInterface:
    """
    The basic class for the VirtualUserInterface (VUI).

    - It is essentially a layer over PyAutoGui to make user of an asset library.
    - It also adds some shortcuts as quality of life improvements
    """
    _originX = 0
    _originY = 0
    _sizeX = 1920
    _sizeY = 1080

    _library = None

    _imgConfidence = 0.9            # 0 < confidence <= 1
    _searchMargin = 0               # in pixels

    def __init__(self, originX = 0, originY = 0, sizeX = 1920, sizeY = 1080):
        """ Create the manipulator object. If nothing is specified, it will create a
        default Full HD screen.
        """

        self.setFrame(originX, originY, sizeX, sizeY)

    def setFrame(self, originX, originY, sizeX, sizeY):
        """ Will set the frame within the GUIManipulator will operate.
        """

        self._originX = int(originX)
        self._originY = int(originY)
        self._sizeX = int(sizeX)
        self._sizeY = int(sizeY)

    def setLibrary(self, library):
        """ Assign the library to use in the manipulator.
        """

        self._library = library

    def getLibrary(self):
        """ Returns the library currently in use.
        """

        return self._library

    def loadLibrary(self, path, profile = "DefaultProfile", library = "DefaultLibrary"):
        """ Will load a library based on provided path, profile and name.
        """

        self._library = AssetLibrary(path, profile, library)

    def setImageConfidence(self, confidence):
        """ Define the image confidence to use when comparing images. (Defaults to 0.9).
        """

        self._imgConfidence = confidence

    def getImageConfidence(self):
        """ Returns the image confidence currently in use.
        """

        return self._imgConfidence

    def setSearchMargin(self, margin):
        """ Define the margin around the region in which the manipulator will search for
        an image. (Defaults to 0)
        """

        self._searchMargin = margin

    def getSearchMargin(self):
        """ Returns the search margin currently in use.
        """

        return self._searchMargin

###---------------------------------------------------------------------------------------
###     PyAutoGui overloaded methods : will make use of the AssetLibrary when relevant.
###

    def alert(self, text, useLibrary = False):
        """ Display the text in an alert box. (NO LIBRABRY USE YET!)
        """
        if useLibrary and not self._library :
            raise Exception("No Library was provided !")

        PAG.alert(text)         # Implement in library !!!

    def press(self, key, useLibrary = False):
        """ Press the keyboard key (available keys provided by PyAutoGui) (NO LIBRABRY USE YET!)
        """
        if useLibrary and not self._library :
            raise Exception("No Library was provided !")

        PAG.press(key)          # Implement in library !!!

    def hotkey(self, *keys, useLibrary = False):
        """ Triggers a hotkey sequence. (NO LIBRABRY USE YET!)
        """

        if useLibrary and not self._library :
            raise Exception("No Library was provided !")

        PAG.hotkey(*keys)       # Implement in library !!!

    def click(self, position, offX = 0, offY = 0):
        """ Click on the provided position defined in the library.

            offX & offY allow, respectively, to add an offset to x or y coordinates.
        """

        self._checkLibrary()

        pos = self._library.getPosition(position)
        PAG.click(self._originX + pos[0] + offX, self._originY + pos[1] + offY)

    def doubleClick(self, position):
        """ Double click on the provided position defined in the library.
        """

        self._checkLibrary()

        pos = self._library.getPosition(position)
        PAG.doubleClick(self._originX + pos[0], self._originY + pos[1])

    def tripleClick(self, position):
        """ Triple click on the provided position defined in the library.
        """

        self._checkLibrary()

        pos = self._library.getPosition(position)
        PAG.tripleClick(self._originX + pos[0], self._originY + pos[1])

    def sleep(self, wait):
        """ Wait for the amount of time defined in the library.
        """

        if isinstance(wait, (int, float)):
            PAG.sleep(wait)

        elif isinstance(wait, str):
            self._checkLibrary()

            wait = self._library.getWaitTime(wait)
            PAG.sleep(wait[0])

        else:
            raise TypeError("Type is not correct, must be int, float or string")

    def moveTo(self, position):
        """ Move the mouse to the position defined in the library.
        """

        self._checkLibrary()

        pos = self._library.getPosition(position)
        PAG.moveTo(self._originX + pos[0], self._originY + pos[1])

    def locateOnScreen(self, image, area = None):
        """ Will locate the image from the library inside the given area, also from the library.
        If the area is not provided, the entire frame will be used.
        """

        self._checkLibrary()

        if area :
            area = self._library.getArea(area)

            region = (
                max(self._originX + area[0] - self._searchMargin, 0),
                max(self._originY + area[1] - self._searchMargin, 0),
                area[2]-area[0] + self._searchMargin * 2,  # We need the size, and not the position
                area[3]-area[1] + self._searchMargin * 2   # margin * 2 removed it in the origin.
            )

        else :
            region = (
                self._originX,
                self._originY,
                self._sizeX,
                self._sizeY
            )

        imageFile = self._library.getImageFile(image)
        return PAG.locateOnScreen(
            imageFile,
            region = region,
            confidence = self._imgConfidence
        )


###---------------------------------------------------------------------------------------
###     Additional methods : augmenting or fixing caveats from PyAutoGui
###
    def writeText(self, text, position = None):
        """ Will write a text safely. If position is provided, the manipulator will click on
        the widget before copying the text.
        """

        self._checkLibrary()

        if position :
            self.click(position)

        # Copy the provided text in the clipboard, this way we avoid keyboard layout issues.
        copy(text)
        PAG.hotkey("ctrl", "v")

    def checkImage(self, image, retries=0, interval=.5, area=None):
        """ Check if a previously saved image is still the same.

            It is possible to specify the number of retries for looking for the image,
            as well as the interval time between each try. Is it useful when trying to check images
            that needs time to load for example.

            It is also possible to specify a different area in which to search for the image (i.e.
            a different area than the one provided by the image)
        """

        self._checkLibrary()

        img = self._library.getImage(image)

        if area is not None :
            area = self._library.getArea(area)

            region = (
            max(self._originX + area[0] - self._searchMargin, 0),
            max(self._originY + area[1] - self._searchMargin, 0),
            area[2]-area[0] + self._searchMargin * 2 ,   # We need the size, and not the position
            area[3]-area[1] + self._searchMargin * 2     # margin * 2 removed it in the origin
            )
        else :
            region = (
                max(self._originX + img[0] - self._searchMargin, 0),
                max(self._originY + img[1] - self._searchMargin, 0),
                img[2]-img[0] + self._searchMargin * 2 ,   # We need the size, and not the position
                img[3]-img[1] + self._searchMargin * 2     # margin * 2 removed it in the origin
            )

        imageFile = self._library.getImageFile(image)

        result = None
        currTry = 0
        while result is None and currTry <= retries:
            result = PAG.locateOnScreen(
                imageFile,
                region = region,
                confidence = self._imgConfidence
            )

            currTry += 1
            PAG.sleep(interval)

        return result

    def enter(self):
        """ Shortcut to press 'enter'
        """
        self._checkLibrary()

        PAG.press("enter")

    def esc(self):
        """ Shortcut to press 'esc'
        """

        self._checkLibrary()

        PAG.press("esc")

###---------------------------------------------------------------------------------------
###     Private Methods
###
    def _checkLibrary(self):
        if not self._library :
            raise Exception("No Library was provided !")


###---------------------------------------------------------------------------------------
### Specialized Interfaces
###
class Browser(VirtualUserInterface) :
    """ Implement extra GUI manipulation for a typical browser usage, such as new tab creation
    """

    def newTab(self):
        """ Create a new tab in the browser
        """

        self._checkLibrary()

        PAG.hotkey("ctrl", "t")

    def closeTab(self):
        """ Close the current tab in the browser
        """

        self._checkLibrary()

        PAG.hotkey("ctrl", "w")

    def refresh(self, ignoreCache = False):
        """ Reload the page.

            if ignoreCache is True, the page will be reloaded and cache overriden.
        """

        self._checkLibrary()

        if ignoreCache :
            PAG.hotkey("ctrl", "f5")
        else :
            PAG.press("f5")

    def fullscreen(self, wait=0):
        """ Toggles fullscreen : ! doesn't check if already fullscreen or not.

            It is possible to specify a wait time to cope with some fullscreen animation
            like in Firefox.
        """

        self._checkLibrary()

        PAG.press("f11")

        if wait:
            PAG.sleep(wait)

    def focus(self, position = None):
        """ Tries and grab the focus for the browser.
            If no position is passed, the top left corner will be used.

            ! This is not to grab the focus of a page element, check below for such functions.
        """

        self._checkLibrary()

        if position :
            self.click(position)
        else :
            PAG.click(self._originX + 20, self._originY + 5)

    def focusNext(self):
        """ Select the next focusable object on the page.
        """

        self._checkLibrary()

        PAG.press("tab")

    def focusPrevious(self):
        """ Select the previous focusable object on the page.
        """

        self._checkLibrary()

        PAG.hotkey("shift", "tab")

class Firefox(Browser):
    """ Class specialized for Firefox
    """

class Chrome(Browser):
    """ Class specialized for Chrome
    """
