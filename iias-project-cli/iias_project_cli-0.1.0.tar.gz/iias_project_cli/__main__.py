import argparse
import os
import re
from project_cli.templates import (get_main, get_init, get_readme, get_setup)

if os.name == 'nt':
    ENV_USER = 'USERNAME'
else:
    ENV_USER = 'USER'


_DEFAULT_NAME = os.getcwd().split(os.sep)[-1]
_DEFAULT_DESCRIPTION = 'A Python %s' % _DEFAULT_NAME
_DEFAULT_VERSION = '0.1.0'
_DEFAULT_AUTHOR = os.getenv(ENV_USER)
_DEFAULT_RUNNABLE = 'yes'
_DEFAULT_CORRECT = 'yes'

try:
    input_ = raw_input  # Python2.7
except NameError:
    input_ = input  # Python3.+


def _is_yes(user_input):
    return user_input.lower() in ('yes', 'y', 'o', 'oui', 'ok')


def _get_input(message, default, regex=None, requirements=None):
    user_input = input_('%s (%s) ' % (message, default)) or default
    if regex:
        match = re.match(regex, user_input)
        if not match or match.group(0) != user_input:
            print('Invalid input. %s' % requirements)
            print('')
            return _get_input(message, default, regex, requirements)
    return user_input


def _get_user_inputs():

    name = _get_input('Project name', _DEFAULT_NAME, '[a-zA-Z_]\w*',
                      'A project name must be a word; it must start with a ' +\
                      'letter or underscore and may contain only letters, ' +\
                      'underscores and numbers in the remainder.')

    description = _get_input('Description', 'A Python %s' % name)

    version = _get_input('Initial version', _DEFAULT_VERSION,
                         '[0-9]\.[0-9]\.[0-9]',
                         'A version must have the form: x.y.z where x, y ' +\
                         'and z are all whole numbers.')

    author = _get_input('Author', _DEFAULT_AUTHOR)

    runnable = _is_yes(_get_input('Is the project runnable?',
                                  _DEFAULT_RUNNABLE))

    print('')
    print('Setup overview')
    print('--------------')
    print('Project name:    %s' % name)
    print('Description:     %s' % description)
    print('Initial version: %s' % version)
    print('Author:          %s' % author)
    print('Runnable:        %s' % ('yes' if runnable else 'no'))
    print('')
    correct = _is_yes(_get_input('Is this correct?', _DEFAULT_RUNNABLE))
    if not correct:
        print()
        return _get_user_inputs()
    return name, description, version, author, runnable


def _setup(name, description, version, author, runnable):
    print('Setting up project now')

    main_package = name
    source_package = name + '/src'
    scripts_package = main_package + source_package + '/scripts'
    notebook_package = main_package + '/notebook'
    lib_package = main_package + '/libs'
    data_package = main_package + '/data'

    os.makedirs(main_package, exist_ok=True)
    os.makedirs(source_package, exist_ok=True)
    os.makedirs(scripts_package, exist_ok=True)
    os.makedirs(notebook_package, exist_ok=True)
    os.makedirs(lib_package, exist_ok=True)
    os.makedirs(data_package, exist_ok=True)

    # root
    _create_file('README.md', get_readme(name, description), main_package)
    _create_file('setup.py', get_setup(name, version, author, description,
                                       runnable), main_package)
    _create_file('.gitignore', get_gitignore(), main_package)

    # script
    _create_file('__init__.py', get_init(), scripts_package)
    _create_file('__main__.py', get_main(name), scripts_package)


def _create_file(fname, content, pname=None):
    fpath = '%s/%s' % (pname, fname) if pname else fname
    with open(fpath, 'w+') as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--yes', action='store_true',
                        help="Say 'yes' to all prompts")
    args = parser.parse_known_args()[0]

    defaults = (_DEFAULT_NAME, _DEFAULT_DESCRIPTION, _DEFAULT_VERSION,
                _DEFAULT_AUTHOR, _DEFAULT_RUNNABLE)
    inputs = defaults if args.yes else _get_user_inputs()
    _setup(*inputs)


if __name__ == '__main__':
    main()
