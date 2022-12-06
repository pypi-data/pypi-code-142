from collections import *;


def info():
    """
    Description:

        Functions in this Library:
        - Multimap (unique to fastcp package)
        - defaultdict
        - OrderedDict
        - namedtuple
        - deque
        - ChainMap
        - Counter
        - UserDict
        - UserList
        - UserString
    """
    print("""
    Description:

        Functions in this Library:
        - Multimap (unique to fastcp package)
        - defaultdict
        - OrderedDict
        - namedtuple
        - deque
        - ChainMap
        - Counter
        - UserDict
        - UserList
        - UserString
    """)
    
    
def Multimap(default):
    """
    This Function returns a Multimap (i.e Multi-DefaultDict) 
    
    Args:
        default (Any): the default value of multi-map will depend on the Argument passed
        0 -> Default value is Int
        [] -> Default value is List
        () -> Default value is Tuple
        {} -> Default value is Dict 
        0.0 -> Default value is Float
        True -> Default value is Bool
        etc ...
    Returns:
        defaultdict : returns a Multi-DefaultDict with default value as passed as Argument
    Example:
        >>> dictionary = Multimap(1) # takes int as default value (any int can be passed as argument)
        >>> dictionary[1][0] 
        0
        >>> dictionary = Multimap([])
        >>> dictionary[0][0]
        []
    """
    return defaultdict(lambda: defaultdict(type(default)));

