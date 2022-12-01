# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/utils/nbdev_utils.ipynb.

# %% auto 0
__all__ = ['cd_root', 'nbdev_setup', 'TestRunner', 'md', 'replace_imports', 'get_test_and_library_folders', 'nbdev_build_test',
           'nbdev_build_all', 'nbdev_update_all', 'nbdev_sync']

# %% ../../nbs/utils/nbdev_utils.ipynb 3
__author__ = "Jaume Amores"
__copyright__ = "Copyright 2021, Johnson Controls"
__license__ = "MIT"

# %% ../../nbs/utils/nbdev_utils.ipynb 4
import os
import shutil
import joblib
import re
from pathlib import Path
import socket
from configparser import ConfigParser
from IPython.display import display, Markdown, Latex
from functools import partial

from fastcore.script import *

from .utils import get_norun
from .test_exporter import build_test_nb

# %% ../../nbs/utils/nbdev_utils.ipynb 8
def cd_root (filename='settings.ini'):
    max_count=10
    while not os.path.exists(filename):
        os.chdir('..')
        max_count = max_count - 1
        if max_count <= 0:
            break

# %% ../../nbs/utils/nbdev_utils.ipynb 10
from warnings import filterwarnings

# %% ../../nbs/utils/nbdev_utils.ipynb 11
def nbdev_setup (filename='settings.ini', no_warnings=True):
    if no_warnings:
        filterwarnings("ignore")
    cd_root (filename=filename)
    return get_norun ()

# %% ../../nbs/utils/nbdev_utils.ipynb 14
class TestRunner ():
    def __init__ (self, do_all=False, do_test=None, all_tests=None, tags=None, targets=None,
                  remote_targets=None, load=False, save=True, path_config='config_test/test_names.pk',
                  localhostname=None, show=True):

        if save:
            Path(path_config).parent.mkdir(parents=True, exist_ok=True)

        if load and Path(path_config).exists():
            do_test_, all_tests_, tags_, targets_, remote_targets_, localhostname_ = joblib.load (path_config)
            do_test = do_test_ if do_test is None else do_test
            all_tests = all_tests_ if all_tests is None else all_tests
            tags = tags_ if tags is None else tags
            targets = targets_ if targets is None else targets
            remote_targets = remote_targets_ if remote_targets is None else remote_targets
            localhostname = localhostname_ if localhostname is None else localhostname
        else:
            do_test = [] if do_test is None else do_test
            all_tests = [] if all_tests is None else all_tests
            tags = {} if tags is None else tags
            targets = [] if targets is None else targets
            remote_targets = ['dummy'] if remote_targets is None else remote_targets
            localhostname = 'DataScience-VMs-03' if localhostname is None else localhostname

        if not isinstance(targets, list):
            targets = [targets]

        self.do_test = do_test
        self.all_tests = all_tests
        self.tags = tags
        self.do_all = do_all
        self.targets = targets
        self.save = save
        self.path_config = path_config
        self.hostname = socket.gethostname()
        self.localhostname = localhostname
        self.remote_targets = remote_targets
        self.is_remote = self.localhostname != self.hostname
        self.show = show
        self.storage = {}

    def get_data (self, data_func, *args, store=False, **kwargs):
        name = data_func.__name__
        if name in self.storage:
            data = self.storage[name]
        else:
            data = data_func(*args, **kwargs)
            if store:
                self.storage[name] = data
        return data

    def run (self, test_func, data_func=None, do=None, include=False, debug=False,
            exclude=False, tag=None, show=None, store=False):
        name = test_func.__name__
        show = self.show if show is None else show
        if (name not in self.all_tests) and not exclude:
            self.all_tests.append (name)
        if include and name not in self.do_test:
            self.do_test.append (name)
        if tag is not None:
            if tag in self.tags and name not in self.tags[tag]:
                self.tags[tag].append(name)
            else:
                self.tags[tag] = [name]
        if self.save:
            joblib.dump ([self.do_test, self.all_tests, self.tags, self.targets,
                         self.remote_targets, self.localhostname], self.path_config)
        targets = self.remote_targets if self.is_remote else self.targets
        if do is not None and not do:
            return
        if ((name in self.do_test) or do or (self.do_all and not exclude) or
            ((tag is not None) and (tag in targets)) ):
            if data_func is not None:
                data = self.get_data (data_func, store=store)
                args = [data]
            else:
                args = []
            if debug:
                pdb.runcall (test_func, *args)
            else:
                if show:
                    print (f'running {name}')
                test_func (*args)

# %% ../../nbs/utils/nbdev_utils.ipynb 26
def md (txt, nl=''):
    if 'b' in nl: print ('\n')
    display(Markdown(txt))
    if 'e' in nl: print ('\n')

# %% ../../nbs/utils/nbdev_utils.ipynb 29
def replace_imports (path_file, library_name):
    file = open (path_file, 'rt')
    text = file.read ()
    file.close ()
    text = re.sub (r'from \.+', f'from {library_name}.', text)

    file = open (path_file, 'wt')
    file.write (text)
    file.close ()

# %% ../../nbs/utils/nbdev_utils.ipynb 31
def get_test_and_library_folders (library_name=None, test_folder='tests'):
    from configparser import ConfigParser
    
    cd_root ()
    if (library_name is None) or (test_folder is None):
        config = ConfigParser(delimiters=['='])
        config.read('settings.ini')
        cfg = config['DEFAULT']
    if library_name is None:
        library_name = cfg['lib_name']
    if test_folder is None:
        test_folder = cfg['test_path']
    return library_name, test_folder

# %% ../../nbs/utils/nbdev_utils.ipynb 33
def nbdev_build_test (library_name=None, test_folder='tests'):
    library_name, test_folder = get_test_and_library_folders (library_name=library_name,
                                                              test_folder=test_folder)
    print (f'moving {library_name}/{test_folder} to root path: {os.getcwd()}')
    if os.path.exists (test_folder):
        print (f'{test_folder} exists, removing it')
        shutil.rmtree (test_folder)
    shutil.move (f'{library_name}/{test_folder}', '.')
    for root, dirs, files in os.walk(test_folder, topdown=False):
        for name in files:
            if name.endswith('.py'):
                print (f'replacing imports in {os.path.join(root, name)}')
                replace_imports (os.path.join(root, name), library_name)

# %% ../../nbs/utils/nbdev_utils.ipynb 38
def nbdev_build_all ():
    from nbdev.doclinks import nbdev_export

    build_test_nb ()
    nbdev_export ()
    nbdev_build_test ()

# %% ../../nbs/utils/nbdev_utils.ipynb 40
def _script2notebook_nested_path (fname, dic, silent=False):
    "Put the content of `fname` back in the notebooks it came from."
    import nbformat
    from nbformat.sign import NotebookNotary
    from nbdev.export import split_flags_and_code, read_nb
    from nbdev.imports import get_config
    from nbdev.sync import _split, _deal_loc_import
    from dsblocks.utils.utils import compare_last_part
    
    if os.environ.get('IN_TEST',0): return  # don't export if running tests
    lib_path = get_config().path("lib_path").name
    fname = lib_path / Path(fname)
    with open(fname, encoding='utf8') as f: code = f.read()
    splits = _split(code)
    rel_name = fname.absolute().resolve().relative_to(get_config().path("lib_path"))
    key = str(rel_name.with_suffix(''))
    assert len(splits)==len(dic[key]), f'"{rel_name}" exported from notebooks should have {len(dic[key])} cells but has {len(splits)}.'
    assert all([c1[0]==c2[1]] for c1,c2 in zip(splits, dic[key]))
    splits = [(c2[0],c1[0],c1[1]) for c1,c2 in zip(splits, dic[key])]
    nb_fnames = {get_config().path("nbs_path")/s[1] for s in splits}
    for nb_fname in nb_fnames:
        converted = False
        exception_found = None
        try:
            nb = read_nb(nb_fname)
            for i,f,c in splits:
                c = _deal_loc_import(c, str(fname))
                if compare_last_part (nb_fname, f):
                    try:
                        flags = split_flags_and_code(nb['cells'][i], str)[0]
                        nb['cells'][i]['source'] = flags + '\n' + c.replace('', '')
                        converted = True
                    except Exception as e:
                        exception_found = e
            if not converted:
                print (f"Could not convert {nb_fname}, exception: {exception_found}")
            NotebookNotary().sign(nb)
            nbformat.write(nb, str(nb_fname), version=4)
        except Exception as e:
            print (f'notebook {nb_fname} could not be read: {e}')

    if not silent: print(f"Converted {rel_name}.")

# %% ../../nbs/utils/nbdev_utils.ipynb 41
def nbdev_update_all (silent=False, library_name=None, test_folder='tests',
                      ignore_tests=False):
    from nbdev.export import notebook2script, get_nbdev_module
    from fastcore.foundation import L
    
    library_name, test_folder = get_test_and_library_folders (library_name=library_name,
                                                              test_folder=test_folder)
    if os.path.exists (test_folder):
        if os.path.exists (f'{library_name}/{test_folder}') and not ignore_tests:
            raise RuntimeError (f'both {test_folder} and {library_name}/{test_folder} exists\n'
                                'consolidate them into one before proceeding, or pass ignore_tests=True.')
        shutil.move (test_folder, f'{library_name}/{test_folder}')
    dic = notebook2script(silent=True, to_dict=True)
    exported = get_nbdev_module().modules
    if os.path.exists (f'{library_name}/{test_folder}'):
        files = L (exported)
    else:
        files = L([x for x in exported if not x.startswith ('tests')])
    files.map(partial(_script2notebook_nested_path, dic=dic, silent=silent))

# %% ../../nbs/utils/nbdev_utils.ipynb 45
def nbdev_sync ():
    from nbdev.export2html import nbdev_build_lib
    
    nbdev_update_all ()
    nbdev_build_lib ()
    nbdev_build_test ()
