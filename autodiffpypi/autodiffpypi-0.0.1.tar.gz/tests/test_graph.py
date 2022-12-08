from multiprocessing import parent_process
import pytest
from src.structures.graph import Node
import numpy as np


def test_graph():
    """
    Test suite for the Node class within graph.py
    Includes tests for the following operators:
    __init__, __neg__, __pos, __add__, __radd__
    __mul__, __rmul__, __sub__, __rsub__
    __trudiv__, __rtruediv__, __pow__, __rpow__,
    get_gradients
    And comparison operators:
    __eq__, __neq__
    __gt__, __ge__
    __lt__, __le__
    """
    def test_init():
        # base constructor test with int
        test_obj = Node(1)
        assert test_obj.value == 1
        assert test_obj.parent_gradients == []
        assert test_obj.name == ""
        assert test_obj.derivative == 1
        
        # base constructor test with array
        test_obj2 = Node(1, [(2, 3)], "x", 3)
        assert test_obj2.value == 1
        assert test_obj2.parent_gradients == [(2, 3)]
        assert test_obj2.name == "x"
        assert test_obj2.derivative == 3

        # dunder direct constructor test
        test_obj2.__init__(100, [(3, 2)], "y", 3)
        assert test_obj2.value == 100
        assert test_obj2.parent_gradients == [(3, 2)]
        assert test_obj2.name == "y"
        assert test_obj2.derivative == 3

        # type test
        test_obj3 = Node(1, 2)
        assert isinstance(test_obj3, Node)

        with pytest.raises(TypeError):
            Node("hello", "hi")

    def test_repr():
        x = Node(350, [])
        assert x.__repr__() == "Node name: "", value: 350, parent gradients: [], derivative: 1"


    def test_gradient():
        x = Node(350, [], "x")
        y = Node(-4, [], "y")
        f = (x / y - x) * (y / x + x + y) * (x - y)

        gradients = f.get_gradients()
        # the partial derivative of result with respect to x
        assert gradients[x] == -459350
        # the partial derivative of result with respect to y
        assert gradients[y] == -5366393/2

        x = Node(2)
        y = Node(5)
        f = 3*x + 5*y
        assert f.get_gradients()[y] == 5
        assert f.get_gradients()[x] == 3

    def test_neg():
        x = Node(2)
        x = -x
        assert x.value == -2

    def test_addition_node():
        node1 = Node(1)
        node2 = Node(2)

        # node + node
        res = node1 + node2
        assert res.value == 3

        # unsupported + node
        str1 = '2'
        with pytest.raises(TypeError):
            str1 + node1
            node1 + str1

    def test_addition():
        node1 = Node(1, [])
        node2 = Node(2, [])
        int1 = 5
        float1 = 10.1

        # int + node
        res = node1 + int1
        assert res.value == 6

        # float + node
        res = node1 + float1
        assert res.value == 11.1

        # node + node
        res = node1 + node2
        assert res.value == 3
        assert res.parent_gradients == [(node1, 1), (node2, 1)]

    def test_radd_node():
        node1 = Node(1, 2)
        node2 = Node(2, 4)
        node1 += node2
        assert node1.value == 3
        assert node1.parent_gradients == [(Node(1, 2), 1), (node2, 1)]

    def test_radd():
        node1 = Node(1, 2)
        node1 += 1
        assert node1.value == 2
        node1 += 1.1
        assert node1.value == 3.1

        int1 = 1
        node1 = Node(4, 2)
        res = int1 + node1
        assert res.value == 5

        with pytest.raises(TypeError):
            "2" + node1

    def test_subtraction_node():
        node1 = Node(1, [1, 4], [0, 7])
        node2 = Node(2, [5, 0], [4, 5])

        # node - node
        res = node1 - node2
        assert res.value == -1
        assert res.parent_gradients == [ (node1, 1), (node2, -1) ]

        # unsupported + node
        str1 = '2'
        with pytest.raises(TypeError):
            str1 - node1
            node1 - str1
    
    def test_subtraction():
        node1 = Node(1, [1, 4], [0, 7])
        int1 = 5
        float1 = 5.1

        # int - node
        res = node1 - int1
        assert res.value == -4
        assert res.parent_gradients == [ (node1, 1) ]

        # float - node
        res = node1 - float1
        assert res.value == -4.1
        assert res.parent_gradients == [ (node1, 1) ]

    def test_rsub_node():
        node1 = Node(1)
        node2 = Node(2)
        node1 -= node2
        assert node1.value == -1
        # x = x - y
        # d/dx x - y = 1
        # d/dy x - y = -1
        assert node1.parent_gradients == [ (Node(1), 1), (node2, -1) ]    

    def test_rsub():
        node1 = Node(1)
        node1 -= 1
        assert node1.value == 0
        assert node1.parent_gradients == [ (Node(1), 1) ] 
        node1 -= 1.1
        assert node1.value == -1.1
        assert node1.parent_gradients == [ (Node(0, [(Node(1), 1)]), 1) ] 

        int1 = 1
        node1 = Node(4)
        res = int1 - node1
        assert res.value == -3
        assert res.parent_gradients == [ (node1, -1) ]

        with pytest.raises(TypeError):
            "2" - node1

    def test_multiplication_node():
        node1 = Node(1)
        node2 = Node(2)

        # node * node
        res = node1 * node2
        assert res.value == (node1.value * node2.value)
        assert res.parent_gradients == [ (node1, 2), (node2, 1) ]

        # unsupported * node
        str1 = '2'
        with pytest.raises(TypeError):
            str1 * node1
            node1 * str1

    def test_multiplication():
        node1 = Node(1)
        int1 = 5
        float1 = 10.1

        # int * node
        res = node1 * int1
        assert res.value == (node1.value * int1)
        assert res.parent_gradients == [ (node1, 5)]
        
        # float * node
        res = node1 * float1
        assert res.value == (node1.value * float1)
        assert res.parent_gradients == [ (node1, 10.1) ]

    def test_rmul_node():
        node1 = Node(5)
        node2 = Node(2)
        temp = node1
        node1 *= node2
        assert node1.value == 10
        # derivative of x * y 
        # d/dx xy = y = 2
        # d/dy xy = x = 5
        assert node1.parent_gradients == [ (temp, 2), (node2, 5)]

        int1 = 2
        node3 = Node(2, 2)
        res = int1 * node3
        assert res.value == 4
        assert res.parent_gradients == [ (node3, 2)]

    def test_rmul():
        node1 = Node(1)
        int1 = 2
        float1 = 2.1
        node1 *= int1
        assert node1.value == 2

        node1 *= float1
        assert node1.value == 4.2

        with pytest.raises(TypeError):
            "2" * node1

    def test_truediv_node():
        node1 = Node(2)
        node2 = Node(2)

        # node / node
        res = node1 / node2
        assert res.value == 1
        # x/y where x = 2 and y = 2
        # d/dx x/y = 1/y = 1/2
        # d/dy x/y = - x/y^2 = - 2/4 = 1/2
        assert res.parent_gradients == [ (node1, 0.5), (node2, -0.5)]

        # unsupported / node
        str1 = '2'
        with pytest.raises(TypeError):
            str1 / node1
            node1 / str1

    def test_truediv():
        node1 = Node(2)
        res = node1 / 2
        assert res.value == 1

        node1 = Node(2)
        res = node1 / 2.0
        assert res.value == 1.0

    def test_rtruediv():
        node1 = Node(2)
        res = 2 / node1
        assert res.value == 1
        assert res.parent_gradients == [ (Node(2), -0.5) ]

        with pytest.raises(TypeError):
            "2" / node1

    def test_pow_node():
        node1 = Node(2)
        node2 = Node(4)

        # node / node
        res = node1 ** node2
        assert res.value == 16
        # derivative of x^y
        # d/dx x^y = (y-1) * x ^ y = 3 * 2^4
        # d/dy x^y = log(y) * y^x  = 32log(2)
        assert res.parent_gradients == [ (node1, 32), (node2, 16 * np.log(2)) ]

        # unsupported / node
        str1 = '2'
        with pytest.raises(TypeError):
            str1 ** node1
            node1 ** str1

    def test_pow():
        node1 = Node(2)
        res = node1 ** 2
        assert res.value == 4
        # derivative
        # d/dx x^2 = (1)x^2 = 4
        assert res.parent_gradients == [ (Node(2), 4)]

        node1 = Node(2, 2)
        res = node1 ** 2.0
        assert res.value == 4.0

        with pytest.raises(TypeError):
            node1 ** "2"

    def test_rpow():
        node1 = Node(2)
        res = 3 ** node1
        assert res.value == 9
        # derivative of x^y
        # d/dy x^y = log(x) * x^y  = log(2)* 2^3
        assert res.parent_gradients == [ (Node(2), (2**3) * np.log(2)) ]
        
        with pytest.raises(TypeError):
            "2" ** node1

    def test_reflective_operators():
        node1 = Node(1)
        int1 = 5
        float1 = 10.1
        res = int1 + node1
        assert res.value == 6

        res = float1 + node1
        assert res.value == 11.1

        res = int1 * node1
        assert res.value == (node1.value * int1)

    def test_eq():
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(2)
        node4 = Node(2)
        int1 = 2
        float1 = 2

        assert False == (node1 == node2)
        assert True == (node1 == node3)
        assert True == (int1 == node4)
        assert True == (float1 == node4)

        node5 = Node(2, [(2,3)])
        node6 = Node(2, [(2,3)])
        assert True == (node5 == node6)

        with pytest.raises(TypeError):
            node1 == "2"


    def test_ne():
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(2)
        node4 = Node(2)
        int1 = 2
        float1 = 2.0

        assert True == (node1 != node2)
        assert False == (node1 != node3)
        assert False == (int1 != node4)
        assert False == (float1 != node4)

        node5 = Node(2, [(2,3)])
        node6 = Node(2, [(4,5)])
        assert True == (node5 != node6)

        with pytest.raises(TypeError):
            node1 != "2"

    def test_lt():
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(2)
        node4 = Node(2)
        int1 = 2
        float1 = 2.0

        assert True == (node1 < node2)
        assert False == (node1 < node3)
        assert False == (node3 < node1)
        assert True == (int1 < node2)
        assert False == (float1 < node4)

        with pytest.raises(TypeError):
            node1 < "2"

    def test_gt():
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(2)
        node4 = Node(2)
        int1 = 10
        float1 = 1.0

        assert False == (node1 > node2)
        assert False == (node1 > node3)
        assert False == (node3 > node1)
        assert True == (int1 > node2)
        assert False == (float1 > node4)
        
        with pytest.raises(TypeError):
            node1 > "2"

    def test_ge():
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(2)
        node4 = Node(2)
        int1 = 10
        float1 = 3.0

        assert False == (node1 >= node2)
        assert True == (node1 >= node3)
        assert True == (node3 >= node1)
        assert True == (int1 >= node2)
        assert True == (float1 >= node4)
        
        with pytest.raises(TypeError):
            node1 >= "2"

    def test_le():
        node1 = Node(2)
        node2 = Node(3)
        node3 = Node(2)
        node4 = Node(2)
        int1 = 10
        float1 = 3.0

        assert True == (node1 <= node2)
        assert True == (node1 <= node3)
        assert True == (node3 <= node1)
        assert False == (int1 <= node2)
        assert False == (float1 <= node4)

        with pytest.raises(TypeError):
            node1 <= "2"

    test_init()
    test_gradient()
    test_neg()
    test_addition()
    test_addition_node()
    test_radd_node()
    test_radd()
    test_subtraction()
    test_subtraction_node()
    test_rsub_node()
    test_rsub()
    test_multiplication()
    test_multiplication_node()
    test_rmul_node()
    test_rmul()
    test_truediv_node()
    test_truediv()
    test_rtruediv()
    test_pow_node()
    test_pow()
    test_rpow()
    test_eq()
    test_ne()
    test_lt()
    test_gt()
    test_ge()
    test_le()
    test_reflective_operators()

if __name__ == '__main__':
    test_graph()
    print("Good job! All tests passed.")