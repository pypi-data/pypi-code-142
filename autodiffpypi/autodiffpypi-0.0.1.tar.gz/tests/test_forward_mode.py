import pytest

from src.autodiffpypi.forward_mode import Forward
from src.autodiffpypi.base_derivatives import *

def test_forward_mode():
    """
    Test suite for the Forward class, including 
    `evaluate`, `derivative`, and `jacobian`.
    """

    def test_init():
        x = 2
        f = 8 * x
        with pytest.raises(ValueError):
            Forward(f, 1)
            Forward([f, f], 1)


    def test_evaluate():
        x = 2
        f1 = lambda x: x**2 + sin(x)
        assert(Forward(f1, 1).evaluate(x) == 2**2 + sin(2))
        
        x = 2
        f = lambda x: 2 * x + x**3 - log(x)
        assert(Forward(f, 1).evaluate(x) == 2 * 2 + 2**3 - log(2))

        x = 2
        y = 3
        f1 = lambda x, y: x ** 2 + y
        f2 = lambda x, y: y**2 - x / y
        fwd = Forward([f1, f2], 2).evaluate(x, y)

        assert(fwd[0][0] == 7)
        assert(fwd[1][0] == 9 - 2/3)

        with pytest.raises(ValueError):
            Forward(f, 1).evaluate()
            Forward([f1, f2], 2).evaluate(x)


    def test_derivative():
        x = 2
        func = lambda x: 2 * x + x**3 - log(x)
        assert(Forward(func, 1).derivative(x) == 2 + 3 * 2**2 - 1 / 2)

        y = 2
        func = lambda y: (y)**(1/2) - sinh(y**2) - 14*exp(y)
        assert(Forward(func, 1).derivative(y) == 1/(2*np.sqrt(2)) - 14*exp(2) - 4*np.cosh(4))

        z = 2
        func = lambda z: z**2 + sin(z)
        assert(Forward(func, 1).derivative(z) == 2 * 2 + np.cos(2))

        x = 2
        y = 3
        f1 = lambda x, y: x ** 2 + y
        f2 = lambda x, y: log(y) - x / y
        der_x = Forward([f1, f2], 2).derivative(0, x, y)
        der_y = Forward([f1, f2], 2).derivative(1, x, y)
        assert(der_x[0] == 4)
        assert(der_x[1] == -1/3)
        assert(der_y[0] == 1)
        assert(der_y[1] == (2 + 3)/3**2)

        # missing variable
        with pytest.raises(TypeError):
            Forward(func, 1).derivative()

        # multiple inputs, single function
        x = 2
        w = 2
        f = lambda x, w: x * (w ** 2)
        assert(Forward(f, 2).derivative(0, x, w) == 4.)
        assert(Forward(f, 2).derivative(1, x, w) == 8.)

        # single input, multiple functions
        x = 2
        f = lambda x: log(x)
        f1 = lambda x: 3 * x ** 2
        assert(round(Forward([f, f1], 1).derivative(x)[0][0], 2) == 1/2)
        assert(round(Forward([f, f1], 1).derivative(x)[1][0], 2) == 12)


    def test_jacobian():
        x = 2
        f = lambda x: 2 * x + x**3 - log(x)
        assert(Forward(f, 1).jacobian(x) == [2 + 3 * 2**2 - 1 / 2])

        y = 2
        f = lambda y: (y)**(1/2) - sinh(y**2) - 14*exp(y)
        assert(Forward(f, 1).jacobian(y) == [1/(2*np.sqrt(2)) - 14*exp(2) - 4*np.cosh(4)])

        z = 2
        f1 = lambda z: z**2 + sin(z)
        assert(Forward(f1, 1).jacobian(z) == [2 * 2 + np.cos(2)])

        # multiple inputs, single function
        w = 2
        f = lambda x, w: x * w ** 2
        assert(Forward(f, 2).jacobian(x, w)[0][0] == 4)

        # single input, multiple functions
        f = lambda x: log(x)
        f1 = lambda x: 3 * x ** 2
        assert(round(Forward([f, f1], 1).jacobian(x)[0][0], 2) == 1/2)
        assert(round(Forward([f, f1], 1).jacobian(x)[1][0], 2) == 12.0)

        x = 2
        y = 3
        f1 = lambda x, y: x ** 2 + y
        f2 = lambda x, y: log(y) - x / y

        j = Forward([f1, f2], 2).jacobian(x, y)
        j_f1 = j[0]
        j_f2 = j[1]
        assert(j_f1[0] == 4)
        assert(j_f1[1] == 1)
        assert(j_f2[0] == -1/3)
        assert(j_f2[1] == (2 + 3)/3**2)

        x = 2
        y = 3
        f1 = lambda x, y: x ** 2 + y
        f2 = lambda x, y: y**2 - x**2
        f3 = lambda x : x + 1
        test = Forward([f1, f2, f3], 2).jacobian(x, y)
        assert(test[0][0] == 4.)
        assert(test[0][1] == 1.)
        assert(test[1][0] == -4.)
        assert(test[1][1] == 6.)
        assert(test[2][0] == 1.)
        assert(test[2][1] == 0.)
    
    def test_errors():
        with pytest.raises(ValueError):
            Forward("hello", 1).evaluate(1)
        with pytest.raises(ValueError):
            Forward(["hello"], 1).evaluate(1)
        with pytest.raises(ValueError):
            Forward([], 1).evaluate(1)
        with pytest.raises(ValueError):
            x = 2
            y = 3
            f1 = lambda x, y: x ** 2 + y
            f2 = lambda x, y: log(y) - x / y
            Forward([f1, f2], 1).evaluate(x, y)
        with pytest.raises(ValueError):
            x = 2
            y = 3
            f1 = lambda x, y: x ** 2 + y
            f2 = lambda x, y: log(y) - x / y
            Forward([f1, f2], 3).evaluate(x, y)
        with pytest.raises(ValueError):
            x = 2
            y = 3
            f1 = lambda x, y: x ** 2 + y
            f2 = lambda x, y: log(y) - x / y
            Forward([f1, f2], 1).jacobian(x, y)
        with pytest.raises(ValueError):
            x = 2
            y = 3
            f1 = lambda x, y: x ** 2 + y
            f2 = lambda x, y: log(y) - x / y
            Forward([f1, f2], 3).jacobian(x, y)

    test_init()
    test_evaluate()
    test_derivative()
    test_jacobian()
    test_errors()

test_forward_mode()
