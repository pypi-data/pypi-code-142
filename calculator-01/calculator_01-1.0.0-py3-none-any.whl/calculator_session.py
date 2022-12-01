from calculator_main import *

if __name__ == '__main__':
    # infinite loop. At any moment if print 'stop' program stops and prints out the result. If operation choice
    # is incorrect program makes new offer and continues with previous result:
    while True:
        Calculator.options()
        choice = input("Enter + or - or * or / or root or stop >> ")        # User input information
        if choice == 'stop':
            print(f'final result: {Calculator.result}')
            break
        num1 = input("Enter First number >> ")                               # User input information
        if num1 == 'stop':
            print(f'final result: {Calculator.result}')
            break
        elif num1 == '':
            num2 = input("Enter Second number >> ")                          # User input information
        else:
            num2 = input("Enter Second number >> ")                          # User input information
            if num2 == 'stop':
                print(f'final result: {Calculator.result}')
                break
        obj = Calculator(num1, num2)
        if choice == '+':
            obj.addition()
            continue
        if choice == '-':
            obj.subtraction()
            continue
        if choice == '*':
            obj.multiply()
            continue
        if choice == '/':
            obj.division()
            continue
        if choice == 'root':
            obj.root()
            continue
