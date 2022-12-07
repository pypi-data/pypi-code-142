class PowerOf2:
    
    
    def __init__(self, number):
        self.number = number

    def isPowerOf2(self):
        """
        Check if a number is power of 2

        :param number: The number to check if it is power of 2.
        :type number: int

        """
        if self.number != 0 and (self.number & (self.number-1)) == 0:
            return True
        else:
            return False

