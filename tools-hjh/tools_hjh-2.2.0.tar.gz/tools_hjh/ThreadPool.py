# coding:utf-8
import time
import _thread
import threading
from uuid import uuid1


class ThreadPool():
    """ 维护一个线程池 """
    
    def __init__(self, size):
        self.size = size
        self.pool_status = [0]
        self.result_map = {}
        
    def clear(self):
        self.pool_status = [0]
        self.result_map = {}

    def run(self, func, args, kwargs={}):
        """ 主线程命令当前线程池从空闲线程中取一个线程执行给入的方法，如果池满，则主线程等待 """
        if self.pool_status[0] < self.size:
            thread_id = uuid1()
            t = myThread(func, args=args, kwargs=kwargs, thread_id=thread_id, pool_status=self.pool_status, result_map=self.result_map)
            t.start()
            return thread_id
        else:
            while self.pool_status[0] >= self.size:
                time.sleep(0.2)
            return self.run(func, args, kwargs)

    def get_results(self):
        return self.result_map
    
    def get_result(self, num):
        return self.result_map[num]
    
    def clear_result(self):
        self.result_map = {}

    def wait(self):
        """ 主线程等待，直到线程池不存在活动线程 """
        while self.pool_status[0] > 0:
            time.sleep(0.2)


class myThread (threading.Thread):

    def __init__(self, func, args, kwargs, thread_id, pool_status, result_map):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.thread_id = thread_id
        self.pool_status = pool_status
        self.result_map = result_map

    def run(self):
        self.pool_status[0] = self.pool_status[0] + 1
        result = self.func(*self.args, **self.kwargs)
        self.result_map[self.thread_id] = result
        self.pool_status[0] = self.pool_status[0] - 1


class ThreadPool2():
    """ 维护一个线程池 """
    
    def __init__(self, size):
        self.size = size
        self.locks = []
        
    def clear(self):
        self.locks.clear()

    def run(self, func, args, kwargs={}):
        """ 主线程命令当前线程池从空闲线程中取一个线程执行给入的方法，如果池满，则主线程等待 """
        if len(self.locks) < self.size:
            lock = _thread.allocate_lock()
            lock.acquire()
            self.locks.append(lock)
            args = (*args, lock)
            newfunc = self._getnewfunc(func)
            _thread.start_new_thread(newfunc, args, kwargs)
        else:
            while len(self.locks) >= self.size:
                for lock in self.locks:
                    if not lock.locked():
                        self.locks.remove(lock)
                time.sleep(0.2)
            self.run(func, args, kwargs)

    def wait(self):
        """ 主线程等待，直到线程池不存在活动线程 """
        for lock in self.locks:
            while lock.locked():
                time.sleep(0.2)

    def _getnewfunc(self, func):

        def newfunc(*arg, **kwargs):
            try:
                func(*arg[0:-1], **kwargs)
            finally:
                arg[-1].release()

        return newfunc

