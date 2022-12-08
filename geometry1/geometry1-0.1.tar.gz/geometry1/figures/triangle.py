class Triangle:
    def __init__(self, point1, point2, point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    def perimeter(self):
        a = ((self.__point2.first_value - self.__point1.first_value) ** 2 +
             (self.__point2.second_value - self.__point1.second_value) ** 2) ** 0.5
        b = ((self.__point3.first_value - self.__point2.first_value) ** 2 +
             (self.__point3.second_value - self.__point2.second_value) ** 2) ** 0.5
        c = ((self.__point3.first_value - self.__point1.first_value) ** 2 +
             (self.__point3.second_value - self.__point1.second_value) ** 2) ** 0.5
        perimeter = a + b + c
        return round(perimeter, 4)

    def square(self):
        a = ((self.__point2.first_value - self.__point1.first_value) ** 2 +
             (self.__point2.second_value - self.__point1.second_value) ** 2) ** 0.5
        b = ((self.__point3.first_value - self.__point2.first_value) ** 2 +
             (self.__point3.second_value - self.__point2.second_value) ** 2) ** 0.5
        c = ((self.__point3.first_value - self.__point1.first_value) ** 2 +
             (self.__point3.second_value - self.__point1.second_value) ** 2) ** 0.5
        p = (a + b + c)/2
        s = (p * (p - a) * (p - b) * (p - c))**0.5
        return round(s, 4)

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

    @property
    def point3(self):
        return self.__point3

    @point3.setter
    def point3(self, point3):
        self.__point3 = point3
