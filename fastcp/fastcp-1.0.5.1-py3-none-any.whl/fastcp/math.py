def Sieve(value):
    """
    A function that generates sieve of erathosthenes till value
       Example: 
                >>> math.sieve(10)
                [0,0,1,1,0,1,0,1,0,0,0] 
                0 -> not prime and 1 -> prime
                
    Args:
        value (int): Number to generate sieve of erathosthenes
    Returns:
        List: returns a list of sieve of erathosthenes
    Complexity: O(N LogN)
    """
    prime = [1]*value;
    prime[0], prime[1] = 0, 0; i = 2;
    while(i*i <= value):
        if (prime[i]):
            for j in range(i*i, value, i):
                if (prime[j]): prime[j] = 0;
        i += 1;
    return prime;

def IsPrime(value):
    """
    Args:
        value (int): value to check whether prime or not
    Returns:
        bool: return True if prime else returns False
    Complexity: O(root N)
    """
    if (value <= 1): return False;
    if (value in (2,3,5,7)): return True;
    if (value <= 10): return False;
    for i in range(2, int(value**0.5)+1):
        if value % i == 0: return False;
    return True;

def Product(arr):
    """ A funtion that returns product of all elements of array
    Args:
        arr (List): Input array
    Returns:
        int: returns product of all elements of array, 0 if array is empty
    Complexity: O(N)
    """
    if (arr):
        i = 1; 
        for val in arr: i *= val;
        return i;
    return 0;

from math import *;