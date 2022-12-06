""" Asset Library Module
"""

class AssetLibrary:
    """ Asset Management Library
    """

    libName = None

    waits = None
    regions = None
    positions = None

    imgConfidence = None

    def __init__(self, libName = None, imgConfidence=0.9):
        self.libName = libName
        self.imgConfidence = imgConfidence

        if libName :
            self.readAssetLib(libName)

    def readAssetLib(self, libName = None):
        """ Parse and load the Asset Library
        """

        if libName :
            self.libName = libName
            # If a no new libName is provided, the asset library will simply refresh

        self.waits = {}
        file = open("RobotModules/LeagueOps/Libraries/Assets/" + \
            self.libName + "/waits.csv", "r")

        for line in file.readlines():
            if line.lstrip()[0] != "#" :        # Ignore comments (& titles)
                line = line.split(',')
                self.waits[line[0]] = int(line[1]) / 1000

        self.regions = {}
        file = open("RobotModules/LeagueOps/Libraries/Assets/" + \
            self.libName + "/regions.csv", "r")

        for line in file.readlines():
            if line.lstrip()[0] != "#" :        # Ignore comments (& titles)
                line = line.split(',')
                self.regions[line[0]] = (
                    int(line[1]),
                    int(line[2]),
                    int(line[3]) - int(line[1]),
                    int(line[4]) - int(line[2]))

        self.positions = {}
        file = open("RobotModules/LeagueOps/Libraries/Assets/" + \
            self.libName + "/positions.csv", "r")

        for line in file.readlines():
            if line.lstrip()[0] != "#" :        # Ignore comments (& titles)
                line = line.split(',')
                self.positions[line[0]] = (int(line[1]), int(line[2]))

    def setImgConfidence(self, imgConfidence = 0.9):
        """ Define the image confidence for comparison in OpenCV
        """

        self.imgConfidence = imgConfidence
