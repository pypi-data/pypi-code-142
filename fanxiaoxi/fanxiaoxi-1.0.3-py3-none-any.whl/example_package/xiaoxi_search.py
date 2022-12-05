list1 = ['张三', '李四', '王五']


def search():
    for i in list1:
        print('查询结果', i)

    print('查询完毕')
    return list1


if __name__ == '__main__':
    search()
