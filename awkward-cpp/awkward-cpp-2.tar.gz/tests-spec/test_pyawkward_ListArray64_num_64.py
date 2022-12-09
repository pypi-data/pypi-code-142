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

def test_pyawkward_ListArray64_num_64_1():
    tonum = [123, 123, 123]
    fromstarts = [2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    fromstops = [3, 2, 4, 5, 3, 4, 2, 5, 3, 4, 6, 11]
    length = 3
    funcPy = getattr(kernels, 'awkward_ListArray64_num_64')
    funcPy(tonum=tonum, fromstarts=fromstarts, fromstops=fromstops, length=length)
    pytest_tonum = [1.0, 2.0, 2.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_ListArray64_num_64_2():
    tonum = [123, 123, 123]
    fromstarts = [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    fromstops = [8, 4, 5, 6, 5, 5, 7]
    length = 3
    funcPy = getattr(kernels, 'awkward_ListArray64_num_64')
    funcPy(tonum=tonum, fromstarts=fromstarts, fromstops=fromstops, length=length)
    pytest_tonum = [7.0, 4.0, 5.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_ListArray64_num_64_3():
    tonum = [123, 123, 123]
    fromstarts = [1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2]
    fromstops = [1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2]
    length = 3
    funcPy = getattr(kernels, 'awkward_ListArray64_num_64')
    funcPy(tonum=tonum, fromstarts=fromstarts, fromstops=fromstops, length=length)
    pytest_tonum = [0.0, 0.0, 0.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_ListArray64_num_64_4():
    tonum = [123, 123, 123]
    fromstarts = [1, 7, 6, 1, 3, 4, 2, 5, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2]
    fromstops = [1, 9, 6, 2, 4, 5, 3, 6, 3, 4, 2, 4, 5, 5, 7, 8, 2, 3]
    length = 3
    funcPy = getattr(kernels, 'awkward_ListArray64_num_64')
    funcPy(tonum=tonum, fromstarts=fromstarts, fromstops=fromstops, length=length)
    pytest_tonum = [0.0, 2.0, 0.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

def test_pyawkward_ListArray64_num_64_5():
    tonum = [123, 123, 123]
    fromstarts = [0, 0, 0, 0, 0, 0, 0, 0]
    fromstops = [1, 1, 1, 1, 1, 1, 1, 1]
    length = 3
    funcPy = getattr(kernels, 'awkward_ListArray64_num_64')
    funcPy(tonum=tonum, fromstarts=fromstarts, fromstops=fromstops, length=length)
    pytest_tonum = [1.0, 1.0, 1.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)

