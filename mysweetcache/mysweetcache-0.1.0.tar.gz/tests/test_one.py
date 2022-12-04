import numpy as np
from mySweetCache import cache, use_par

def test_one():
    name = "test_one"
    a = np.random.random((4,5))
    @cache(name)
    # @use_par(a)
    def identical(x):
        return x
    @cache(name)
    # @use_par(a)
    def get_none(x):
        return None
    b = identical(a, use_cache = False)
    c = get_none(a)
    assert np.all(c==a)
    assert np.all(b==a)