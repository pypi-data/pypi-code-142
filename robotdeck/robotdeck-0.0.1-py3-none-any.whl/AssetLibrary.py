""" Asset Library Module
"""

import os
import shutil

from datetime import (
    datetime
)

from pathlib import (
    Path
)

#------------------------------------------
# To fix the .VSCode issue with Pylint
#pylint: disable=unused-import
#pylint: disable=import-error
#pylint: disable=no-name-in-module
#------------------------------------------
from RobotDeck.Tools import (
    arrangeCoords,
    saveImage
)
#------------------------------------------
# To fix the .VSCode issue with Pylint
#pylint: enable=unused-import
#pylint: enable=import-error
#pylint: enable=no-name-in-module
#------------------------------------------

class AssetLibrary:
    """ Asset Management Library
    """

    _assetPath = None
    _libPath = None

    _profileName = ""
    _libName = ""

    _waits = {}
    _positions = {}
    _images = {}
    _areas = {}

    _backupFolder = "Backup/"
    _keepBackups = 3

    def __init__(self, assetPath, profileName = "DefaultProfile", libName = "DefaultLibrary"):
        self._assetPath = Path(os.path.abspath(assetPath))
        self.loadAssetLibrary(profileName, libName)

    def getAssetPath(self):
        """ Retrieve the path to assets
        """

        return self._assetPath

    def getProfileName(self):
        """ Retrieve the name of the profile
        """

        return self._profileName

    def getLibraryName(self):
        """ Retrieve the name of the library
        """

        return self._libName

    def setWaitTime(self, waitName, milliseconds, _desc = ""):
        """ Add a new waiting time to the library, or replace it if already existing.
        """

        self._waits[waitName] = (milliseconds,_desc)

    def getWaitTime(self, waitName):
        """ Return the request waiting time.
        """

        return self._waits[waitName]

    def setPosition(self, posName, pos, _desc = ""):
        """ Add a new position to the library, or replace it if already existing.
        """

        self._positions[posName] = (pos.x(), pos.y(), _desc)

    def getPosition(self, posName):
        """ Return the request position.
        """

        return self._positions[posName]

    def setImage(self, imgSource, imgName, origin, dest, _desc = ""):
        """ Add a new image to the library, or replace it if already existing.
        """

        saveImage(
            str(self._libPath.joinpath("Images/" + imgName + ".png")),
            origin,
            dest,
            imgSource
        )

        origX, origY, destX, destY = arrangeCoords(origin.x(), origin.y(), dest.x(), dest.y())
        self._images[imgName] = (origX, origY, destX, destY, _desc)

    def getImage(self, imgName):
        """ Return the request image information.
        """

        return self._images[imgName]

    def getImageFile(self, imgName):
        """ Return the request image file (as .png file)
        """

        return str(self._libPath.joinpath(f"Images/{imgName}.png"))

    def setArea(self, areaName, origin, dest, _desc = ""):
        """ Add a new area to the library, or replace it if already existing.
        """

        origX, origY, destX, destY = arrangeCoords(origin.x(), origin.y(), dest.x(), dest.y())

        self._areas[areaName] = (origX, origY, destX, destY, _desc)

    def getArea(self, areaName):
        """ Return the request area.
        """

        return self._areas[areaName]

    def loadAssetLibrary(self, profileName = "", libName = ""):
        """ Will load the library of a given profile. \
            If no profile or libName is given, the current library will be reloaded.
        """

        if profileName :
            self._profileName = profileName

            # Re-computing library path
            self._computeLibPath()

        if libName :
            self._libName = libName

            # Re-computing library path
            self._computeLibPath()

        if self._profileName and self._libName :
            # Re-init the dictionaries
            self._waits = {}
            self._positions = {}
            self._images = {}
            self._areas = {}

            # Reading library files.
            self._readWaits()
            self._readPositions()
            self._readImages()
            self._readAreas()
        else :
            raise Exception(f"Library '{self._libName}' in profile '{self._profileName}' \
doesn't not exist !")

    def saveAssetLibrary(self, profileName = "", libName = ""):
        """ Will save the library in the given profile.
            If no profile or libName is given, the current library will be overriden.
            Also, before overriding a library, a backup will be saved.
        """

        if profileName :
            self._profileName = profileName

            # Re-computing library path
            self._computeLibPath()

        if libName :
            self._libName = libName

            # Re-computing library path
            self._computeLibPath()

        # Saving files.
        self._saveWaits()
        self._savePositions()
        self._saveImages()
        self._saveAreas()

    def saveBackup(self):
        """
        Saving a new backup, with a suffix based on Python's timestamp.
        """

        if self._libPath.exists() :
            try :
                shutil.copytree(
                    self._libPath,
                    self._libPath.parent.joinpath(
                        self._backupFolder + self._libName + str(datetime.now().timestamp())
                    )
                )
            except FileExistsError :
                pass

        # Removing old backups and keeping only the last 'self.keepBackups' amount, typically 3.
        count = 0

        for dirName in sorted(
                self._libPath.parent.joinpath(self._backupFolder).iterdir(), reverse=True
            ):

            if count >= self._keepBackups :
                shutil.rmtree(dirName)
            count += 1

    def restoreLibrary(self):
        """ Restore a library from a previously taken backup.
        NOT IMPLEMENTED : For now, simply copy paste the backup library \
            in the correct folder for revovery.
        """

        # TODO : Implement this method !

    def _computeLibPath(self):
        self._libPath = self._assetPath.joinpath("%s/%s" % (self._profileName, self._libName))

        if not self._libPath.exists() :
            self._libPath.mkdir(parents=True)

            imagePath = self._libPath.joinpath("Images")
            imagePath.mkdir(parents=True)

    def _readWaits(self):
        try :
            with open(self._libPath.joinpath("waits.csv"), "r") as library :

                for line in library.readlines():
                    if line.lstrip()[0] != "#" :            # Ignore comments (& titles)
                        line = line.split(',')
                        self._waits[line[0].strip()] = (
                            int(line[1]),
                            line[2].strip()
                        )
        except FileNotFoundError :
            file = open(self._libPath.joinpath("waits.csv"), "w")
            file.write("#Empty File Created !")
            file.close()

    def _readPositions(self):
        try :
            with open(self._libPath.joinpath("positions.csv"), "r") as library :
                for line in library.readlines():
                    if line.lstrip()[0] != "#" :            # Ignore comments (& titles)
                        line = line.split(',')
                        self._positions[line[0].strip()] = (
                            int(line[1]),
                            int(line[2]),
                            line[3].strip()
                        )
        except FileNotFoundError :
            file = open(self._libPath.joinpath("positions.csv"), "w")
            file.write("#Empty File Created !")
            file.close()

    def _readImages(self):
        try :
            with open(self._libPath.joinpath("images.csv"), "r") as library :
                for line in library.readlines():
                    if line.lstrip()[0] != "#" :            # Ignore comments (& titles)
                        line = line.split(',')

                        line[1], line[2], line[3], line[4] = arrangeCoords(
                            int(line[1]),
                            int(line[2]),
                            int(line[3]),
                            int(line[4])
                        )

                        self._images[line[0].strip()] = (
                            line[1],
                            line[2],
                            line[3],
                            line[4],
                            line[5].strip()
                        )
        except FileNotFoundError :
            file = open(self._libPath.joinpath("images.csv"), "w")
            file.write("#Empty File Created !")
            file.close()

    def _readAreas(self):
        try :
            with open(self._libPath.joinpath("areas.csv"), "r") as library :
                for line in library.readlines():
                    if line.lstrip()[0] != "#" :            # Ignore comments (& titles)
                        line = line.split(',')

                        line[1], line[2], line[3], line[4] = arrangeCoords(
                            int(line[1]),
                            int(line[2]),
                            int(line[3]),
                            int(line[4])
                        )

                        self._areas[line[0].strip()] = (
                            line[1],
                            line[2],
                            line[3],
                            line[4],
                            line[5].strip()
                        )
        except FileNotFoundError :
            file = open(self._libPath.joinpath("areas.csv"), "w")
            file.write("#Empty File Created !")
            file.close()

    def _saveWaits(self):
        with open(self._libPath.joinpath("waits.csv"), "w") as library :

            library.write("#Name                         , Time (ms), Description\n")
            for wait in self._waits :
                library.write(
                    f"{wait:<30}, \
{self._waits[wait][0]:>9}, \
{self._waits[wait][1]}\n") # in ms!

    def _savePositions(self):
        with open(self._libPath.joinpath("positions.csv"), "w") as library :

            library.write("#Name                         , Pos X, Pos Y, Description\n")
            for pos in self._positions :
                library.write(
                    f"{pos:<30}, \
{self._positions[pos][0]:>5}, \
{self._positions[pos][1]:>5}, \
{self._positions[pos][2]}\n")

    def _saveImages(self):
        with open(self._libPath.joinpath("images.csv"), "w") as library :

            library.write(
                "#Name                         , Org X, Org Y, DestX, DestY, Description\n")
            for img in self._images :
                library.write(
                    f"{img:<30}, \
{self._images[img][0]:>5}, \
{self._images[img][1]:>5}, \
{self._images[img][2]:>5}, \
{self._images[img][3]:>5}, \
{self._images[img][4]}\n")

    def _saveAreas(self):
        with open(self._libPath.joinpath("areas.csv"), "w") as library :

            library.write(
                "#Name                         , Org X, Org Y, DestX, DestY, Description\n")
            for area in self._areas :
                library.write(
                    f"{area:<30}, \
{self._areas[area][0]:>5}, \
{self._areas[area][1]:>5}, \
{self._areas[area][2]:>5}, \
{self._areas[area][3]:>5}, \
{self._areas[area][4]}\n")
