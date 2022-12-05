import sys
from time import sleep
    
def Type(Message):
    for char in Message:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    input()
def TypeT(Message, Time):
    for char in Message:
            sleep(Time)
            sys.stdout.write(char)
            sys.stdout.flush()
    input()