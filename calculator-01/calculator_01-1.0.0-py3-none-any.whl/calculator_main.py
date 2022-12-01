""" Create program Calculator. Class Calculator performs these actions:
Addition / Subtraction.
Multiplication / Division.
Take (n) root of a number.
Reset memory (Calculator has its own memory, meaning it manipulates its starting number 0 until it is reset.)."""

# result stores the answers of the arithmetic operations until the program is stopped or reset.
# If one number is given program makes calculations based on previous result. If both numbers are given -
# the result memory resets.


class Calculator:
    result = float(0)

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def addition(self):
        """ Adding two numbers. If values are empty - calculation result is zero. """
        try:
            if self.num_1 == '':
                self.num_1 = 0
                print(f'{Calculator.result} + {self.num_2} = {(Calculator.result + float(self.num_2)):.2f}')
                Calculator.result = (Calculator.result + float(self.num_2))
                return Calculator.result
            elif self.num_2 == '':
                self.num_2 = 0
                print(f'{self.num_1} + {Calculator.result} = {(float(self.num_1) + Calculator.result):.2f}')
                Calculator.result = float(self.num_1) + Calculator.result
                return Calculator.result
            else:
                Calculator.result = (float(self.num_1) + float(self.num_2))
                print(f'{self.num_1} + {self.num_2} = {Calculator.result:.2f}')
                return Calculator.result
        except ValueError:
            print('Give me a number, not a word. A decimal number is separated by a dot, not a comma.')

    def subtraction(self):
        """subtracting two numbers, for empy values - default number is 0."""
        try:
            if self.num_1 == '':
                self.num_1 = 0
                print(f'{Calculator.result} - {float(self.num_2)} = {(Calculator.result - float(self.num_2)):.2f}')
                Calculator.result = (Calculator.result - float(self.num_2))
                return Calculator.result
            elif self.num_2 == '':
                self.num_2 = 0
                print(f'{Calculator.result} - {self.num_1} = {(Calculator.result - float(self.num_1)):.2f}')
                Calculator.result = (Calculator.result - float(self.num_1))
                return Calculator.result
            else:
                Calculator.result = float(self.num_1) - float(self.num_2)
                print(f'{self.num_1} - {self.num_2} = {Calculator.result:.2f}')
                return Calculator.result
        except ValueError:
            print('Give me a number, not a word. A decimal number is separated by a dot, not a comma.')

    def multiply(self):
        """ Multiply two numbers, for empy values - default number is 1. """
        try:
            if self.num_1 == '':
                self.num_1 = 1
                print(f'{Calculator.result} * {self.num_2} = {(Calculator.result * float(self.num_2)):.2f}')
                Calculator.result = Calculator.result * float(self.num_2)
                return Calculator.result
            elif self.num_2 == '':
                self.num_2 = 1
                print(f'{Calculator.result} * {self.num_1} = {(Calculator.result * float(self.num_1)):.2f}')
                Calculator.result = Calculator.result * float(self.num_1)
                return Calculator.result
            else:
                Calculator.result = float(self.num_1) * float(self.num_2)
                print(f'{self.num_1} * {self.num_2} = {Calculator.result:.2f}')
                return Calculator.result
        except ValueError:
            print('Give me a number, not a word. A decimal number is separated by a dot, not a comma.')

    def division(self):
        """ Function to devide two numbers, for empy values - default number is 1. """
        try:
            if self.num_1 == '':
                self.num_1 = 1
                print(f'{Calculator.result} / {self.num_2} = {(Calculator.result / float(self.num_2)):.2f}')
                Calculator.result = Calculator.result / float(self.num_2)
                return Calculator.result
            elif self.num_2 == '':
                self.num_2 = 1
                print(f'{Calculator.result} / {self.num_1} = {(Calculator.result / float(self.num_1)):.2f}')
                Calculator.result = Calculator.result / float(self.num_1)
                return Calculator.result
            else:
                Calculator.result = float(self.num_1) / float(self.num_2)
                print(f'{self.num_1} / {self.num_2} = {Calculator.result:.2f}')
                return Calculator.result
        except ZeroDivisionError:
            print("Zerro division is impossible")
        except ValueError:
            print('Give me a number, not a word. A decimal number is separated by a dot, not a comma.')

    def root(self):
        """ Take (n) root of a number. First number is (n), if it is < 0 calculate absolute value.
        The root of a negative number will always be a positive number. """
        try:
            if self.num_1 == '':
                self.num_1 = 1
                print(f'{self.num_2}th root of number {Calculator.result} is'
                      f' {(Calculator.result ** (1.0 / abs(int(self.num_2)))):.2f}')
                Calculator.result = Calculator.result ** (1.0 / abs(int(self.num_2)))
                return Calculator.result
            elif self.num_2 == '':
                self.num_2 = 1
                print(f'{self.num_1}th root of number {Calculator.result} is '
                      f'{(Calculator.result ** (1.0 / abs(int(self.num_1)))):.2f}')
                Calculator.result = Calculator.result ** (1.0 / abs(int(self.num_1)))
                return Calculator.result
            elif int(self.num_1) < 0:
                self.num_1 = abs(int(self.num_1))
                Calculator.result = abs(float(self.num_2)) ** (1.0 / abs(int(self.num_1)))
                print(f'The {self.num_1}th root of number {self.num_2} is {Calculator.result:.2f}')
                return Calculator.result
            else:
                Calculator.result = abs(float(self.num_2)) ** (1.0 / abs(int(self.num_1)))
                print(f'The {self.num_1}th root of number {self.num_2} is {Calculator.result:.2f}')
                return Calculator.result
        except ValueError:
            print('First number must be integer')
        except ZeroDivisionError:
            print("Zerro division is impossible")

    # function is static, only ment for printing the options
    @staticmethod
    def options() -> None:
        print("Please select operation you would like to make:\n+. for addition;\n-. for subtraction;\n"
              "*. for multiplication;\n/. for division;\nroot. for taking (n) root of a number;\n"
              "stop. for reset the memory\n")
