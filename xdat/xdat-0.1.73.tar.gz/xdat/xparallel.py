from tqdm import tqdm
from joblib import Parallel, delayed


def x_on_iter(llist, func, n_jobs=-1):
    all_items = Parallel(n_jobs=n_jobs)(delayed(func)(i) for i in tqdm(llist, total=len(llist)))
    return all_items


def x_on_keys(ddict, keys, func, n_jobs=-1):
    all_keys = list(keys)
    all_vals = Parallel(n_jobs=n_jobs)(delayed(func)(ddict[k]) for k in tqdm(all_keys, total=len(all_keys)))
    new_dict = dict(zip(all_keys, all_vals))
    return new_dict


def x_reduce(llist, calc_func, reduce_func=max, n_jobs=-1):
    vals = x_on_iter(llist, calc_func, n_jobs=n_jobs)
    vals = [v for v in vals if v is not None]
    val = reduce_func(vals)
    return val
