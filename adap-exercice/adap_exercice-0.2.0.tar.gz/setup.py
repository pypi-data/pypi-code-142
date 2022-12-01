# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adap_exercice']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2,<4.0.0', 'sympy>=1.11.1,<2.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['adap-exercice = adap_exercice.main:app']}

setup_kwargs = {
    'name': 'adap-exercice',
    'version': '0.2.0',
    'description': 'Library to create a tex and pdf file of an exercice of economics which can be modified by the user',
    'long_description': '# Exercice Adaptatif\n\nCe package permet la résolution d\'un exercice. Celui-ci permet aussi de modifier les paramètres de l\'exercice pour laisser plus de liberté à l\'utilisateur. Les réponses données par le fichier s\'adapteront alors aux paramètres.\n\nL\'exécution du package permet la création d\'un fichier PDF à l\'aide du langage LaTeX. Le fichier TeX est lui aussi récupérable pour une modification plus précise du fichier.\n\n---\n## Exercice \nA monopoly operates for two periods and\nproduces a homogenous good whose quality is either high or low (the monopoly cannot choose the quality of the good). \n\nIn the first period, the quality of the good is unobserved by consumers and their demand is $q_1$ = $s_1$ − $p_1$, where $s_1$ is the perceived quality of the good and p1 is the price in period 1. \n\nIn the second period, the quality of the good becomes common knowledge and the demand for the good is $q_2$ = 4 − $p_2$ if the quality is high and $q_2$ = 2 − $p_2$ if the quality is low, where $p_2$ is the price in the second period. \n\nThe\nper unit cost of production is 1 in the first period, and 1 − $\\gamma q_1$ in the second period, where $\\gamma$ is a positive constant that reflects a learning-by-doing effect : the more the firm produces in period 1, the lower is its per unit cost in period 2. Assume that $\\gamma$ = $\\frac{1}{4}$ if the monopoly produces a high quality product and $\\gamma$ = $\\frac{1}{2}$ if the monopoly produces a low quality product. For simplicity, assume that there is no discounting.\n\n### Questions :\n\n1. Solve the monopoly’s problem in period 2 and compute the monopoly’s profit at the optimum, taking $q_1$ as given (recall that $q_1$ determines the per-unit cost of production in period 2).\n\n2. Write out the sum of the monopoly profits in periods 1 and 2 as a function of $p_1$, given the monopoly type, assuming that consumers believe that (1) $s_1$ = 4 and (2) $s_1$ = 2.\n\n3. Now suppose that in period 1 the monopoly chooses a price, $p_1$, and a level of uninformative advertising, A. Solve for the strategy of a low type monopoly in a separating equilibrium.\n\n4. Let A($p_1$) define, for each period 1 price $p_1$, the minimal amount of advertising required by a high quality monopoly in order to deter a low quality monopoly from mimicking it. Given your answers to parts (2) and (3), compute $A(p_1)$ and show it in a figure. Moreover, compute the prices at which $A(p_1)$ crosses the horizontal axis.Explain the meaning of these crossing points.\n\n5. Solve for the price that a high quality monopoly will charge in a Pareto undominated separating equilibrium (one where a high quality monopoly advertises just enough to induce separation, or more precisely, one where consumers believe that the monopoly must be of a high quality if they observe a pair $(p_1,A)$ which is a weakly dominated strategy for a low quality monopoly) and compute the amount of advertising that it will choose.\n\n6. Compare your answer in part (5) to the optimal strategy of a high quality monopoly in the full information case (the case where the quality is common knowledge even in period 1). Does the monopoly underprice or overprice in equilibrium, relative to the full information case ? Explain why the price distortion could serve as a signal for quality in this particular case.\n\n---\n## Présentation du module\n\n### Installation\n\nIl y a deux manières pour installer ce module :\n\n1. Installer le package depuis PiPy avec `pip` :\n```sh\npy -m pip install adap_exercice\n```\n\n2. Installer le module à partir du répertoire téléchargé sur GitHub (en utilisant votre propre chemin où se situe le dossier) :\n\n```sh\npy -m pip install "C:/Users/Username/Downloads/adap_exercice"\n```\n### Fonctionnement\n\nCe module contient deux fonctions utilisables en ligne de commandes par l\'utilisateur :\n\n1. La première permet d\'obtenir la version originale de la correction de l\'exercice, tous les calculs étant fait de manière symbolique grâce au module `sympy`.\n\n```sh\npy -m adap_exercice original\n```\n\n2. La seconde permet de modifier les paramètres au choix de l\'utilisateur à l\'aide d\'un prompt :\n    1. Les valeurs de qualité haute et basse $s_1$ et $s_2$.\n    2. Les valeurs des $\\gamma$.\n\n<p align="center">\n\n![](command_modify.gif)\n\n</p>\n\nEnfin, la commande :\n\n```sh\npy -m adap_exercice --help\n```\nElle permet d\'obtenir les différentes informations sur le package, ainsi que l\'auto-complétion et les descriptions des commandes.\n### Fichiers\n\nLe fichiers PDF s\'ouvrira normalement automatiquement dans une fenêtre. Il est cependant possible de récupérer les deux fichiers dans le dossier `C:/Users/Username`.',
    'author': 'Mathieu',
    'author_email': 'mathieuveron@outlook.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
