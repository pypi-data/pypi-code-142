"""
============================
Project: pytest-py15
Time:2022/12/1 20:10
E-mail:121292679@qq.com
============================
"""
import gevent
from gevent.monkey import patch_all

patch_all()


# 添加pytest的命令行参数
def pytest_addoption(parser):
    # 添加参数分组
    group = parser.getgroup('pytest-lemon')
    # 添加参数信息
    group.addoption('--current', default=None, help='运行的线程数量')
    group.addoption('--runTask', default=None, help='并发的任务粒度 mod or case')


def run_test(items):
    """
    并发执行的任务函数
    :param items: 包含用例的列表
    :return:
    """
    for item in items:
        # 执行单条用例
        item.ihook.pytest_runtest_protocol(item=item, nextitem=None)


def pytest_runtestloop(session):
    """pytest用例执行的钩子函数"""

    # 获取命令传入的参数
    current = session.config.getoption('--current')
    runTask = session.config.getoption('--runTask')

    # 根据参数拆分并发执行的任务粒度
    if runTask == 'mod':
        case_dict = {}
        # 遍历所有的用例
        for item in session.items:
            # 获取用例所属的模块
            module = item.module
            # 判断case_list中是否有该模块
            if case_dict.get(module):
                # 保存用例
                case_dict[module].append(item)
            else:
                # 把模块作为key保存得到case_dict
                case_dict[module] = [item]

        # 以模块为单位并发执行(一个模块一个并发)
        gs = []
        for cases in case_dict.values():
            g = gevent.spawn(run_test, cases)
            gs.append(g)

        gevent.joinall(gs)

    return True
