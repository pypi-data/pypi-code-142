from setuptools import setup, find_packages
import energy_callback


# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(name='energy-callback',
      version='0.1.10',
      packages=find_packages(),
      install_requires=['tensorflow', 'energy-monitor'],
      long_description=long_description,
      long_description_content_type='text/markdown')
