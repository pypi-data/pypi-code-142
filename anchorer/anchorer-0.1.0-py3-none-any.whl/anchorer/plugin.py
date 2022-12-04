""""""
import os
import shutil
import sys
from virtualenvwrapper.anchorer import fix
import logging

from virtualenvwrapper.user_scripts import get_path

log = logging.getLogger(__name__)


# can see this is found with `python -m virtualenvwrapper.hook_loader --list pre_mkvirtualenv`
# byt can't see it being used when using mkvirtualenv
def pre_mkvirtualenv(args):
    log.info('adding anchorer to virtualenv - sys.pythonpath and CWD will have symlinks resolved at load time')
    env_name = args[0]
    # get the path to the target virtualenv's site packages
    virtualenv_site_packages = get_path(
        # virtualenvwrapper will have this environ set at the time this hook is called
        '$WORKON_HOME',
        env_name,
        'lib',
        f'python{sys.version_info.major}.{sys.version_info.minor}',
        'site-packages')
    # if hooks were called inside the activated virtualenv, `sysconfig.get_path('platlib')` could have been used instead

    new_module_path = os.path.join(virtualenv_site_packages, '__anchorer.py')
    new_pth_path = os.path.join(virtualenv_site_packages, '__anchorer.pth')
    shutil.copy(fix.__file__, new_module_path)
    with open(new_pth_path, 'w') as pth_file:
        pth_file.write('import __anchorer')
    print(f'added anchorer fixer to {new_pth_path}')
