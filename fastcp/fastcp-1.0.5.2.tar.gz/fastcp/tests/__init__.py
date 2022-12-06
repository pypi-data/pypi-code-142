from easycp import __version__
from easycp import math
from easycp import strings
from easycp import arrays
__version__ = "1.0.0"

def test_math():
    assert 3.0 == math.Cbrt(27);
    
def test_strings():
    assert 5 == strings.VowelCount("aeiou");

def test_arrays():
    assert 5 == arrays.Length([1,2,3,4,5]);