from collections import Counter as _Counter
from itertools import combinations as _combinations;
from itertools import permutations as _permutations;


def Freq(string):
    """A functions to get frequency of each character of string
    Args:
        string (str): _input string to get frequency
    Returns:
        dict: returns the dict of frequency of each character in string
        Complexity: O(N)
    """
    string = [i for i in string]
    return dict(_Counter(string));

def VowelCount(string):
    """A functions to count number of vowels in string
    Args:
        string (str): input string to get count of vowels
    Returns:
        int: returns the count of vowels in string
        Complexity: O(N)
    """
    vowel = ['a', 'e', 'i', 'o', 'u'];
    string = "".join([i for i in string]);
    string = string.lower(); count = 0;
    for i in string:
        if (i in vowel): count += 1;
    del vowel;
    return count;

def Substr(string):
    """A functions to get substrings of string
    Args:
        string (str): input string to get substring
    Returns:
        List: returns an List containing all substrings
        Complexity: O(N*N)
    """
    string = "".join([i for i in string]); substr = []; n = len(string);
    for i in range(n):
        ref = ''
        for j in range(i, n):
            ref += string[j];
            substr.append(ref);
    del ref;
    return substr;

def Subseq(string):
    """A function to get all subsequences of string

    Args:
        string (str): A string to get subsequences

    Returns:
        List: retuns a List containing all the subsequences of string
        Complexity: O(2**N)
    """
    string = "".join([str(i) for i in string])
    n = len(string); seq = []; ref = []
    def recur(string, n, i, seq, ref):
        if (i >= n): 
            seq.append("".join(ref)); return;
        ref.append(string[i]);
        recur(string, n, i+1, seq, ref);
        ref.pop();
        recur(string, n, i+1, seq, ref);
    recur(string, n, 0, seq, ref); del ref;
    return seq;

        
    
        