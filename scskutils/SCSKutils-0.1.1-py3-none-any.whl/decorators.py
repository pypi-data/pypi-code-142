import time 

def timeit(f):
    def wrapper(*args,**kwargs):
        start = time.time()
        rv = f(*args,**kwargs)
        end = time.time()
        total = end-start
        print(f'time taken for function {f.__name__}: {total}')
        return rv
    return wrapper