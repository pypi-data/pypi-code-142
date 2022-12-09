# AUTO GENERATED ON 2022-12-09 AT 09:28:13
# DO NOT EDIT BY HAND!
#
# To regenerate file, run
#
#     python dev/generate-tests.py
#

# fmt: off

import ctypes
import pytest

from awkward_cpp.cpu_kernels import lib

def test_cpuawkward_RegularArray_num_64_1():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    size = 3
    length = 3
    funcC = getattr(lib, 'awkward_RegularArray_num_64')
    ret_pass = funcC(tonum, size, length)
    pytest_tonum = [3, 3, 3]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_RegularArray_num_64_2():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    size = 2
    length = 3
    funcC = getattr(lib, 'awkward_RegularArray_num_64')
    ret_pass = funcC(tonum, size, length)
    pytest_tonum = [2, 2, 2]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_RegularArray_num_64_3():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    size = 1
    length = 3
    funcC = getattr(lib, 'awkward_RegularArray_num_64')
    ret_pass = funcC(tonum, size, length)
    pytest_tonum = [1, 1, 1]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_RegularArray_num_64_4():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    size = 2
    length = 3
    funcC = getattr(lib, 'awkward_RegularArray_num_64')
    ret_pass = funcC(tonum, size, length)
    pytest_tonum = [2, 2, 2]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_RegularArray_num_64_5():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    size = 0
    length = 3
    funcC = getattr(lib, 'awkward_RegularArray_num_64')
    ret_pass = funcC(tonum, size, length)
    pytest_tonum = [0, 0, 0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

