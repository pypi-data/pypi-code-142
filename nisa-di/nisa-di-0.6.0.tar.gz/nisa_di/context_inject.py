import asyncio
import inspect
import functools
from contextvars import ContextVar, copy_context
from hashlib import md5
from collections import OrderedDict
import pickle

inject_context: ContextVar[dict] = ContextVar('Context injection nisa di')

def get_hash(path: str, *args, **kwargs):
    data = frozenset(OrderedDict(kwargs).items())
    return hash((path, *args, data))


def run_in_new_context(callable, *args, **kwarg):
    context = copy_context()
    
    if asyncio.iscoroutinefunction(callable):
        @functools.wraps(callable)
        async def wrapper(*warg, **wkwarg):
            
            inject_context.set({})
            return await callable(*warg, **wkwarg)
    else:
    
        @functools.wraps(callable)
        def wrapper(*warg, **wkwarg):
            
            inject_context.set({})
            return callable(*warg, **wkwarg)
    
    return context.run(wrapper, *args, **kwarg)


def get_context_dependency(depend, *args, **kwargs):
    injection_data = inject_context.get()
    
    
    path = inspect.getfile(depend)
    name = depend.__name__
    
    hash = f'{path}::{name}'
    hash = get_hash(hash, *args, **kwargs)
    
    hasil = injection_data.get(hash)
    if hasil == None:
        if asyncio.iscoroutinefunction(depend):
            hasil = asyncio.create_task(depend(*args, **kwargs))
        else:
            hasil = depend(*args, **kwargs)
        injection_data[hash] = hasil
    
    return hasil