from setuptools import setup
import setuptools



requirements = ['aiohttp>=3.3', 'aioxmpp>=0.10.4']
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

extras_require = {
    'docs': [
        'sphinxcontrib_trio==1.1.2',
        'furo==2021.4.11b34',
        'Jinja2<3.1',
    ]
}


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='klldpy',
    version='3.6.5',
    description='',
    author= 'klld',
    url = 'https://github.com/klldme/klldpy',
    project_urls={
        "Documentation": "https://klldpy.42web.io/en/latest/",
        "Issue tracker": "https://github.com/klldme/klldpy/issues",
    },
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    keywords=['klldpy'],
    classifiers=[
         'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    python_requires='>=3.5.3',
    py_modules=['klldpy', 'klldpy.ext.commands'],
)