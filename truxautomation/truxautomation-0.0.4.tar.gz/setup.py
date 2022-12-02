from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'A small python package for automating tasks within Trux.'
LONG_DESCRIPTION = 'A small python package for automating tasks within Trux.'

# Setting up
setup(
        name="truxautomation", 
        version=VERSION,
        author="Nevil Mills",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pyautogui', 'Pillow'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)