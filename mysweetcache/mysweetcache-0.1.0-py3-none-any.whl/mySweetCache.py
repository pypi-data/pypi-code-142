import os

import numpy as np

from .utils import use_par

SETUP = {
    "CACHE_FILES": ".MScache_files",
    "MSC_USE_CACHE": True,
}


def make_cache_dir(_CACHE_FILES=SETUP["CACHE_FILES"]):
    if _CACHE_FILES not in os.listdir():
        os.mkdir(_CACHE_FILES)

def read_cache(MSC_name: str, cache_folder: str=None):
    """File to fast read MSC.

    Args:
        MSC_name (str): cache key to read.
        cache_folder (str, optional): Cache will be read from .MScache_files from cache_folder.
        If cache_folder is None is used current folder. Defaults to None.

    Raises:
        NameError: If this cache don't exist.

    Returns:
        _type_: _description_
    """    
    if cache_folder is None:
        cache_folder = SETUP["CACHE_FILES"]
    cache_folder += SETUP["CACHE_FILES"]
    if not os.path.exists(os.sep.join([cache_folder, MSC_name])):
        raise NameError(f"{MSC_name} cache not exist")

    @cache(MSC_name)
    def NobodyExpectsTheSpanishInquisition():
        return
    return NobodyExpectsTheSpanishInquisition(use_cache=True)
    

def cache(MSC_name=None, *, dim=2):
    """Wrapper add possibility caching function result to wrapped function

    Wrapper add possibility caching function result to wrapped function.
    If file MSC_name.txt exist in _CACHE_FILES
        wraped function return cache from right cache.
    else
        make new cache
    Wrapper add optional argument 'use_cache'.
    If use_cache == False
        cache will overwrite.

    Args:
        MSC_name (string, optional): name of cache (key to identify)
            If MSC_name is None then stay __name__ of cached function. Defaults to None.

    Returns:
        fun: Function with cache functionality.
    """
    if SETUP["CACHE_FILES"] not in os.listdir():
        make_cache_dir(SETUP["CACHE_FILES"])

    @use_par(MSC_name)
    def wrapper(MSC_name, fun):
        if MSC_name is None:
            MSC_name = fun.__name__

        def TO_RETURN(*args, use_cache=SETUP["MSC_USE_CACHE"]):
            if MSC_name in os.listdir(SETUP["CACHE_FILES"]) and use_cache:
                return read_from_file(os.sep.join([SETUP["CACHE_FILES"], MSC_name]))
            ret = fun(*args)
            save_to_file(ret, os.sep.join([SETUP["CACHE_FILES"], MSC_name]), MSC_name)
            return ret

        TO_RETURN.__name__ = fun.__name__
        return TO_RETURN

    return wrapper


def save_to_file(lists, file_name, header="", sep_in_data=","):
    """Funkcja zapisuje podane estymowane dane do późniejszego wykożystania.
    Aby je późnije odczytać należy użyć funkcji read_from_file.
    Args:
        lists (_type_): lista list plików do zapisania. najlepiej dwuwymiarowy np.array
        file_name (string): azwa pliku, w którym mają być zapisane dane
        header (str, optional): pierwsza linijka stanowiąca opis danych,
            ignorowana później, przy odczytywaniu. Defaults to "".
        sep_in_data (str, optional): znak jakim mają być oddzielane dane. Defaults to ",".
    """
    ret = header + "\n"
    for el in lists:
        for i in el:
            ret += str(i) + sep_in_data
        ret = ret[:-1] + "\n"
    try:
        with open(file_name, "w") as f:
            f.write(ret)
    except FileNotFoundError:
        old = os.getcwd()
        path = file_name.split(os.sep)[:-1]
        for i in path:
            os.mkdir(i)
            os.chdir(i)
        os.chdir(old)
        with open(file_name, "w") as f:
            f.write(ret)


def read_from_file(file_name, sep_in_data=",", show_warr=True):
    """Funkcja odczytuje zapisane wczesniej dane funkcją save_to_file.
    Args:
        file_name (string): nazwa pliku, z którego mają być odczytane dane
        sep_in_data (str, optional): znak jakim mają być oddzielane dane. Defaults to ",".
        show_warr (bool, optional): jeżeli true, funkcja wyświetli ostrzerzenie
            jeżeli danych nie uda się zamienić na liczby
            i zwroci je jako str. Defaults to True.
    Returns:
        np.array: dwuwymiarowa macierz
    """
    with open(file_name, "r") as f:
        data = f.read().split("\n")
    for i in range(1, len(data)):
        if data[i] == "":
            data = data[:i]
            break
        try:
            data[i] = [float(k) for k in data[i].split(sep_in_data)]
        except ValueError:
            data[i] = data[i].split(sep_in_data)
            if show_warr is False:
                continue
            print("Warring! Data was read as string.")

    return np.array(data[1:])
