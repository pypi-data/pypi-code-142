from setuptools import find_packages, setup
setup(
    name='jackals',
    packages=find_packages(include=['jackals']),
    version='0.1.0',
    description='Quantco Exercise',
    author='Pietro Bonazzi',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
