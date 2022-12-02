# BUG
class Equation:
    """It must be 5 characters long with one operation and all numbers and operators or names of items stored to its
    'storage unit'. Operators must have spaces around them. You can only access ones that have key that is one letter
    long. Any stored value that is going to be used in an equation must be in the form 'int'. You can change values
    using the change command, passing in the name and new value. Recognized operators that meet the length requirement:
     %, *, -, +, /, ^ (NOT EXPONENTS) You might get an error if you pass in and un-evaluated equation, so you shouldn't
     do that unless you are sure that it works that way

    --------
    Scientific Notation and More
    Package: ScientificNotationAndMore
    --------
    Module: ScientificNotationAndMore.equations
    --------
    """

    class UnknownOperatorError(Exception):
        pass

    # Creates function to raise an UnknownOperatorError
    def raise_unknown_operator_error(self, operator):
        raise self.UnknownOperatorError("The package: ScientificNotationAndMore, does not recognize this operator '" +
                                        str(operator) + "'")

    def __init__(self, string):
        # Creates UnknownOperatorError

        # Creates SpacingError
        class SpacingError(Exception):
            pass

        # Creates function to raise a SpacingError
        def spacing_error():
            raise SpacingError("There is an error in your spacing")

        # Creates LengthError
        class LengthError(Exception):
            pass

        # Creates function to raise a LengthError
        def length_error(x):
            raise LengthError("The string is too " + x)

        # Checks to see if the string is the correct length

        if len(string) > 5:
            length_error("long")
        if len(string) < 5:
            length_error("short")

        # Checks to see if the spacing is correct

        space = 0
        if list(string)[1] != " " or list(string)[3] != " ":
            spacing_error()
        self._equation = string
        # Finds the operator used, and if it is unknown raises a  UnknownOperatorError

    # Storage
    class Unit:
        unit = {}
        storage_list = []

    # Puts a value in the storage dictionary
    def assign(self, name, value):
        self.Unit.unit[name] = value

    # Gets a value
    def access(self, item):
        return self.Unit.unit[item]

    # Store a value in the storage list
    def store_in_list(self, item):
        self.Unit.storage_list.append(item)

    # Find a value in the storage list and return it
    def get(self, index):
        return self.Unit.storage_list[index]

    # Delete an item in the storage list
    def delete(self, index):
        del self.Unit.storage_list[index]

    # Stores a value from the storage list in the storage unit dictionary
    def store_in_unit(self, index, name_in_unit):
        self.Unit.unit[name_in_unit] = self.Unit.storage_list[index]

    # Gets the storage list and returns it
    def get_storage_list(self):
        return self.Unit.storage_list

    # Transfers an item from the storage list to the storage unit dictionary
    def transfer(self, index, name):
        self.Unit.unit[name] = self.Unit.storage_list[index]
        del self.Unit.storage_list[index]

    # Changes a value in the storage unit dictionary
    def change(self, name, new_value):
        self.Unit.unit[name] = new_value

    # Checks to see if it is an integer
    def is_int(self, number):
        try:
            number = int(number)
        except ValueError:
            return False
        except TypeError:
            return False
        else:
            return True

    # Finds the answer to the problem and returns it
    def evaluate(self):
        # Gets the operator that was used
        operator = list(self._equation)[2]
        # Determines if the first value 'list(self._equation)[0]'is a number or a key for the storage unit
        if self.is_int(list(self._equation)[0]):
            # Gets the value of the first number IF it is a integer
            a = int(list(self._equation)[0])
        else:
            # Checks to see if it has a key
            try:
                # Gets it if it has a key
                a = self.access(list(self._equation)[0])
            # Handles the exception for KeyError
            except KeyError:
                # Gets the first element of the string
                a = list(self._equation)[0]
            # Checks to see if it is an equation or number being stored
            if self.is_int(a):
                # Keeps the first value the same if it is a number
                a = a
            else:
                # Gets the answer to the equation
                a = a.evaluate()
        # Determines if the second number/expression 'list(self._equation)[4]'is a number or a key for the storage unit
        if self.is_int(list(self._equation)[4]):
            # Gets it and converts to a number IF it is a number
            b = int(list(self._equation)[4])
        # Applies the rules for equations/numbers in the dictionary to it if it is an equation
        else:
            try:
                # Checks to see if it is an equation and is stored in the dictionary
                b = self.access(list(self._equation)[4])
            # If it is not in the dictionary converts it to an integer
            except KeyError:
                b = list(self._equation)[4]
            # Checks to see if it doesn't need to be evaluated
            if self.is_int(b):
                # IF it is here it doesn't need to be evaluated
                b = b
            else:
                # IF it is here it gets evaluated
                b = b.evaluate()

        # Figures out which operator is being used.
        if operator == "%":
            # Modulus
            return a % b
        elif operator == "*":
            # TIMES
            return a * b
        elif operator == "-":
            # Minus
            return a - b
        elif operator == "+":
            # Plus
            return a + b
        elif operator == "/":
            # Divided by
            return a / b
        elif operator == "^":
            return a ^ b
        else:
            # Unknown operator
            self.raise_unknown_operator_error(operator)

    # Returns the equation
    def return_equation(self):
        return self._equation
