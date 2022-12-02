# setup.py - settings file for twine. This info is used to export this package to pypi.org
# https://pypi.org/manage/projects/

from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.10'
DESCRIPTION = 'Generate a word cloud png file based on text or a URL contents.'
LONG_DESCRIPTION = 'A package that creates png image files based on text or the contents of a URL.'

setup(
    name="keywordcloud",
    version=VERSION,
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    author="Jeffery Mandrake",
    author_email="<info@goinfosystems.com>",
    url = "https://amzto.com/",   # Link to your github or to your website
    download_url = "https://github.com/jmandrake/keywordcloud",    # Github Repo page
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['wordcloud', 'numpy', 'matplotlib', 'pillow'],
    keywords=['python', 'keyword cloud', 'word cloud', 'wordcloud', 'keywordcloud', 'keywords', 'png', 'keyword', 'text to image'],    
    classifiers=[
        # Classifiers: -->> https://pypi.org/classifiers/
        #                   https://pypi.org/search/?q=&o=
        "Development Status :: 1 - Planning",      
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing", 
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content", 
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)