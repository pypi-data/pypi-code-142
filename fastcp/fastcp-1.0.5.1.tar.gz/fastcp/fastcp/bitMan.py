"""
    Most of the functions in this module are implemented at O(logN) Time Complexity;
    This Module Contains multiple methods to tackle with bit Manipulation problems.
"""

import math as _math


def Binary(value) -> str:
    """
    Args:
        value (int): Enter a value to get binary of that value
    Returns:
        str: returns binary as string
    Complexity: O(Log N)
    """
    return bin(value)[2:];

def Hexa(value) -> str:
    """
    Args:
        value (int): Enter a value to get hexadecimal of that value
    Returns:
        str: returns hexadecimal as string
    Complexity: O(Log N)
    """
    return hex(value)[2:];

def Octal(value) -> str:
    """
    Args:
        value (int): Enter a value to get octadecimal of that value
    Returns:
        str: returns octadecimal as string
    Complexity: O(Log N)
    """
    return oct(value)[2:];

def Toggle(value):
    """
    Args:
        value (int): a number to toggle bits
    Returns:
        _int_: returns the number after toggling it's bits
    Complexity: O(Log N)
    """
    power = 2**(int(_math.log2(value)) + 1) - 1;
    return value ^ power;

def CountSetBits(value) -> int:
    """
    Args:
        value (int): a number to count the set bits

    Returns:
        int: returns set bit count of number
    Complexity: O(Log N)
    """
    count = 0;
    while(value): 
        if value & 1: count += 1;
        value >>= 1;
    return count;
        
def BinToDecimal(binary) -> int:
    """A function to convert binary to decimal

    Args:
        binary (int/string): input binary

    Returns:
        int: returns decimal value of binary
    Complexity: O(Log N)
    """
    binary = str(binary);
    return int(binary, 2);

def OctToDecimal(octal) -> int:
    """A function to convert octal to decimal
    Args:
        octal (int/string): input binary
    Returns:
        int: returns decimal value of octal
    Complexity: O(Log N)
    """
    octal = str(octal);
    return int(octal, 2);

def HexToDecimal(hexadecimal) -> int:
    """A function to convert hexadecimal to decimal
    Args:
        hexadecimal (int/string): input hexadecimal
    Returns:
        int: returns decimal value of hexadecimal
    Complexity: O(Log N)
    """
    hexadecimal = str(hexadecimal);
    return int(hexadecimal, 16);



