def list2_sort_by_list(list2: list[list], according: list) -> list[list]:
    """
    对二维列表排序，主要针对excel
    :param list2:二维列表
    :param according: 按照此列表对二维列表排序
    :return: list[list]
    """
    if len(according) != len(set(according)):
        print('according不能有重复值')
        input("继续，但是没卵用：")
        return [[]]
    newlist2 = []
    sort_order = {}
    for i in list2[0]:
        sort_order[i] = according.index(i)

    for i in list2:
        newi = None
        newi = list(range(len(i)))
        k = 0
        for j in i:
            firstline_value = list2[0][k]
            newi[sort_order[firstline_value]] = j
            k += 1
        newlist2.append(newi)
    return newlist2


def list_sort_by_index(task_list: list, old_index: int, insert_index: int) -> list:
    """
    移动list元素位置
    :param task_list: list,要处理的list
    :param old_index: int, 该值原先处于列表的位置
    :param insert_index: int, 移动到哪个位置
    :return: list
    """
    task_list.insert(insert_index, task_list.pop(old_index))
    return task_list


def list2_sort_by_index(task_list2: list[list], old_index: int, insert_index: int) -> list[list]:
    """
    移动二维列表元素位置，针对excel表格数据
    :param task_list: list[list],要处理的二维列表
    :param old_index: int, 该值原先处于列表的位置
    :param insert_index: int, 移动到哪个位置
    :return: list[list]
    """
    for task_list in task_list2:
        task_list.insert(insert_index, task_list.pop(old_index))
    return task_list2

def list2_split(task_list2:list[list],index_:int,split_by_str:str) -> list[list]:
    """
    二维列表单列分两列，空的用None
    :param task_list2: list[list],二维列表
    :param index_: int,按一维列表的index来
    :param split_by_str: 分割符号
    :return: list[list]
    """"
    for t1 in task_list2:
        v = t1[index_].split(split_by_str)
        if len(v)==2:
            v1,v2=v
            t1.pop(index_)
            t1.insert(index_,v1)
            t1.insert(index_+1, v2)
        elif len(v)==1:
            v1=v[0]
            v2=None
            t1.pop(index_)
            t1.insert(index_, v1)
            t1.insert(index_ + 1, v2)
        else:
            print('GRD,数据有问题，怎么出现多个'+split_by_str)
            print('出现问题的列表',t1)
            print('这儿出现的问题', t1[index_])
            input('继续，会有未知问题：')
    return task_list2


