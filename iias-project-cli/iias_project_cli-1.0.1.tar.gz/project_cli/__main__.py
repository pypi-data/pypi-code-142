import argparse
import os
import re
from project_cli.templates import (get_main, get_init, get_readme, get_gitignore, get_credentials)

if os.name == 'nt':
    ENV_USER = 'USERNAME'
else:
    ENV_USER = 'USER'


_DEFAULT_NAME = 'projet iias'
_DEFAULT_DESCRIPTION = 'Projet IA pour l\'IIAS'
_DEFAULT_VERSION = '0.1.0'
_DEFAULT_AUTHOR = os.getenv(ENV_USER)
_DEFAULT_RUNNABLE = 'yes'
_DEFAULT_CORRECT = 'oui'

try:
    input_ = raw_input  # Python2.7
except NameError:
    input_ = input  # Python3.+

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

    name = _get_input('Nom du projet', _DEFAULT_NAME, '[a-zA-Z_]\w*',
                      'Le nom du projet doit être un mot; doit commencer par une ' +\
                      'lettre ou un underscore et ne doit contenir que des lettres, ' +\
                      'des underscores et des chiffres pour le reste.')
    description = _get_input('Description', _DEFAULT_DESCRIPTION)
    author = _get_input('Auteur', _DEFAULT_AUTHOR)

    print('')
    print(bcolors.HEADER + 'Vision de la configuration' + bcolors.ENDC)
    print(bcolors.HEADER + '--------------' + bcolors.ENDC)
    print(bcolors.HEADER + 'Nom du projet:    %s' % name + bcolors.ENDC)
    print(bcolors.HEADER + 'Description:      %s' % description + bcolors.ENDC)
    print(bcolors.HEADER + 'Auteur:           %s' % author + bcolors.ENDC)
    print('')
    correct = _is_yes(_get_input('Est-ce correct ?', _DEFAULT_CORRECT))
    if not correct:
        print()
        return _get_user_inputs()
    return name, description, author


def _setup(name, description, version):
    print('Création du projet en cours..')

    main_package = name
    source_package = name + '/src'
    scripts_package = source_package + '/scripts'
    notebook_package = main_package + '/notebooks'
    lib_package = main_package + '/libs'
    data_package = main_package + '/data'
    assets_package = main_package + '/assets'

    os.makedirs(main_package, exist_ok=True)
    os.makedirs(source_package, exist_ok=True)
    os.makedirs(scripts_package, exist_ok=True)
    os.makedirs(notebook_package, exist_ok=True)
    os.makedirs(lib_package, exist_ok=True)
    os.makedirs(data_package, exist_ok=True)
    os.makedirs(assets_package, exist_ok=True)

    # root
    _create_file('README.md', get_readme(name, description), main_package)
    _create_file('.gitignore', get_gitignore(), main_package)
    _create_file('credentials.yml', get_credentials(), main_package)

    # script
    _create_file('__init__.py', get_init(), scripts_package)
    _create_file('__main__.py', get_main(name), scripts_package)

    print('\n' + bcolors.OKCYAN + 'Projet ' + name + ' créé avec succés ! 🎉' + bcolors.ENDC)


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
