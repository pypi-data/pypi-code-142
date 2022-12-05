"""
package file
"""

import setuptools

setuptools.setup(
    name='stock portfolio',
    version='0.0.1',
    author='Frank Teixeira',
    python_requires='>3.0',
    description='stock portfolio report generator',
    packages=['portfolio'],
    entry_points={
        'console_scripts': ['portfolio_report=portfolio_report:main']
    },
    install_requires=[
        "requests>=2", "pytest>=7", "requests-mock>=1"
    ]
)

