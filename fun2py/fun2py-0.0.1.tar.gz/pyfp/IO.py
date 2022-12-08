from .type import String,Numeral

def read_input(prompt:str):
    text = input(prompt)
    if text.isnumeric():
        return Numeral(float(text))
    else:
        return String(text)