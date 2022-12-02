
import random
import numpy as np

def print1():
    num = 1
    print(f'You have {num}')

def printArray1(size):
    print(np.ones(size))

def printRandInt(start, end):
    num = random.randint(start, end)
    print(f'You have {num}')
