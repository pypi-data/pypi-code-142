from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.12'
DESCRIPTION = "Executes GREP on your Android device, and returns a Pandas DataFrame"

# Setting up
setup(
    name="adb_grep_search",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/adb_grep_search',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['get_the_hell_out_of_here', 'pandas', 'subprocess_print_and_capture'],
    keywords=['grep', 'pandas', 'DataFrame', 'regex', 'adb', 'Android'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['get_the_hell_out_of_here', 'pandas', 'subprocess_print_and_capture'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*