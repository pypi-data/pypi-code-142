import gevent
from gevent.monkey import patch_all

patch_all()
from concurrent.futures.thread import ThreadPoolExecutor

def pytest_runtestloop(session):
    """用例执行的钩子函数"""
    # 获取命令传入的参数
    runTask = session.config.getoption('--runTask')
    thread = session.config.getoption('--thread')

    # 根据任务参数拆分用例
    if runTask == 'mod':
        # 以模块为粒度进行拆分用例
        """
        {
        "模块1":[用例1，用例2],
        "模块2":[用例1，用例2],
        "模块3":[用例1，用例2]
        }
        """
        # 获取模块
        case_dict = {}
        # 遍历所有的用例
        for case_ in session.items:
            # 获取用例所属的模块
            module = case_.module
            # 判断case_dict是否存在module
            if case_dict.get(module):
                # 将用例添加进去
                case_dict[module].append(case_)
            else:
                # 将模块作为key保存到case_dict中
                case_dict[module] = [case_]
        # 以模块为单位执行测试用例,一个模块一个并发
        with ThreadPoolExecutor(max_workers=int(thread)) as tp:
            for item in case_dict.values():
                tp.submit(run_test,item)
        gevent_list=[]
        for item in case_dict.values():
            """遍历用例使用协程执行"""
            g = gevent.spawn(run_test, item)#创建协程对象
            gevent_list.append(g)
        # 等待协程执行结束
        gevent.joinall(gevent_list)

    return True



def run_test(items):
    """并发执行用例的任务函数
    items包含用例的列表
    """
    for item in items:
        item.ihook.pytest_runtest_protocol(item=item, nextitem=None)
