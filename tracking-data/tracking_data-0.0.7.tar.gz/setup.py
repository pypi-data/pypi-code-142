from setuptools import setup, find_packages

VERSION = '0.0.7'
DESCRIPTION = 'Tracking annotated data package'
LONG_DESCRIPTION = 'Package which formats and structures video data for single object tracking'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="tracking_data",
        version=VERSION,
        author="Rodion Shyshkin",
        author_email="<rodion.shyshkin@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['opencv-contrib-python'], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'tracking', 'datasets'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
