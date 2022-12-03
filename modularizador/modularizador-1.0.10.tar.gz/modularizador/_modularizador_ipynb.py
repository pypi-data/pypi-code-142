import os


script = '''# Modularizador 
import io, os, sys, types 
from IPython import get_ipython 
from nbformat import read 
from IPython.core.interactiveshell import InteractiveShell 
def find_notebook(fullname, path=None): 
    # find a notebook, given its fully qualified name and an optional path 
    # This turns "foo.bar" into "foo/bar.ipynb" 
    # and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar 
    # does not exist. 
    name = fullname.rsplit('.', 1)[-1] 
    if not path: 
        path = [''] 
    for d in path: 
        nb_path = os.path.join(d, name + ".ipynb") 
        if os.path.isfile(nb_path): 
            return nb_path 
        # let import Notebook_Name find "Notebook Name.ipynb" 
        nb_path = nb_path.replace("_", " ") 
        if os.path.isfile(nb_path): 
            return nb_path 
class NotebookLoader(object): 
    """Module Loader for Jupyter Notebooks""" 
    def __init__(self, path=None): 
        self.shell = InteractiveShell.instance() 
        self.path = path 
    def load_module(self, fullname): 
        """import a notebook as a module""" 
        path = find_notebook(fullname, self.path) 
        # load the notebook object 
        with io.open(path, 'r', encoding='utf-8') as f: 
            nb = read(f, 4) 
        # create the module and add it to sys.modules 
        # if name in sys.modules: 
        #    return sys.modules[name] 
        mod = types.ModuleType(fullname) 
        mod.__file__ = path 
        mod.__loader__ = self 
        mod.__dict__['get_ipython'] = get_ipython 
        sys.modules[fullname] = mod 
        # extra work to ensure that magics that would affect the user_ns 
        # actually affect the notebook module's ns 
        save_user_ns = self.shell.user_ns 
        self.shell.user_ns = mod.__dict__ 
        try: 
          for cell in nb.cells: 
            if cell.cell_type == 'code': 
                # transform the input to executable Python 
                code = self.shell.input_transformer_manager.transform_cell(cell.source) 
                # run the code in themodule 
                exec(code, mod.__dict__) 
        finally: 
            self.shell.user_ns = save_user_ns 
        return mod 
class NotebookFinder(object): 
    """Module finder that locates Jupyter Notebooks""" 
    def __init__(self): 
        self.loaders = {} 
    def find_module(self, fullname, path=None): 
        nb_path = find_notebook(fullname, path) 
        if not nb_path: 
            return 
        key = path 
        if path: 
            # lists aren't hashable 
            key = os.path.sep.join(path) 
        if key not in self.loaders: 
            self.loaders[key] = NotebookLoader(path) 
        return self.loaders[key] 
sys.meta_path.append(NotebookFinder()) 
# print('Modularizador carregado. Você já pode importar arquivos .ipynb.') '''
nome_do_arquivo = 'modularizador.py'
startup_folder = get_ipython().profile_dir.startup_dir
path = f'{startup_folder}\\{nome_do_arquivo}'

def ativa():
    ja_existia = _arquivo_ja_existe()
    with open(f'{path}', 'w', encoding='utf-8') as f:
        f.write(script)
    if ja_existia:
        print(f'{nome_do_arquivo} já existia e foi sobrescrito em {startup_folder}.')
    else:
        print(f'{nome_do_arquivo} inserido em {startup_folder}.')

def desativa():
    if _arquivo_ja_existe():
        os.remove(path)
        print(f'{nome_do_arquivo} removido de {startup_folder}.')
    else:
        print(f'{nome_do_arquivo} já não existia em {startup_folder}.')

def _arquivo_ja_existe():
    return os.path.exists(path)

def status_startup():
    if _arquivo_ja_existe():
        return('Modularizador ativo na pasta startup do ipython.')
    else:
        return('Não existe modularizador ativo na pasta startup do ipython.')        
        
exec(script)