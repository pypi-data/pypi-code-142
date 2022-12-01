
from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.5'
DESCRIPTION = 'A basic hello package'
LONG_DESCRIPTION = 'A small example package'

# Setting up
setup(
    name="hellojeno",
    version=VERSION,
    author="AKANIT",
    author_email="<akanitk84@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description="long_description",
    packages=find_packages(),
    # install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    install_requires=[],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]   
)
