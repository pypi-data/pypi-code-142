import pytest
import kernels

def test_awkward_ListArray_num_1():
	tonum = [123, 123]
	fromstarts = [0, 0]
	fromstops = [0, 0]
	length = 2
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [0, 0]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_2():
	tonum = [123]
	fromstarts = [0]
	fromstops = [0]
	length = 1
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [0]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_3():
	tonum = [123, 123, 123]
	fromstarts = [0, 0, 1]
	fromstops = [0, 1, 1]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [0, 1, 0]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_4():
	tonum = [123, 123, 123, 123, 123, 123, 123, 123, 123]
	fromstarts = [0, 0, 1, 1, 2, 4, 4, 5, 7]
	fromstops = [0, 1, 1, 2, 4, 4, 5, 7, 10]
	length = 9
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [0, 1, 0, 1, 2, 0, 1, 2, 3]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_5():
	tonum = [123, 123, 123]
	fromstarts = [0, 0, 1]
	fromstops = [0, 1, 2]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [0, 1, 1]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_6():
	tonum = [123, 123, 123, 123, 123, 123, 123, 123, 123, 123]
	fromstarts = [0, 0, 1, 2, 2, 3, 3, 3, 4, 5]
	fromstops = [0, 1, 2, 2, 3, 3, 3, 4, 5, 5]
	length = 10
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_7():
	tonum = [123, 123, 123, 123]
	fromstarts = [0, 0, 1, 3]
	fromstops = [0, 1, 3, 6]
	length = 4
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [0, 1, 2, 3]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_8():
	tonum = [123, 123, 123, 123, 123, 123, 123, 123]
	fromstarts = [0, 1, 2, 2, 3, 3, 3, 4]
	fromstops = [1, 2, 2, 3, 3, 3, 4, 5]
	length = 8
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [1, 1, 0, 1, 0, 0, 1, 1]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_9():
	tonum = [123, 123, 123, 123]
	fromstarts = [0, 1, 2, 3]
	fromstops = [1, 2, 3, 4]
	length = 4
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [1, 1, 1, 1]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_10():
	tonum = [123, 123, 123, 123, 123]
	fromstarts = [0, 0, 0, 0, 0]
	fromstops = [1, 1, 1, 1, 1]
	length = 5
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [1, 1, 1, 1, 1]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_11():
	tonum = [123, 123, 123]
	fromstarts = [0, 1, 3]
	fromstops = [1, 3, 6]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [1, 2, 3]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_12():
	tonum = [123, 123, 123, 123]
	fromstarts = [0, 2, 3, 3]
	fromstops = [2, 3, 3, 5]
	length = 4
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [2, 1, 0, 2]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_13():
	tonum = [123, 123, 123, 123]
	fromstarts = [3, 3, 3, 0]
	fromstops = [5, 5, 3, 3]
	length = 4
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [2, 2, 0, 3]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_14():
	tonum = [123, 123, 123, 123, 123]
	fromstarts = [0, 0, 0, 0, 0]
	fromstops = [2, 2, 2, 2, 2]
	length = 5
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [2, 2, 2, 2, 2]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_15():
	tonum = [123, 123, 123]
	fromstarts = [0, 2, 5]
	fromstops = [2, 5, 9]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [2, 3, 4]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_16():
	tonum = [123, 123, 123, 123, 123]
	fromstarts = [0, 3, 3, 10, 10]
	fromstops = [3, 3, 5, 10, 13]
	length = 5
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [3, 0, 2, 0, 3]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_17():
	tonum = [123, 123, 123]
	fromstarts = [0, 3, 3]
	fromstops = [3, 3, 5]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [3, 0, 2]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_18():
	tonum = [123, 123, 123]
	fromstarts = [0, 3, 5]
	fromstops = [3, 3, 7]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [3, 0, 2]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_19():
	tonum = [123, 123, 123, 123, 123]
	fromstarts = [0, 3, 3, 5, 6]
	fromstops = [3, 3, 5, 6, 10]
	length = 5
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [3, 0, 2, 1, 4]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_20():
	tonum = [123, 123, 123, 123]
	fromstarts = [0, 3, 5, 6]
	fromstops = [3, 5, 6, 6]
	length = 4
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [3, 2, 1, 0]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_21():
	tonum = [123, 123, 123]
	fromstarts = [0, 3, 6]
	fromstops = [3, 6, 9]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [3, 3, 3]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_22():
	tonum = [123, 123, 123, 123, 123]
	fromstarts = [0, 0, 0, 0, 0]
	fromstops = [3, 3, 3, 3, 3]
	length = 5
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [3, 3, 3, 3, 3]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_23():
	tonum = [123, 123, 123, 123, 123]
	fromstarts = [0, 0, 0, 0, 0]
	fromstops = [4, 4, 4, 4, 4]
	length = 5
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [4, 4, 4, 4, 4]
	assert tonum == pytest_tonum


def test_awkward_ListArray_num_24():
	tonum = [123, 123, 123]
	fromstarts = [0, 5, 10]
	fromstops = [5, 10, 15]
	length = 3
	funcPy = getattr(kernels, 'awkward_ListArray_num')
	funcPy(tonum = tonum,fromstarts = fromstarts,fromstops = fromstops,length = length)
	pytest_tonum = [5, 5, 5]
	assert tonum == pytest_tonum


