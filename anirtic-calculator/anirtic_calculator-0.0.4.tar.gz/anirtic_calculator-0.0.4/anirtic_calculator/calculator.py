class Calculator:
    """
    A class to perform basic calculator operations

    ...

    Attributes
    ----------
    memory : float
        Calculator memory

    Methods
    ----------
    add(number):
        Takes the number and adds it to calculator memory
    subtract(number):
        Takes the number and subtracts it from calculator memory
    multiply(number):
        Multiplies calculator memory by a given number
    divide(number):
        Divides calculator memory by a given number
    root(number):
        Takes the n root of calculator memory
    reset():
        Resets calculator memory
    """
    memory = 0.0

    @classmethod
    def add(cls, number=float) -> float:
        """Takes the number and adds it to calculator memory

            For example:

            >>> Calculator.memory = 0.0
            >>> Calculator.add(2.1)
            2.1
        """
        cls.memory += number
        return cls.memory

    @classmethod
    def subtract(cls, number=float) -> float:
        """Takes the number and subtracts it from calculator memory

            For example:

            >>> Calculator.memory = 9.0
            >>> Calculator.subtract(2)
            7.0
        """
        cls.memory -= number
        return cls.memory

    @classmethod
    def multiply(cls, number=float) -> float:
        """Multiplies calculator memory by a given number
            For example:

            >>> Calculator.memory = 9.0
            >>> Calculator.multiply(2)
            18.0

        """
        cls.memory *= number
        return cls.memory

    @classmethod
    def divide(cls, number=float) -> float:
        """Divides calculator memory by a given number

            For example:

            >>> Calculator.memory = 9
            >>> Calculator.divide(2)
            4.5
        """
        if number == 0:
            print("Can't divide by 0")
            return cls.memory
        else:
            cls.memory /= number
            return cls.memory

    @classmethod
    def root(cls, n: float) -> float:
        """Takes the n root of calculator memory

            For example:

            >>> Calculator.memory = 9
            >>> Calculator.root(2)
            3.0
        """

        if cls.memory < 0:
            # Checks if we are not taking a root of negative number
            print("Can't take a root of negative number")
            return cls.memory
        else:
            try:
                cls.memory = cls.memory ** (1/n)  # (1/n) or (1 / n)
            except OverflowError:
                print("Result is too large")
                return cls.memory

        return cls.memory

    @classmethod
    def reset(cls) -> float:
        """Resets calculator memory

            For example:

            >>> Calculator.memory = 285
            >>> Calculator.reset()
            0.0
        """
        cls.memory = 0.0
        return cls.memory


if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
