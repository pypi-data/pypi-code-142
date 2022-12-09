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

def test_cpuawkward_ListArrayU32_num_64_1():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    fromstarts = [2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
    fromstarts = (ctypes.c_uint32*len(fromstarts))(*fromstarts)
    fromstops = [3, 2, 4, 5, 3, 4, 2, 5, 3, 4, 6, 11]
    fromstops = (ctypes.c_uint32*len(fromstops))(*fromstops)
    length = 3
    funcC = getattr(lib, 'awkward_ListArrayU32_num_64')
    ret_pass = funcC(tonum, fromstarts, fromstops, length)
    pytest_tonum = [1.0, 2.0, 2.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_ListArrayU32_num_64_2():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    fromstarts = [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
    fromstarts = (ctypes.c_uint32*len(fromstarts))(*fromstarts)
    fromstops = [8, 4, 5, 6, 5, 5, 7]
    fromstops = (ctypes.c_uint32*len(fromstops))(*fromstops)
    length = 3
    funcC = getattr(lib, 'awkward_ListArrayU32_num_64')
    ret_pass = funcC(tonum, fromstarts, fromstops, length)
    pytest_tonum = [7.0, 4.0, 5.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_ListArrayU32_num_64_3():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    fromstarts = [1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2]
    fromstarts = (ctypes.c_uint32*len(fromstarts))(*fromstarts)
    fromstops = [1, 4, 5, 6, 5, 5, 7, 1, 2, 1, 3, 1, 5, 3, 2]
    fromstops = (ctypes.c_uint32*len(fromstops))(*fromstops)
    length = 3
    funcC = getattr(lib, 'awkward_ListArrayU32_num_64')
    ret_pass = funcC(tonum, fromstarts, fromstops, length)
    pytest_tonum = [0.0, 0.0, 0.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_ListArrayU32_num_64_4():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    fromstarts = [1, 7, 6, 1, 3, 4, 2, 5, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2]
    fromstarts = (ctypes.c_uint32*len(fromstarts))(*fromstarts)
    fromstops = [1, 9, 6, 2, 4, 5, 3, 6, 3, 4, 2, 4, 5, 5, 7, 8, 2, 3]
    fromstops = (ctypes.c_uint32*len(fromstops))(*fromstops)
    length = 3
    funcC = getattr(lib, 'awkward_ListArrayU32_num_64')
    ret_pass = funcC(tonum, fromstarts, fromstops, length)
    pytest_tonum = [0.0, 2.0, 0.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

def test_cpuawkward_ListArrayU32_num_64_5():
    tonum = [123, 123, 123]
    tonum = (ctypes.c_int64*len(tonum))(*tonum)
    fromstarts = [0, 0, 0, 0, 0, 0, 0, 0]
    fromstarts = (ctypes.c_uint32*len(fromstarts))(*fromstarts)
    fromstops = [1, 1, 1, 1, 1, 1, 1, 1]
    fromstops = (ctypes.c_uint32*len(fromstops))(*fromstops)
    length = 3
    funcC = getattr(lib, 'awkward_ListArrayU32_num_64')
    ret_pass = funcC(tonum, fromstarts, fromstops, length)
    pytest_tonum = [1.0, 1.0, 1.0]
    assert tonum[:len(pytest_tonum)] == pytest.approx(pytest_tonum)
    assert not ret_pass.str

