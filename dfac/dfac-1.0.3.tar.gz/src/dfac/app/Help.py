import sys

class Help:

    help_string ='''
    Usage: dfac.py [OPTION...] [OUTPUT]...
Datafactory generates random string of data for testing and other purposes.

Examples:
    dfac.py -t a -v n
    dfac.py -t s -v u -x

DESCRIPTION

OPTIONS
-t, --datatype
Option for the data type to be generated. Below are the available datatypes.

    Data Types
        s, string 
            print out string as data type
        a, array 
            print out array as data type 


-v, --valuetype
Option for the type of value to be generated. Below are the available value type options.
    
    Value Types
        For String data type
            n, alphanumeric 
                print out string containing random values of latin alphabet and numbers
            a, alphabet
                print out random string alphabet in a mix of uppercase and lowercase.
            u, upper
                print out random string of alphabet in uppercase.
            l, lower
                print out random string of alphabet in lowercase.
            y, alphasymbolic
                print out random mix of alphabet and symbols.
    
        For Array data type
            n, alphanumeric
                print out array containing strings with random alphabets and numbers.
            a, alphabet
                print out array containing strings with random alphabets uppercase and lowercase.
            u, upper
                print out array containing strings with random alphabets uppercase.
            l, lower
                print out array containing strings with random alphabets containing lowercase.
            y, alphasymbolic
                print out array containing strings with random alphabets and symbols.
            i, integer
                print out array containing strings with random integer.
            d, decimal
                print out array containing strings with random decimal numbers.
            o, symbolic
                print out array containing string with random symbols.

-0, --length
Option to print out length of string or array.

-L, --low
(For Array types) Option to set minimum length of value.

-H, --high
(For Array types) Option to set maximum length of value.

-x, --file
Print out generated value to file, if no name is provided output.txt is used.

-h, --help
Print this help text.
    '''
    def noValue(self):
        print("Usage: 'main.py --help' for more information")
        sys.exit()
    
    def printHelp(self):
        print(self.help_string)
        sys.exit()