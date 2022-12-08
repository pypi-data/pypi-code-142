import pytest
from src.autodiffpypi.dual_number import DualNumber
import numpy as np


def test_dual_number():
    """
    Test suite for the Dual_Number class.
    Includes tests for the following operators:
    __init__, __neg__, __pos, __add__, __radd__
    __mul__, __rmul__, __sub__, __rsub__
    __trudiv__, __rtruediv__, __pow__, __rpow__
    And comparison operators:
    __eq__, __neq__
    __gt__, __ge__
    __lt__, __le__
    """
    def test_init():
        # base constructor test
        test_obj = DualNumber(1, 2)
        assert test_obj.real == 1
        assert test_obj.dual == 2

        # dunder direct constructor test
        test_obj2 = DualNumber(1, 2)
        assert test_obj2.real == 1
        assert test_obj2.dual == 2

        test_obj2.__init__(2, 1)
        assert test_obj2.real == 2
        assert test_obj2.dual == 1

        # type test
        test_obj3 = DualNumber(1, 2)
        assert isinstance(test_obj3, DualNumber)

        with pytest.raises(TypeError):
            DualNumber("hello", "hi")

    def test_neg():
        x = DualNumber(2, 1)
        x = -x
        assert x.real == -2
        assert x.dual == -1

    def test_addition_dual():
        dual1 = DualNumber(1, 2)
        dual2 = DualNumber(2, 4)

        # dual + dual
        res = dual1 + dual2
        assert res.real == 3
        assert res.dual == 6

        # unsupported + dual
        str1 = '2'
        with pytest.raises(TypeError):
            str1 + dual1
            dual1 + str1

    def test_addition():
        dual1 = DualNumber(1, 2)
        int1 = 5
        float1 = 10.1

        # int + dual
        res = dual1 + int1
        assert res.real == 6
        assert res.dual == 2

        # float + dual
        res = dual1 + float1
        assert res.real == 11.1
        assert res.dual == 2

    def test_radd_dual():
        dual1 = DualNumber(1, 2)
        dual2 = DualNumber(2, 4)
        dual1 += dual2
        assert dual1.real == 3
        assert dual1.dual == 6

    def test_radd():
        dual1 = DualNumber(1, 2)
        dual1 += 1
        assert dual1.real == 2
        dual1 += 1.1
        assert dual1.real == 3.1

        int1 = 1
        dual1 = DualNumber(4, 2)
        res = int1 + dual1
        assert res.real == 5
        assert res.dual == 2

    def test_subtraction_dual():
        dual1 = DualNumber(1, 2)
        dual2 = DualNumber(2, 4)

        # dual - dual
        res = dual1 - dual2
        assert res.real == -1
        assert res.dual == -2

        # unsupported + dual
        str1 = '2'
        with pytest.raises(TypeError):
            str1 - dual1
            dual1 - str1
    
    def test_subtraction():
        dual1 = DualNumber(1, 2)
        int1 = 5
        float1 = 5.1

        # int - dual
        res = dual1 - int1
        assert res.real == -4
        assert res.dual == 2

        # float - dual
        res = dual1 - float1
        assert res.real == -4.1
        assert res.dual == 2

    def test_rsub_dual():
        dual1 = DualNumber(1, 2)
        dual2 = DualNumber(2, 4)
        dual1 -= dual2
        assert dual1.real == -1
        assert dual1.dual == -2

    def test_rsub():
        dual1 = DualNumber(1, 2)
        dual1 -= 1
        assert dual1.real == 0
        dual1 -= 1.1
        assert dual1.real == -1.1

        int1 = 1
        dual1 = DualNumber(4, 2)
        res = int1 - dual1
        assert res.real == -3
        assert res.dual == -2

    def test_multiplication_dual():
        dual1 = DualNumber(1, 2)
        dual2 = DualNumber(2, 4)

        # dual * dual
        res = dual1 * dual2
        assert res.real == (dual1.real * dual2.real)
        assert res.dual == ((dual1.real * dual2.dual) +
                            (dual2.real * dual1.dual))

        # unsupported * dual
        str1 = '2'
        with pytest.raises(TypeError):
            str1 * dual1
            dual1 * str1

    def test_multiplication():
        dual1 = DualNumber(1, 2)
        int1 = 5
        float1 = 10.1

        # int * dual
        res = dual1 * int1
        assert res.real == (dual1.real * int1)
        assert res.dual == (dual1.dual * int1)

        # float * dual
        res = dual1 * float1
        assert res.real == (dual1.real * float1)
        assert res.dual == (dual1.dual * float1)

    def test_rmul_dual():
        dual1 = DualNumber(1, 2)
        dual2 = DualNumber(2, 4)
        dual1 *= dual2
        assert dual1.real == 2
        assert dual1.dual == 8

        int1 = 2
        dual3 = DualNumber(2, 2)
        res = int1 * dual3
        assert res.real == 4
        assert res.dual == 4

    def test_rmul():
        dual1 = DualNumber(1, 2)
        int1 = 2
        float1 = 2.1
        dual1 *= int1
        assert dual1.real == 2
        assert dual1.dual == 4
        dual1 *= float1
        assert dual1.real == 4.2
        assert dual1.dual == 8.4

    def test_truediv_dual():
        dual1 = DualNumber(2, 2)
        dual2 = DualNumber(2, 4)

        # dual / dual
        res = dual1 / dual2
        assert res.real == 1
        assert res.dual == -1

        # unsupported / dual
        str1 = '2'
        with pytest.raises(TypeError):
            str1 / dual1
            dual1 / str1

    def test_truediv():
        dual1 = DualNumber(2, 2)
        res = dual1 / 2
        assert res.real == 1
        assert res.dual == 1

        dual1 = DualNumber(2, 2)
        res = dual1 / 2.0
        assert res.real == 1.0
        assert res.dual == 1.0

    def test_rtruediv():
        dual1 = DualNumber(2, 2)
        res = 2 / dual1
        assert res.real == 1
        assert res.dual == 1

    def test_pow_dual():
        dual1 = DualNumber(2, 1)
        dual2 = DualNumber(4, 1)

        # dual / dual
        res = dual1 ** dual2
        assert res.real == 16
        assert res.dual == 32 + 16 * np.log(2)

        # unsupported / dual
        str1 = '2'
        with pytest.raises(TypeError):
            str1 ** dual1
            dual1 ** str1

    def test_pow():
        dual1 = DualNumber(2, 2)
        res = dual1 ** 2
        assert res.real == 4
        assert res.dual == 8

        dual1 = DualNumber(2, 2)
        res = dual1 ** 2.0
        assert res.real == 4.0
        assert res.dual == 8.0

    def test_rpow():
        dual1 = DualNumber(2, 2)
        res = 2 ** dual1
        assert res.real == 4
        assert res.dual == np.log(2) * (4) * 2
     
    def test_reflective_operators():
        dual1 = DualNumber(1, 2)
        int1 = 5
        float1 = 10.1
        res = int1 + dual1
        assert res.real == 6
        assert res.dual == 2

        res = float1 + dual1
        assert res.real == 11.1
        assert res.dual == 2

        res = int1 * dual1
        assert res.real == (dual1.real * int1)
        assert res.dual == (dual1.dual * int1)

    def test_eq():
        dual1 = DualNumber(2, 2)
        dual2 = DualNumber(3, 3)
        dual3 = DualNumber(2, 2)
        dual4 = DualNumber(2, 1)
        int1 = 2
        float1 = 2

        assert False == (dual1 == dual2)
        assert True == (dual1 == dual3)
        assert True == (int1 == dual4)
        assert True == (float1 == dual4)
    
    def test_ne():
        dual1 = DualNumber(2, 2)
        dual2 = DualNumber(3, 3)
        dual3 = DualNumber(2, 2)
        dual4 = DualNumber(2, 1)
        int1 = 2
        float1 = 2.0

        assert True == (dual1 != dual2)
        assert False == (dual1 != dual3)
        assert False == (int1 != dual4)
        assert False == (float1 != dual4)

    def test_lt():
        dual1 = DualNumber(2, 2)
        dual2 = DualNumber(3, 3)
        dual3 = DualNumber(2, 2)
        dual4 = DualNumber(2, 1)
        int1 = 2
        float1 = 2.0

        assert True == (dual1 < dual2)
        assert False == (dual1 < dual3)
        assert False == (dual3 < dual1)
        assert True == (int1 < dual2)
        assert False == (float1 < dual4)

    def test_gt():
        dual1 = DualNumber(2, 2)
        dual2 = DualNumber(3, 3)
        dual3 = DualNumber(2, 2)
        dual4 = DualNumber(2, 1)
        int1 = 10
        float1 = 1.0

        assert False == (dual1 > dual2)
        assert False == (dual1 > dual3)
        assert False == (dual3 > dual1)
        assert True == (int1 > dual2)
        assert False == (float1 > dual4)

    def test_ge():
        dual1 = DualNumber(2, 2)
        dual2 = DualNumber(3, 3)
        dual3 = DualNumber(2, 2)
        dual4 = DualNumber(2, 1)
        int1 = 10
        float1 = 3.0

        assert False == (dual1 >= dual2)
        assert True == (dual1 >= dual3)
        assert True == (dual3 >= dual1)
        assert True == (int1 >= dual2)
        assert True == (float1 >= dual4)

    def test_le():
        dual1 = DualNumber(2, 2)
        dual2 = DualNumber(3, 3)
        dual3 = DualNumber(2, 2)
        dual4 = DualNumber(2, 1)
        int1 = 10
        float1 = 3.0

        assert True == (dual1 <= dual2)
        assert True == (dual1 <= dual3)
        assert True == (dual3 <= dual1)
        assert False == (int1 <= dual2)
        assert False == (float1 <= dual4)

    test_init()
    test_neg()
    test_addition()
    test_addition_dual()
    test_radd_dual()
    test_radd()
    test_subtraction()
    test_subtraction_dual()
    test_rsub_dual()
    test_rsub()
    test_multiplication()
    test_multiplication_dual()
    test_rmul_dual()
    test_rmul()
    test_truediv_dual()
    test_truediv()
    test_rtruediv()
    test_pow_dual()
    test_pow()
    test_rpow()
    test_eq()
    test_ne()
    test_lt()
    test_gt()
    test_ge()
    test_le()
    test_reflective_operators()


test_dual_number()
