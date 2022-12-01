from setuptools import setup,find_packages
import codecs
import os

here=os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here,"README.md"),encoding="utf-8") as fh:
	long_description="\n"+fh.read()
VERSION="1.0.0"
DESCRIPTION="collage"


setup(
name="collage library",
version=VERSION,
author="Maziar Bahrampour",
author_email="<dr.bahrampour@gmail.com>",
description=DESCRIPTION,
long_description_content_type='text/markdown',
long_description=long_description,
package=find_packages(),
install_requires=[],
keywords=["python","collage","tax","salary","student","employee","insurance"],
classifiers=[
"Development Status :: 1 - Planning",
"Intended Audience :: Developers",
"Programming Language :: Python :: 3",
"Operating System :: Unix",
"Operating System :: MacOS :: MacOS X",
"Operating System :: Microsoft :: Windows",
]
)


