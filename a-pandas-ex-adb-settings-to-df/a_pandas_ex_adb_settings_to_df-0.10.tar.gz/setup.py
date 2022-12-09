from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.10'
DESCRIPTION = "# Parses all Android config files (json/db/xml) in the /data/ folder and returns an easy-to-handle DataFrame"

# Setting up
setup(
    name="a_pandas_ex_adb_settings_to_df",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/a_pandas_ex_adb_settings_to_df',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_pandas_ex_adb_to_df', 'a_pandas_ex_plode_tool', 'a_pandas_ex_read_sql', 'a_pandas_ex_text_compare', 'a_pandas_ex_xml2df', 'flexible_partial', 'list_all_files_recursively', 'pandas', 'regex', 'ujson'],
    keywords=['settings', 'adb', 'pandas', 'DataFrame', 'content', 'android', 'providers'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_pandas_ex_adb_to_df', 'a_pandas_ex_plode_tool', 'a_pandas_ex_read_sql', 'a_pandas_ex_text_compare', 'a_pandas_ex_xml2df', 'flexible_partial', 'list_all_files_recursively', 'pandas', 'regex', 'ujson'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*