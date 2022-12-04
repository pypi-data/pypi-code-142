from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator
from operation import Operation
from utils import parse_to_number

def main():
    questions = [
        {
            "type": "number", 
            "message": "Input the first number:", 
            "float_allowed": True,
            "validate": EmptyInputValidator()
        },
        {
            "type": "number", 
            "message": "Input the second number:", 
            "float_allowed": True,
            "validate": EmptyInputValidator()
        },
        {
            "type": "list",
            "message": "Choose the operation:",
            "choices": [
                "Addition", "Subtraction", "Multiplication", "Division"
            ],
        },
    ]
    
    result = prompt(questions)
    first_number = parse_to_number(result[0])
    second_number = parse_to_number(result[1])
    ops = Operation(first_number, second_number)
    
    if result[2] == 'Addition':
        print(ops.addition())
    elif result[2] == 'Subtraction':
        print(ops.subtraction())
    elif result[2] == 'Multiplication':
        print(ops.multiplication())
    else:
        print(ops.division())
    
    
if __name__ == "__main__":
    main()