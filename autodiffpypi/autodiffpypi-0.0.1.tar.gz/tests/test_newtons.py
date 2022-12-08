from src.autodiffpypi.forward_mode import Forward
from src.autodiffpypi.dual_number import DualNumber
from src.autodiffpypi.base_derivatives import *
import src.autodiffpypi as adp
from applications.newtons import newton

def test_newton_full():
    """
    Test suite for the Newton class.
    """
    allowed_error = 0.0001

    def test_newton():
        # Test for success on good guess
        init_guess = 0.1
        f = lambda x : x - adp.exp(-2.0 * adp.sin(4.0 * x) * adp.sin(4.0 * x))
        res = newton.newton(f, init_guess, 10000)
        assert abs(res - 2.473481e-01) <= allowed_error

        # Test for failure on bad guess
        init_guess = 10
        f = lambda x : x - adp.exp(-2.0 * adp.sin(4.0 * x) * adp.sin(4.0 * x))
        res = newton.newton(f, init_guess, 100)
        assert abs(res - 2.473481e-01) > allowed_error

        # Test for success on good guess
        init_guess = 1
        f = lambda x : x - adp.cos(x)
        res = newton.newton(f, init_guess, 1000)
        assert abs(res - 0.7390851332151606416553) <= allowed_error

        # Test for failure on bad guess
        init_guess = 500
        f = lambda x : x - adp.cos(x)
        res = newton.newton(f, init_guess, 200)
        assert abs(res - 0.7390851332151606416553) > allowed_error
        
    test_newton()


test_newton_full()
