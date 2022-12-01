
class Calculator:
    def __init__(self, initial_input: float=0, isReset: bool=True) -> None:
        """
            A simple calculator class that can:
            - add/ subtract
            - multiply/ divide
            - find the root of a number
            - reset the result to 0
            
            :param initial_input: initial input to the calculator
            :param isReset: True if the calculator is reset
        """
        self.result = initial_input
        self.isReset = isReset

    def add(self, num: float) -> float:
        """
            Add a number to the result
            :param num: number to add
        """ 
        self.result += num
        return self.result

    def subtract(self, num: float) -> float:
        """
            Subtract a number from the result
            :param num: number to subtract
        """ 
        self.result -= num
        return self.result

    def multiply(self, num: float) -> float:
        """
            Multiply the result by a number
            :param num: number to multiply by
        """ 
        self.result *= num
        return self.result

    def divide(self, num: float) -> float:
        """
            Divide the result by a number
            :param num: number to divide by
        """ 
        if num == 0:
            raise ZeroDivisionError
        self.result /= num
        return self.result

    def root(self, num: float, root: float) -> float:
        """
            Find the root of a number   
            :param num: number to find the root of
            :param root: root to find
        """ 
        self.result = num ** (1 / root)
        return self.result

    def reset(self) -> int:
        self.result = 0
        self.isReset = True
        return self.result


# calculator = Calculator()

# print('=============== Calculator ===============')
# print('Choose one of the following options:')
# print('1. Add')
# print('2. Subtract')
# print('3. Multiply')
# print('4. Divide')
# print('5. Root')
# print('6. Reset')
# print('7. Exit')

# while True:
#     # if the calculator is reset, the initial input is 0
#     # user should be prompted to enter an initial input
#     if calculator.isReset:
#         initial_input = input('Initial input: ')
#         calculator = Calculator(int(initial_input), False)

#     option = int(input('Enter your option: '))

#     if option == 1:
#         num = int(input('Enter the number to add: '))
#         print(f'{calculator.result} + {num} = {calculator.add(num)}')

#     elif option == 2:
#         num = int(input('Enter the number to subtract: '))
#         print(f'{calculator.result} - {num} = {calculator.subtract(num)}')

#     elif option == 3:
#         num = int(input('Enter the number to multiply: '))
#         print(f'{calculator.result} * {num} = {calculator.multiply(num)}')

#     elif option == 4:
#         num = int(input('Enter the number to divide: '))
#         print(f'{calculator.result} / {num} = {calculator.divide(num)}')

#     elif option == 5:
#         num = int(input('Enter the number to root: '))
#         root = int(input('Enter the root: '))
#         print(f'{num} root {root} = {calculator.root(num, root)}')

#     elif option == 6:
#         print(f'{calculator.result} reset to {calculator.reset()}')

#     elif option == 7:
#         print('Exiting...')
#         break

#     else:
#         print('Invalid option. Try again.')

#     print()



