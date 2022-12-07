import inspect
from collections import OrderedDict

__injection_data = {}


def get_hash(path: str, *args, **kwargs):
    data = frozenset(OrderedDict(kwargs).items())
    return hash((path, *args, data))

def mock_dependency(depend, newmock, *args, **kwargs):
    path = inspect.getfile(depend)
    name = depend.__name__
    
    hash = f'{path}::{name}'
    hash = get_hash(hash, *args, **kwargs)
    
    __injection_data[hash] = newmock


def get_dependency(depend, *args, **kwargs):
    path = inspect.getfile(depend)
    name = depend.__name__
    
    hash = f'{path}::{name}'
    hash = get_hash(hash, *args, **kwargs)
    
    hasil = __injection_data.get(hash)
    if hasil == None:
        hasil = depend(*args, **kwargs)
        __injection_data[hash] = hasil
    
    return hasil

if __name__ == '__main__':
    
    class Repo:
        def __init__(self) -> None:
            print('init')
    
    def name():
        print('asdasd')
        return 'test'
    
    def get(close, name: str = get_dependency(Repo)):
        return name
    
    
    # get()
    # get()
    print('asdasd-----')
    hasil = inspect.signature(get).parameters['close']
    print(hasil)

