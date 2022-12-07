import random


def get_number():
    lst = random.randint(0, 9999)
    print("这次中将的数字为：", lst)


if __name__ == '__main__':
    get_number()
