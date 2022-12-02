# This Python file uses the following encoding: utf-8
from setuptools import setup, find_packages

setup(name='MS_visualizer',
      packages=find_packages(),
      version='0.0.1',
      description='Description.',
      long_description='Long description.',
      author=['ThiloSchild', 'David Teschner', 'MatteoLacki'],
      author_email='matteo.lacki@gmail.com',
      url='https://github.com/MatteoLacki/MS_visualizer2.git',
      keywords=['Great module', 'Devel Inside'],
      classifiers=['Development Status :: 1 - Planning',
                   'License :: OSI Approved :: BSD License',
                   'Intended Audience :: Science/Research',
                   'Topic :: Scientific/Engineering :: Chemistry',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.10'],
      install_requires=[
          'dash',
          'plotly',
          'pandas',
          'jsonschema',
          'opentimspy',
          'opentims_bruker_bridge',
      ],
      entry_points={
          'console_scripts': [
              'MS_visualizer = MS_visualizer.bin.run:main'
          ],

      }
      )
