from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='mkdocsquad7',
    version='0.0.1',
    url='https://github.com/fga-eps-mds/2022-2-Squad07',
    license='MIT License',
    author='Bruno Martins, Rafael Nobre, Diógenes Júnior, Bruno Ribeiro, Igor Penha',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='diogjunior10071@gmail.com',
    keywords='Pacote',
    description=u'',
    packages=['mkdocs'],
    install_requires=[''],)