from os import path
from setuptools import setup, find_packages
from lagrang_pack import __about__


try:
    current_path = path.abspath(path.dirname(__file__))
except NameError:
    current_path = None


try:
    with open(path.join(current_path, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''


setup(
    name='lagrang_pack',
    version='1.1',
    license='MIT License',
    author="Svetlana Ilina",
    author_email='skammm.04@mail.ru',
    description='Lagrang product',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),  # packages=['test_package'],
    python_requires='>=3.5',  # pip проверит версии насовпадение
    install_requires=[],  # внешние зависимости, будут установлены pip при установке этого пакета
    entry_points={
        'console_scripts': [
            'main=lagrang_pack:main',
            'lagrang=lagrang_pack.to_sum_of_squares:lagrang',
        ],
    },
)
