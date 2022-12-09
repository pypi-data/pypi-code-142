from setuptools import setup, find_packages

setup(name='ocutils',
      version='1.2.0',
      description='Utility functions for oceanography related work',
      author='Marcus Donnelly',
      author_email='marcus.k.donnelly@gmail.com',
      url='https://github.com/marcuskd/ocutils',
      license='MIT',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering'
                   ],
      keywords=['Oceanography'
                ],
      packages=find_packages(),
      install_requires=['numpy >= 1.20',
                        ],
      include_package_data=True,
      )
