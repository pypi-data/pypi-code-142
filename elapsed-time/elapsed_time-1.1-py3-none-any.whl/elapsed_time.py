import time

def elapsed(func):
    def wrapper(*args, **kwarg):
        start = time.time()
        exec = func(*args, **kwarg)
        func_name = func.__name__
        end = time.time()
        print(f'Elapsed time of {func_name} function was: {end - start} seconds')
        return exec
    return wrapper