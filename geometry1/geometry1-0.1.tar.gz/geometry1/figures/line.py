class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def length(self):
        result = ((self.__point2.first_value - self.__point1.first_value) ** 2
                  + ((self.__point2.second_value - self.__point1.second_value ** 2) ** 0.5))
        return result

    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, point1):
        self.__point1 = point1

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, point2):
        self.__point2 = point2
