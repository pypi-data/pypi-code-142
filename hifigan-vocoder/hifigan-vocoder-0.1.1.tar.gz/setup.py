from setuptools import setup, find_packages

NAME             = "hifigan-vocoder"
AUTHOR           = "Mushan"
AUTHOR_EMAIL     = "wwd137669793@gmail.com"
DESCRIPTION      = "A wrapped hifi-gan vocoder for easy use."
LICENSE          = "MIT"
KEYWORDS         = "None"
URL              = "https://github.com/mushanshanshan/hifigan"
README           = ".github/README.md"
VERSION          = "0.1.1"
CLASSIFIERS      = [
  "Environment :: Console",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.7",
]

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

ENTRY_POINTS = {
    
}

SCRIPTS = [
  
]

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

if __name__ == "__main__":
  setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    scripts=SCRIPTS,
    include_package_data=True    
  )