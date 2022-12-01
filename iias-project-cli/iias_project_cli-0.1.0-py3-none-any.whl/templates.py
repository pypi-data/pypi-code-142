BR = '\n'


def get_init():
    return ''


def get_main(name):
    return 'def main():' + BR \
           + BR \
           + BR \
           + "if __name__ == '__main__':" + BR \
           + '    main()' + BR


def get_readme(name, description, runnable):
    return '# ' + name + BR \
           + description + BR \
           + BR \
           + '***' + BR \
           + '## 🔧 1 - Installation' + BR \
           + BR \
           + 'Vous aurez besoin des prérequis des outils suivant :' + BR \
           + '- Nom outil 1 ([lien](http://google.fr))' + BR \
           + '- ...' + BR \
           + BR \
           + 'Une fois que tout est installé et configuré :' + BR \
           + BR \
           + '- Lancer `ma commande`' + BR \
           + '- Cloner le projet' + BR \
           + '- Dans le répertoire exemple/ : `install exemple`' + BR \
           + '- ...' + BR \
           + BR \
           + '***' + BR \
           + '## 🚀 2 - Lancement' + BR \
           + BR \
           + '- Lancer le service machin : `service machin start`' + BR \
           + '- Lancer le truc : dans le répertoire truc/ : `run truc`' + BR \
           + '- ...' + BR \
           + BR \
           + '***' + BR \
           + '## 💡 3 - Informations générales' + BR \
           + BR \
           + '- Information 1' + BR \
           + '- ...' + BR \
           + BR \
           + '***' + BR \
           + '## 📌 4 - Outils et packages utilisés' + BR \
           + BR \
           + "- Nom de l'outil 1 (version de l'outil) ([lien doc](https://lien_vers_la_doc))" + BR \
           + '- ...' + BR \
           + BR \
           + '***' + BR \
           + '## 💪 5 -  Crédits' + BR \
           + BR \
           + '- Nom prénom 1' + BR \
           + '- ...' + BR \
           + BR \


def get_setup(name, version, author, description, runnable):
    result = '"""This is the installation toolset for this project."""' + BR \
             + "from setuptools import setup, find_packages" + BR \
             + BR \
             + "with open('README.rst', 'r') as fh:" + BR \
             + "    long_description = fh.read()" + BR \
             + BR \
             + "setup(name='" + name + "'," + BR \
             + "      version='" + version + "'," + BR \
             + "      author='" + author + "'," + BR \
             + "      description='" + description + "'," + BR \
             + "      long_description=long_description," + BR \
             + "      packages=find_packages(exclude=('tests',))"
    if runnable:
        result += "," + BR \
                  + "      entry_points={" + BR \
                  + "          'console_scripts': [" + BR \
                  + "              '" + name + " = " + name + ".__main__:main'" \
                  + BR \
                  + "          ]" + BR \
                  + "      }"
    result += ")" + BR
    return result


def get_gitignore():
  return '/data/*' + BR \