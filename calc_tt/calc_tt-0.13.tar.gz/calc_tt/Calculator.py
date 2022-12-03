
import typing
from math import pow
'''
* Adding
* Subtracting
* Multiplication
* Division
* n-th root
'''

class Calculator:
    'Calculator that is able to do adding, subtraction, division, multiplication, root'
    def __init__(self):
        self.memory = '0 '
        self.counter = 0
        self.actions = dict([('clear','c'),('add','+'),('subtract','-'),('divide','/'),('multiply','*'),('root','pow')])

    def intro(self, filtered = False):
        'Prints user action options'
        intro_string = ''
        for item in self.actions.keys():
            #if (self.counter == 0 and item == 'divide') or (self.counter == 0 and item == 'multiply'): continue
            if filtered and item == 'root': continue
            intro_string += f'[{item[0]}]{item[1:]} '
        print(intro_string)

    def isfloat(self, num):
        'Checks if a number is float'
        try:
            float(num)
            return True
        except ValueError:
            return False

    def add(self, number: float):
        'Adds a number with addition action to memory'
        self.memory = self.memory + f' + {number}'

    def subtract(self, number: float):
        'Adds a number with subtraction action to memory'
        self.memory = self.memory + f' - {number}'

    def divide(self, number: float):
        'Adds a number with division action to memory'
        #if int(number) == 0: return False
        self.memory = self.memory + f' / {number}'

    def multiply(self, number: float):
        'Adds a number with multiplication action to memory'
        self.memory = self.memory + f' * {number}'

    def root(self, number: float, n: int, test: bool = False) -> float:
        'Gets n-th root of number'
        if test:
            n = 3
            action_local = '*'
        else:
            self.intro()
            action_local = input(f'Action for {n}-th root: ')

        if action_local.startswith('a'):
            action_local = '+'
        elif action_local.startswith('s'):
            action_local = '-'
        elif action_local.startswith('d'):
            action_local = '/'
        elif action_local.startswith('m'):
            action_local = '*'
        self.memory += f' {action_local} pow({number},1/{n})'
        return eval(f'pow({number},1/{n})')

    def clear(self):
        'Clears the calculator memory'
        self.memory = '0 '
        self.counter = 0

    def compute(self):
        'Gets result of current arithmetic actions in memory'
        return eval(self.memory)

    def accept_input(self, string: str):
        'Performs functions by user input'
        string = string.lower()
        if string.startswith('c'):
            self.memory = ''
        elif string.startswith('a'):
            number = float(input('+'))
            if not self.isfloat(number): return False
            self.add(number)
        elif string.startswith('s'):
            number = input('-')
            if not self.isfloat(number): return False
            self.subtract(number)
        elif string.startswith('d'):
            #if self.counter == 0: return False
            number = input('/')
            if not self.isfloat(number): return False
            print(number)
            #if int(number) == 0:
                #print('You cannot divide by zero!')
                #return False
            self.divide(number)
        elif string.startswith('m'):
            #if self.counter == 0: return False
            number = input('*')
            if not self.isfloat(number): return False
            self.multiply(number)
        elif string.startswith('r'):
            number = input('root of ')
            if not self.isfloat(number): return False
            power = input('n-th root, n is ')
            if not self.isfloat(number): return False
            self.intro(filtered=True)
            action_local = input(f'Action for {power}-th root: ')
            if action_local.startswith('a'): action_local = '+'
            elif action_local.startswith('s'): action_local = '-'
            elif action_local.startswith('d'): action_local = '/'
            elif action_local.startswith('m'): action_local = '*'
            else:
                print('Cannot divide or multiply as we only have one number!')
                return False
            self.memory += f' {action_local} pow({number},1/{power})'
        else:
            return False

        self.counter += 1
        if not self.memory == '': print(f'mem: {self.memory} = {eval(self.memory)}')




    def run(self):
        'Runs the calculator'
        while self.counter < 6:
            self.intro()
            query = input('Enter action: ')
            self.accept_input(query)
        print(f'Result: {eval(self.memory)}')



if __name__ == '__main__':
    instance = Calculator()
    instance.run()


