from setuptools import setup, find_packages
import energy_callback

NAME = 'energy_callback'
VERSION = '0.1.6'

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

def setup_package():
    requirements = []
    with open('requirements.txt', 'r') as fh:
        for line in fh:
            requirements.append(line.strip())

    metadata = dict(name=NAME,
                    version=VERSION,
                    packages=find_packages(),
                    package_data={'': ['*.csv', '*txt']},
                    include_package_Data=True,
                    long_description=long_description,
                    long_description_content_type='text/markdown',
                    install_requires=[requirements],
                    )

    setup(**metadata)


if __name__ == "__main__":
    c = energy_callback
    setup_package()
