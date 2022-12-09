import pytest
import kernels

def test_awkward_RegularArray_num_1():
	tonum = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123]
	length = 15
	size = 2
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	assert tonum == pytest_tonum


def test_awkward_RegularArray_num_2():
	tonum = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123]
	length = 21
	size = 2
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
	assert tonum == pytest_tonum


def test_awkward_RegularArray_num_3():
	tonum = [123, 123]
	length = 2
	size = 3
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [3, 3]
	assert tonum == pytest_tonum


def test_awkward_RegularArray_num_4():
	tonum = [123, 123, 123, 123, 123, 123, 123]
	length = 7
	size = 3
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [3, 3, 3, 3, 3, 3, 3]
	assert tonum == pytest_tonum


def test_awkward_RegularArray_num_5():
	tonum = [123, 123, 123, 123, 123]
	length = 5
	size = 3
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [3, 3, 3, 3, 3]
	assert tonum == pytest_tonum


def test_awkward_RegularArray_num_6():
	tonum = [123, 123, 123]
	length = 3
	size = 5
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [5, 5, 5]
	assert tonum == pytest_tonum


def test_awkward_RegularArray_num_7():
	tonum = [123, 123, 123, 123, 123, 123]
	length = 6
	size = 5
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [5, 5, 5, 5, 5, 5]
	assert tonum == pytest_tonum


def test_awkward_RegularArray_num_8():
	tonum = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123, 123]
	length = 30
	size = 7
	funcPy = getattr(kernels, 'awkward_RegularArray_num')
	funcPy(tonum = tonum,length = length,size = size)
	pytest_tonum = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
	assert tonum == pytest_tonum


