# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:19:01 2022

@author: DeivydasPagojus
"""

# functions - ad/substract, multiply / divide, sqrt, memory, clean to 0
from math import pow


class DPcalc:
    def __init__(self) -> None:
        self.result = 0

    def add(self, x: int):
        self.result += x
        return self.result

    def substract(self, x: int):
        self.result -= x
        return self.result

    def multiply(self, x: int):
        self.result *= x
        return self.result

    def divide(self, x: int):
        if x != 0:
            self.result /= x
        else:
            print('Division by 0 is not allowed')
        return self.result

    def nroot(self, x: int):
        if self.result > 0:
            self.result = pow(self.result, float(1)/x)
        elif self.result < 0:
            self.result = -pow(abs(self.result), float(1)/x)
        return self.result


calculator = DPcalc()
math_functions = {'+': 'add', '-': 'substract', '*': 'multiply',
                  '/': 'divide', 'r': 'nroot', 'x': 'memory reset'}

print("We have a 0. What do you want to do with it?")

while True:
    symbols = "+, -, *, /,r (for root),x (for memory recet), e (for exit)"
    operator = str(input("Select math function: " + symbols))

    if operator == 'e':
        break

    elif operator == 'x':
        result = 0
        print('===================================================')
        print("We have a 0. What do you want to do with it?")

    elif operator in math_functions:
        try:
            x = int(input("Enter a number / or root n: "))
            operation = getattr(calculator, math_functions[operator])
            result = operation(x)

            print('===================================================')
            print(f"We have a {result}. What do you want to do with it?")

        except:
            print('Math operations can only be performed with numbers')

    else: 
        print("Incorect math operator")
