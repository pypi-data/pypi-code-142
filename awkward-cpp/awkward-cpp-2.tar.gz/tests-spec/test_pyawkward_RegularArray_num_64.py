# AUTO GENERATED ON 2022-12-09 AT 09:28:13
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import pytest
import kernels

def test_pyawkward_RegularArray_num_64_1():
    tonum = [123, 123, 123]
    size = 3
    length = 3
    funcPy = getattr(kernels, 'awkward_RegularArray_num_64')
    funcPy(tonum=tonum, size=size, length=length)
    pytest_tonum = [3, 3, 3]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_RegularArray_num_64_2():
    tonum = [123, 123, 123]
    size = 2
    length = 3
    funcPy = getattr(kernels, 'awkward_RegularArray_num_64')
    funcPy(tonum=tonum, size=size, length=length)
    pytest_tonum = [2, 2, 2]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_RegularArray_num_64_3():
    tonum = [123, 123, 123]
    size = 1
    length = 3
    funcPy = getattr(kernels, 'awkward_RegularArray_num_64')
    funcPy(tonum=tonum, size=size, length=length)
    pytest_tonum = [1, 1, 1]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_RegularArray_num_64_4():
    tonum = [123, 123, 123]
    size = 2
    length = 3
    funcPy = getattr(kernels, 'awkward_RegularArray_num_64')
    funcPy(tonum=tonum, size=size, length=length)
    pytest_tonum = [2, 2, 2]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_RegularArray_num_64_5():
    tonum = [123, 123, 123]
    size = 0
    length = 3
    funcPy = getattr(kernels, 'awkward_RegularArray_num_64')
    funcPy(tonum=tonum, size=size, length=length)
    pytest_tonum = [0, 0, 0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

