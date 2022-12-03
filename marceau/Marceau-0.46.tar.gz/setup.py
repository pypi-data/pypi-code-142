from setuptools import setup

# with open('C:\Lyon\Programmation\Canada\MarceauCossette\README.md') as fp:
#     long_desc = fp.read()
long_desc="# Marceau \n# Overview\nThis module provide a fast and efficient way to compute the [Panjer's Algorithm][panjer] in a Python shell.\n\n## Usage\n\nIn the following paragraphs, I am going to describe how you can get and use Marceau for your own projects.\n\n###  Getting it\n\nTo download Marceau, either from this [Github][git-repo-url] repository or simply use Pypi via pip.\n```sh\npip install Marceau\n```\n\n### Module\n\nMarceau uses two modules to work properly, you need to make sure to have the following on your computer:\n\n- [Scipy.stats] - Used to generate probability mass function from discrete distributions.\n- [Numpy] - For usefull calculations.\n\nYou are then ready to use it:\n```sh\nimport Marceau\n```\n\n### Using it\n\nThe class Cossette built in the Marceau module calculate the Probability Density Function (PDF) and the Cumulative Distribution Function (CDF) of a Compound Distribution.\n\n```sh\nfrom Marceau import Cossette\n```\n\nThe command\n```sh\nCossette.help()\n```\n\nand\n```sh\nCossette.example()\n```\n\nprovide respectivly an brief help and two example of the following algorithm.\n\n## Panjer's Algorithm\n\nWe are interested in the compound random variable: $$X=\\sum_{i=1}^{N}B_{i}$$\n\nwhere:\n* $M$ is a frequence random variable from [Panjer-Katz] probability distribution family, otherwise known as (a,b, $0$)[class of distributions]. For $M=0$ we have $X=0$.\n* $\\underline{B}={B_{k},k\\in\\mathbb{N}^{+}}$ are positive i.i.d random variable defined on $\\mathbb{N}$.\n* $\\underline{B}$ and $M$ are independant.\n\nTherefore, the random variable $X$ has value in $\\mathbb{N}$. And the Panjer's recursive method works as follow:\n* If $B_{i}$ are distributed on a lattice $h\\mathbb{N}$ with latticewidth $h>0$. $B\\in$\\{ $0$, $1h$, $2h$,....\\}\n* We have $X\\in$ $A_{h}$=\\{ $0$, $1h$, $2h$,....\\}\n* With $W_{M}$ beeing the probability generating function of M, we compute $f_{X}(0)=W_{M}(f_{B}(0))$\n* The Panjer's recursive relation states for $k>0$: $$f_{X}(kh)=\\frac{1}{1-af_{B}(0)}\\sum_{i=1}^{k}(a+b\\frac{jh}{kh})f_{B}(jh)\\times f_{X}((k-j)h)$$\n\n\n### Implementation\n\nIn order to compute the Panjer's Algorithm, we need to enter the following feature to our class Cossette.\n\n| Arguments | Data Type| Description| \n| ------ | ------ | ------ |\n| k | a positive integer| the epoch of recursion to find X distribution |\n| h | a strictly positive integer|  the latticewidth of $B_{i}$ distribution |\n| parameters | a list of length $1$ (poisson or geometric) or $2$ (binomial or negative binomial)| the parameters for the $X$ compound distribution |\n| method | a string with value 'Binomial', 'NegBinomial', 'Geometric' or 'Poisson'| the law of $X$ compound distribution |\n| fb | a list of length $k+1$ | this correspond to the $f_{B}$ values when those are given, default value is an empty list |\n| generat or\\_param| a list of length $1$ (poisson or geometric) or $2$ (binomial or negative binomial) | the parameters of the $B$ distribution, only needed if $f_{B}$ is empty, default value is empty|\n| generator\\_method|   a string with value 'Binomial', 'NegBinomial', 'Geometric' or 'Poisson' | the law of $B$ distribution, only needed if $f_{B}$ is empty, default value is empty |\n\n\n## Example\n#### Example 1\nLet $X\\sim PComp(\\lambda=2,F_{B}),$ with $B\\sim Bin(10,0.4)$.\n\nWe implement the following\n\n```sh\nmodel= Marceau.Cossette(k=10,parameters=[2],method='Poisson',generator_method='Binomial',generator_param=[10,0.4]) \n```\nAnd we get our output with the call model.panjer():\n```sh\nmodel.panjer()\n >>> f(10*1)=0.05434563071580669 \n F(10*1)=0.6980136730471336 \n ```\n#### Example 2 \n\nLet $X\\sim PComp(\\lambda=2,F_{B}),$ with $B \\in$ \\{ $1000$, $2000$, ... , $6000$ \\} and the following values for $f_{B}(hk)$ with $h=1000$:\n\n| $k$ | $0$ | $1$   | $2$   | $3$   | $4$    | $5$   | $6$   |\n|---|---|-----|-----|-----|------|-----|------|\n| $f_{B}(hk)$ |$0$ | $0.2$ | $0.3$ | $0.2$ | $0.15$ | $0.1$ | $0.05$ |\n\nWe implement the following:\n```sh\nfb=np.zeros(30*1000+1)\nfb[0]=0\nfb[1000]=0.2\nfb[2000]=0.3\nfb[3000]=0.2\nfb[4000]=0.15\nfb[5000]=0.1\nfb[6000]=0.05 \nmodel= Marceau.Cossette(k=10,h=1000,parameters=[1.25],method='Poisson',fb=fb) \n```\n\nAnd we get our output with the call model.panjer():\n```sh\nmodel.panjer()\n >>> f(10*1000)=0.02089842353538644 \nF(10*1000)=0.9536818666811318  \n```\n\n\n## Aknowledgement\nThis module was built with the help of [Marceau] lecture of Risk Theory.\n\n\n## License\n\nMIT\nCopyright (c) 2022 Rayane Vigneron\n\n\n\n\n[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job)\n\n   [git-repo-url]: <https://github.com/despervita/Marceau>\n   [panjer]: <https://www.casact.org/sites/default/files/database/astin_vol12no1_22.pdf>\n   [scipy.stats]: <https://docs.scipy.org/doc/scipy/reference/stats.html>\n   [numpy]: <https://numpy.org/doc/stable/index.html>\n   [Panjer-Katz]: <https://doi.org/10.1016/j.insmatheco.2010.03.010>\n   [class of distributions]: <https://www.actuaries.org/ASTIN/Colloquia/Helsinki/Papers/S7_13_Fackler.pdf>\n   [jQuery]: <http://jquery.com>\n   [Marceau]: <https://www.act.ulaval.ca/departement-et-professeurs/professeurs-et-personnel/professeurs/fiche-de-professeur/etienne-marceau-138>\n   "


setup(
  name = 'Marceau',         # How you named your package folder (MyLib)
  packages = ['Marceau'],   # Chose the same as "name"
  version = '0.46',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = "Panjer's Algorithm in Python",   # Give a short description about your library
  author = 'Rayane Vigneron',                   # Type in your name
  author_email = 'rayanevigneron@yahoo.fr',      # Type in your E-Mail
  url = 'https://github.com/despervita/Marceau',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/despervita/Marceau/archive/v_046.tar.gz',    # I explain this later on
  keywords = ['Panjer', 'Python'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy',
          'scipy',
      ],
   long_description=long_desc,
   long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9' ,     #Specify which pyhton versions that you want to support

  ],
)






















