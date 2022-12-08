import pytest
from src.autodiffpypi.reverse_mode import Reverse
from src.autodiffpypi.base_derivatives import *
from src.structures.graph import Node

def test_reverse_mode():
    """
    Test suite for the Reverse class, including 
    `evaluate`, `derivative`, and `jacobian`.
    """

    def test_evaluate():
        def f1(x, y):
            return (x / y - x) * (y / x + x + y) * (x - y)
        def f2(x, y):
            return x + y

        x = 350
        y = -4

        reverse_ex = Reverse([f1, f2], 2)
        assert reverse_ex.evaluate([x, y]) == [-53584980.0, 346]
        reverse_ex = Reverse([f1], 2)
        assert reverse_ex.evaluate([x, y]) == [-53584980.0]

        def f1(x, y):
            return x ** y
        def f2(x, y):
            return x + y

        x = 2
        y = 5

        reverse_ex = Reverse([f1, f2], 2)
        value = reverse_ex.evaluate([x, y])
        assert value == [32, 7]

    def test_build_nodes():
        x = 2
        y = 5
        def f1(x, y):
            return x ** y
        def f2(x, y):
            return x + y
        reverse_ex = Reverse([f1, f2], 2)
        value = reverse_ex.build_nodes([x, y])
        value == "[(Node name: , value: 2, parent gradients: [], derivative: 1), (Node name: , value: 5, parent gradients: [], derivative: 1)]"

    def test_errors():
        def f1(x, y):
            return (x / y - x) * (y / x + x + y) * (x - y)
        def f2(x, y):
            return x + y

        x = 350
        y = -4

        reverse_ex = Reverse([f1, f2], 2)
        assert reverse_ex.evaluate([x, y]) == [-53584980.0, 346]

        with pytest.raises(IndexError):
            reverse_ex.evaluate([x])

    def test_derivative():
        x = 2
        def f1(x):
            return 2 * x + x**3 - log(x)
        def f2(x):
            return (x)**(1/2) - sinh(x**2) - 14*exp(x)
        def f3(x):
            return x**2 + sin(x)

        rev = Reverse([f1, f2, f3], 1)
        
        rev_mode = list(rev.derivative(x))
        manual = ([ 2 + 3 * 2**2 - 1 / 2, 1/(2*np.sqrt(2)) - 14*exp(2) - 4*np.cosh(4), 2 * 2 + np.cos(2) ])
        assert rev_mode == manual 

        x = 2
        y = 5
        def f4(x, y):
            return x ** y
        def f5(x, y):
            return  x + y
        reverse_ex = Reverse([f4, f5], 2)
        value = reverse_ex.derivative([x, y], 2)
        assert(round(value[0], 2) == round(32*log(2), 2))
        assert(round(value[1], 2) == 1.0)

    def test_jacobian():
        x = 2
        def f1(x):
            return 2 * x + x**3 - log(x)
        def f2(x):
            return (x)**(1/2) - sinh(x**2) - 14*exp(x)
        def f3(x):
            return x**2 + sin(x)

        rev = Reverse([f1, f2, f3], 1)

        assert list(rev.jacobian([x])) == [ [2 + 3 * 2**2 - 1 / 2], [1/(2*np.sqrt(2)) - 14*exp(2) - 4*np.cosh(4)], [2 * 2 + np.cos(2)] ]

        y = 5
        def f4(x, y):
            return x ** y
        def f5(x, y):
            return y ** x

        rev = Reverse([f4, f5], 2)

        # x ^ y derivatives: y * (x ^ (y - 1)) and x ^ y * log(y)
        result = rev.jacobian([x, y])
        assert(result[0][0] == 80)
        assert(round(result[0][1], 2) == round((2 ** 5) * log(2), 2))
        assert(round(result[1][0], 2) == round((25) * log(5), 2)) 
        assert(result[1][1] == 10)

        x = 2
        y = 3
        def f6(x, y):
            return x ** y
        def f7(x, y):
            return x + y
        reverse_ex = Reverse([f6, f7], 2)
        value = reverse_ex.jacobian([x, y])
        assert list(value) == [ [12, 8*np.log(2)], [1, 1] ]

    # execute tests
    test_evaluate()
    test_build_nodes()
    test_derivative()
    test_jacobian()
    test_errors()

if __name__ == '__main__':
    test_reverse_mode()
    print("Good job! All tests passed.")
