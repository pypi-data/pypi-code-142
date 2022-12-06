"""
    This library contains the following functions:
    - SortDict
    - Sort
    - SortDictValues
"""


def SortDict(dictionary, boolean = False) -> dict:
    """
    A Function that returns a Sorted Dictionary
    Args:
        dictionary (dict): Input Dictionary to Sort
        boolean (bool): True for Decreasing Sort, False for Increasing Sort
                        False by Default
    Returns:
        dict : returns a Sorted Dictionary
        Complexity: O(N LogN)
    Example:
        >>> dict = {10: 1, 8: 2, 1: 3, 4: 4}
        >>> print(SortDict(dict))
        {1: 3, 4: 4, 8: 2, 10: 1}
        >>> print(SortDict(dict, True))
        {10: 1, 8: 2, 4: 4, 1: 3}
    """
    newdict = {}
    for key in sorted(dictionary):
        newdict[key] = dictionary[key];
    return newdict;

def SortDictValues(dictionary, boolean = False):
    """
    A Function Sorts Dictionary based on Values of Dictionary
    Args:
        dictionary (dict): Input Dictionary to Sort
        boolean (bool): True for Decreasing Sort, False for Increasing Sort
                        False by Default
    Returns:
        dict : returns a Sorted Dictionary based on Values of Dictionary
        Complexity: O(N LogN)
    Example:
        >>> dict = {10: 1, 8: 2, 1: 3, 4: 4}
        >>> print(SortDict(dict))
        {10: 1, 8: 2, 1: 3, 4: 4}
        >>> print(SortDict(dict, True))
        {4: 4, 1: 3, 8: 2, 10: 1}
    """
    array = list(dictionary.keys()); newdict = {};
    array.sort(key = lambda x: dictionary[x], reverse = boolean);
    for i in array:
        newdict[i] = dictionary[i];
    return newdict;


def Sort(array, boolean = False):
    """
        This Function returns a Sorted List at a Complexity of O(N)
        Restriction: Maximum size of element is 10**8;
        Error Handling: Returns Index Error if Maximum element in List is Greater than 10**8;
    Args:
        array (List): take a input list
        boolean (bool): True for Decreasing Sort, False for Increasing Sort
                        False is taken as default Value
    Returns:
        List: Returns a Sorted List
        Complexity: O(N)
        Example:
            >>> array = [9, 1, 2, -1, -9 , 0, -100000000, 100000000]
            >>> Sort(array)
            [-100000000, -9, -1, 0, 1, 2, 9, 100000000]
            >>> array = [100000001]
            >>> Sort(array)
            IndexError: highest element in list cannot exceed 10**8
    """
    default = 100000000;
    pos_sort = [0]*(default); neg_sort = [0]*(default);
    newarr = []; pos = 0; neg = 0; poscount = 0; negcount = 0;
    try:
        for i in array:
            if (i < 0):
                if (abs(i) ==  default):
                    negcount += 1;
                else:
                    neg_sort[abs(i)] += 1; neg += 1;
            else:
                if (i == default):
                    poscount += 1;
                else:
                    pos_sort[i] += 1; pos += 1;
        if (negcount):
            while(negcount > 0):
                newarr.append(-default); negcount -= 1;
        if (neg):
            for i in range(default):
                if (neg_sort[i]):
                    while(neg_sort[i]):
                        newarr.append(-i); neg_sort[i] -= 1;
        if (pos):
            for i in range(default):
                if (pos_sort[i]):
                    while(pos_sort[i]):
                        newarr.append(i); pos_sort[i] -= 1;
        if (poscount):
            while(poscount > 0):
                newarr.append(default); poscount -= 1;
        del neg_sort; del pos_sort; del neg; del pos; del default;
        if (boolean): newarr.reverse();
        return newarr;          
    except IndexError:
        print("IndexError: highest element in list cannot exceed 10**8")
        return array;
