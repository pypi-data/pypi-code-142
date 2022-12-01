BR = '\n'


def get_init():
    return ''

def get_credentials():
    return 'easily:' + BR \
           + '  test:' + BR \
           + '    host: exemple' + BR \
           + '    port: 1111' + BR \
           + '    user: exemple' + BR \
           + '    password: exemple' + BR \
           + '  production:' + BR \
           + '    host: exemple' + BR \
           + '    port: 1111' + BR \
           + '    user: exemple' + BR \
           + '    password: exemple'


def get_main(name):
    return 'def main():' + BR \
           + '    # Votre super code ici..' + BR \
           + BR \
           + BR \
           + "if __name__ == '__main__':" + BR \
           + '    main()' + BR


def get_readme(name, description):
    return '# ' + name + BR \
           + description + BR \
           + BR \
           + '***' + BR \
           + '## 🔧 1 - Installation' + BR \
           + BR \
           + 'Vous aurez besoin des prérequis des outils suivant :' + BR \
           + BR \
           + '- Python 3 ([lien](https://www.python.org/downloads/))' + BR \
           + BR \
           + 'Une fois que tout est installé et configuré :' + BR \
           + BR \
           + '- Editer le fichier credentials.yml pour les accès au bases de données X' + BR \
           + BR \
           + '***' + BR \
           + '## 🚀 2 - Lancement' + BR \
           + BR \
           + '- Lancer à la racine `python3 src/script/__main__.py`' + BR \
           + BR \
           + '***' + BR \
           + '## 💡 3 - Informations générales' + BR \
           + BR \
           + 'Structures des fichiers : ' + BR \
           + BR \
           + '- src/scripts/ : Contients les fichiers de scripts python' + BR \
           + '- notbooks/ : Contients les notebooks' + BR \
           + '- libs/ : Contients les librairies python' + BR \
           + '- data/ : Contients les fichiers base de données (git-ignoré)' + BR \
           + '- assets/ : Contients les différents fichiers SQL, JSON, XML..' + BR \
           + BR \
           + '***' + BR \
           + '## 📌 4 - Outils et packages utilisés' + BR \
           + BR \
           + '- (à completer) Nom de l\'outil 1 (version de l\'outil) ([lien doc](https://lien_vers_la_doc))' + BR \
           + BR \
           + '***' + BR \
           + '## 💪 5 -  Crédits' + BR \
           + BR \
           + '- (à completer) Nom prénom' + BR \
           + BR


def get_gitignore():
  return '/data/*' + BR \
         + 'credentials.yml'

  