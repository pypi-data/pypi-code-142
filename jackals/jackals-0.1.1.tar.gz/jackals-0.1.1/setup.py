from setuptools import find_packages, setup
setup(
    name='jackals',
    packages=find_packages(include=['src']),
    version='0.1.1',
    description='Quantco Exercise',
    author='Pietro Bonazzi',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='test',
)
