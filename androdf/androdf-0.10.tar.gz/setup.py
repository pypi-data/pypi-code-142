from setuptools import setup, find_packages
import codecs
import os

#change to dict
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.10'
DESCRIPTION = " Locates more items/views/elements on an Android device than similar automation packages by combining ADB's dumpsys activity/uiautomator"

# Setting up
setup(
    name="androdf",
    version=VERSION,
    license='MIT',
    url = 'https://github.com/hansalemaos/androdf',
    author="Johannes Fischer",
    author_email="<aulasparticularesdealemaosp@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    #packages=['a_cv2_imshow_thread', 'a_cv_imwrite_imread_plus', 'a_pandas_ex_plode_tool', 'a_pandas_ex_string_to_dtypes', 'a_pandas_ex_xml2df', 'flatten_everything', 'generate_random_values_in_range', 'keyboard', 'numpy', 'opencv_python', 'pandas', 'PrettyColorPrinter', 'psutil', 'regex', 'sendevent_touch', 'Shapely'],
    keywords=['uiautomator', 'dumpsys', 'adb', 'android', 'debugging', 'pandas', 'DataFrame', 'AndroidManifest', 'views', 'items', 'automation'],
    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
    install_requires=['a_cv2_imshow_thread', 'a_cv_imwrite_imread_plus', 'a_pandas_ex_plode_tool', 'a_pandas_ex_string_to_dtypes', 'a_pandas_ex_xml2df', 'flatten_everything', 'generate_random_values_in_range', 'keyboard', 'numpy', 'opencv_python', 'pandas', 'PrettyColorPrinter', 'psutil', 'regex', 'sendevent_touch', 'Shapely'],
    include_package_data=True
)
#python setup.py sdist bdist_wheel
#twine upload dist/*