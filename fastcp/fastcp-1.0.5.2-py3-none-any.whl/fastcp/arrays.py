from collections import Counter as _Counter
from collections import *;
from typing import List as _List

def Length(arr :_List) -> int:
    """
    Args:
        arr (List): input array
    Returns:
        int: returns length of array
        Complexity: O(N)
    """
    return len(arr);

def Unique(arr :_List) -> int:
    """
    Args:
        arr (List): input array
    Returns:
        List: returns a list of unique elements
        Complexity: O(N)
    """
    return list(set(arr))

def Freq(arr :_List) -> dict:
    """
    Args:
        arr (List): input array
    Returns:
        dict: returns a dict containing frequency of each element of array
        Complexity: O(N)
    """
    return dict(_Counter(arr));

def Subseq(arr :_List) -> _List[_List]:
    """A function to generate subsequences of array

    Args:
        arr (List): Input Array

    Returns:
        List[List]: returns a 2D list containing Subsequences
        Complexity: O(2**N)
    """
    def traverse(arr, i, n, seq, ref):
        if (i == n):
            seq.append(ref[:]); return;        
        ref.append(arr[i]);
        traverse(arr, i+1, n, seq, ref);
        ref.pop();
        traverse(arr, i+1, n, seq, ref);       
    seq = []; ref = [];
    traverse(arr, 0, len(arr), seq, ref); del ref;
    return seq;

def Subarr(arr):
    """A functions to get subarrays of arr
    Args:
        arr (List - int/str): input arr to get subarrays
    Returns:
        List[List]: returns an List containing all subarrays
        Complexity: O(N*N)
    """
    substr = []; n = len(arr);
    for i in range(n):
        ref = []
        for j in range(i, n):
            ref.append(arr[j]);
            substr.append(ref[:]);
    del ref;
    return substr;
