from setuptools import setup, find_packages
import energy_callback

NAME = 'energy_callback'
VERSION = '0.1.7'

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def setup_package():
    metadata = dict(name=NAME,
                    version=VERSION,
                    packages=find_packages(),
                    package_data={'': ['*.csv', '*txt']},
                    include_package_Data=True,
                    long_description=long_description,
                    long_description_content_type='text/markdown',
                    install_requires=['tensorflow==2.10.0', 'energy-monitor==0.7.5'],
                    )

    setup(**metadata)


if __name__ == "__main__":
    setup_package()
