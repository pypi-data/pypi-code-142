import time

def elapsed(func):
    def wrapper(*args, **kwarg):
        start = time.time()
        exec = func(*args, **kwarg)
        end = time.time()
        func_name = func.__name__
        time = end - start
        unit = 'seconds' if time < 60 else 'minutes'
        print(f'Elapsed time of {func_name} was: {time} {unit}')
        return exec
    return wrapper
