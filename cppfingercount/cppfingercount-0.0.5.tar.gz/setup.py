from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.5'
DESCRIPTION = 'Made by x21223572. cpp-project finger count package '


# Setting up
setup(
    name="cppfingercount",
    version=VERSION,
    author="harsh mall",
    author_email="contact.harshmall@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'mediapipe', 'numpy'],
    keywords=['python', 'video', 'camera', 'base64', 'finger count', 'number'], 
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)