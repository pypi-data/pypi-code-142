""" PyAutoGui (PAG) Wrapper Module
"""

class PAGObject :
    """ PyAutoGui Wrapper Object
    """

    originX = 0
    originY = 0
    sizeX = 1
    sizeY = 1

    def __init__(self, originX = 0, originY = 0, sizeX = 1920, sizeY = 1080):
        self.setFrame(int(originX), int(originY), int(sizeX), int(sizeY))

    def setFrame(self, originX, originY, sizeX, sizeY):
        """ Will set the frame within which PAG will operate
        """

        self.originX = int(originX)
        self.originY = int(originY)
        self.sizeX = int(sizeX)
        self.sizeY = int(sizeY)

    def setDefaultFrame(self):
        """ Set the default frame to Full HD
        """

        self.setFrame(0, 0, 1920, 1080)
