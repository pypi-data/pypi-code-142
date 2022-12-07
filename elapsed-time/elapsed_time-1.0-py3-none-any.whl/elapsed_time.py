import time

def elapsed(func):
    def wrapper(*args, **kwarg):
        start = time.time()
        exec = func(*args, **kwarg)
        end = time.time()
        func_name = func.__name__
        rtime = end - start
        unit = 'seconds' if rtime < 60 else 'minutes'
        print(f'Elapsed time of {func_name} function was: {rtime} {unit}')
        return exec
    return wrapper