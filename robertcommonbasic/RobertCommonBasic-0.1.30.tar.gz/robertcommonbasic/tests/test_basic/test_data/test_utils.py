import re
import sys
from robertcommonbasic.basic.data.utils import format_value, revert_exp, chunk_list

def test_format_value():

    print(f"format_value('1.234', '1') = {format_value('1.234', '1')}")
    print(f"format_value('1.234', '-2.0') = {format_value('1.234', '-2.0')}")
    print(f"format_value('-1.234', '2.0') = {format_value('-1.234', '2.0')}")
    print(f"format_value('-1.234', 'v*3') = {format_value('-1.234', 'v*3')}")
    print(f"format_value('测试', '1') = {format_value('测试', '1')}")
    print(f"format_value('测试', '1.2') = {format_value('测试', '1.2')}")
    print(f"format_value('1.234', '') = {format_value('1.234', '')}")

    print(f"format_value('1.234', 'int(v)') = {format_value('1.234', 'int(v)')}")
    print(f"format_value('1.234', 'int(v)') = {format_value('1.234', 'int(v)')}")
    print(f"format_value('2, 'bit(v, 1)') = {format_value('2', 'bit(v, 1)')}")   #取位操作
    print(f"format_value('35535, 'signed(v)') = {format_value('35535', 'signed(v)')}")  # 取位操作
    print(f"format_value('1.234', '1 if v == 20.1234 else 0') = {format_value('1.234', '1 if v == 1.234 else 0')}")

    print()

def test_format_value2():
    print(format_value('5.0', '1 if v == 5 else 0'))
    print(format_value('2', '_or(bit(v, 1), bit(v, 0), _and(bit(v, 0),bit(v, 1)))'))


def test_float_value():
    values = ['123456789.0', '-123456789.0', '9.0', '9.1', '9.12334567', '-9.0', '-9.12300000', '-0.00000567', '-0.000005670001000']
    for value in values:
        print(f"{value} {format_value(value, '1', 7)}")
    print()

def test_format_value3():
    a = format_value('255', 'bit(v, 0)*2+bit(v, 1)')
    print(format_value('255', 'bit(v, 0)'))
    print(format_value('255', 'bit(v, 1)'))
    print(format_value('255', 'bit(v, 2)'))
    print(format_value('2', '_or(bit(v, 1), bit(v, 0), _and(bit(v, 0),bit(v, 1)))'))

def test_format_value31():
    a = format_value(str(int(0x7B)), 'bit(v, 0)*2+bit(v, 1)')
    print(format_value('255', 'bit(v, 0)'))
    print(format_value('255', 'bit(v, 1)'))
    print(format_value('255', 'bit(v, 2)'))
    print(format_value(str(int(0x7B)), '_or(bit(v, 1), bit(v, 0), _and(bit(v, 0),bit(v, 1)))'))

    datas = bytes([0x7B])
    freq_ant = int(format_value(str(int(datas[0])), 'bit(v, 0)') + format_value(str(int(datas[0])), 'bit(v, 1)'))
    print(freq_ant)

def test_nvn_value():
    result = format_value('952', '(max(4, v*3.3*1000/(4095*150))-4)/16*100', 3)
    print(format_value('2', '(max(4, v*3.3*1000/(4095*150))-4)/16*100', 3))


def test_conver():
    result = format_value('-1.234', 'v*10/10-1')
    result1 = format_value(str(result), 'v*10/10-1', revert=True)

    result = format_value('952', '(max(4, v*3.3*1000/(4095*150))-4)/16*100', 3)
    print(format_value(str(result), '(max(4, v*3.3*1000/(4095*150))-4)/16*100', 3))
    print()


def test_chunk_list():
    datas = ['1', '2', '3', '4', '5', '6']
    aa = chunk_list(datas, 2)
    ab = list(aa)
    print(len(ab))


test_chunk_list()