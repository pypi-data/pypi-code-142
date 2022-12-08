class Point:
    def __init__(self, first_value, second_value):
        self.__first_value = first_value
        self.__second_value = second_value

    @property
    def first_value(self):
        return self.__first_value

    @first_value.setter
    def first_value(self, first_value):
        self.__first_value = first_value

    @property
    def second_value(self):
        return self.__second_value

    @second_value.setter
    def second_value(self, second_value):
        self.__second_value = second_value
