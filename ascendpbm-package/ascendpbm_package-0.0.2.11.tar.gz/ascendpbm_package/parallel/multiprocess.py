from itertools import repeat

def apply_kwargs(fn, kwargs):
    return fn(**kwargs)

# multiprocess wrapers for handling kwargs
def starmap_with_kwargs(pool, fn, kwargs_iter):
    args_for_starmap = zip(repeat(fn), kwargs_iter)
    mp_pool = pool.starmap(apply_kwargs, args_for_starmap)
    return mp_pool

