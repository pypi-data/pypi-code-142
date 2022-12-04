# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
═════════════════════════════
@Time   : 2022/11/24 14:31:49
@Author : Rey
@Contact: reyxbo@163.com
@Explain: Rey's decorators
═════════════════════════════
'''


import time
from threading import Thread

from . import rbasic
from .rtype import function, method


def wrap_frame(func: 'function | method') -> 'function':
    '''
    Decorative frame

    Parameters
    ----------
    func: function or method

    Retuens
    -------
    function after decoration

    Demos
    -----
    a)
        @wrap_func
        def func(): ...
        func_ret = func()

    b)  
        def func(): ...
        func = wrap_func(func)
        func_ret = func()
    
    c)
        def func(): ...
        func_ret = wrap_func(func, parameter, ...)
    '''

    rbasic.check_parm(func, function, method)

    def wrap(_func: 'function | method', *args: 'object', **kwargs: 'object') -> 'function | object':
        '''
        Decorative shell
        '''
        
        if args or kwargs:
            func_ret = _func(*args, **kwargs)
            return func_ret
        
        else:
            def wrap_sub(*args: 'object', **kwargs: 'object') -> 'object':
                '''
                Decorative sub shell
                '''

                func_ret = _func(*args, **kwargs)
                return func_ret
            return wrap_sub
    return wrap

def wraps(*wrap_funcs: 'function | method') -> 'function':
    '''
    Batch decorator

    parameters
    ----------
    wrap_funcs: decorator

    Retuens
    -------
    function after decoration

    Demos
    -----
    a)
        @wraps(print_funtime, state_thread)
        def func(): ...
        func_ret = func()

        Same up and down

        @print_funtime
        @state_thread
        def func(): ...
        func_ret = func()

        Same up and down

        def func(): ...
        func = print_funtime(func)
        func = state_thread(func)
        func_ret = func()
    '''

    for element in wrap_funcs: rbasic.check_parm(element, function, method, print_var_name=False)

    for wrap_func in wrap_funcs:
        def wrap(func: 'function | method') -> 'function':
            '''
            Decorative shell
            '''

            def wrap_sub(*args: 'object', **kwargs: 'object') -> 'object':
                '''
                Decorative sub shell
                '''

                func_ret = wrap_func(func, *args, **kwargs)
                return func_ret
            return wrap_sub
        func = wrap
    return wrap

@wrap_frame
def print_runtime(func: 'function | method', *args: 'object', **kwargs: 'object') -> 'function':
    '''
    Print run time of the function
    '''

    rbasic.check_parm(func, function, method)

    start_datetime = rbasic.get_datetime_str()
    start_timestamp = time.time()
    func_ret = func(*args, **kwargs)
    end_datatime = rbasic.get_datetime_str()
    end_timestamp = time.time()
    spend_timestamp = end_timestamp - start_timestamp
    spend_second = int(spend_timestamp)
    print_content = ['Start: %s -> Spend: %ss -> End: %s' % (start_datetime, spend_second, end_datatime)]
    title = func.__name__
    rbasic.print_frame(print_content, title)
    return func_ret

@wrap_frame
def start_thread(func: 'function | method', *args: 'object', daemon: 'bool'=True, **kwargs: 'object') -> 'None':
    '''
    Function start in thread
    '''

    rbasic.check_parm(func, function, method)
    rbasic.check_parm(daemon, bool)

    thread_name = '%s_%s' % (func.__name__, str(int(time.time() * 1000)))
    thread = Thread(target=func, name=thread_name, args=args, kwargs=kwargs)
    thread.daemon = daemon
    thread.start()