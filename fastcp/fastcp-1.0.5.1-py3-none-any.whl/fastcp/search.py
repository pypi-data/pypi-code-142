import bisect as _bisect;

def Find(array, size, value):
    """
    A method to find the index of a value in array at O(LogN) Complexity
    Args:
        array (list): Array to search element
        size (int): Size of Array
        value (int): Value to Search for
    Returns:
        int: Returns index of value if value is found else returns -1
    """
    if (value in array):
        return _bisect.bisect_left(array, value, 0, size);
    return -1;

def UpperBound(array, size, value):
    """
    A method to find the possible index to insert value into the array to maintain Sorted Order
    at O(LogN) Complexity (returns highest possible Index
    Args:
        array (list): Array to search element
        size (int): Size of Array_
        value (int): Value to Search for
    Returns:
        int: Returns index of value if value is found else returns -1
    """
    return _bisect.bisect_right(array, value, 0, size);

def LowerBound(array, size, value):
    """
    A method to find the possible index to insert value into the array to maintain Sorted Order
    at O(LogN) Complexity (returns least possible Index)
    Args:
        array (list): Array to search element
        size (int): Size of Array
        value (int): Value to Search for
    Returns:
        int: Returns index of value if value is found else returns -1
    """
    return _bisect.bisect_left(array, value, 0, size);


    