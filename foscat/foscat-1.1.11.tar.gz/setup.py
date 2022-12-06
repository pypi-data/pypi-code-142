from setuptools import setup, find_packages


setup(
    name='foscat',
    version='1.1.11',
    description='Synthesise 2D or Healpix data using Cross Scattering Transform' ,
    long_description='Synthesise data (2D or Healpix) using Cross Scattering Transform (https://arxiv.org/abs/2207.12527) usable for component separation (e.g. denoising).\n\n1. startup\nTo generate test files run the follosing lines inside python:\n\n* import foscat.build_demo as dem\n* dem.genDemo()\n* quit()\n\n2. run 2D test:\n\n   >python test2D.py\n\nto plot the corresponding results:\n\n   >python test2Dplot.py\n\n3. run spherical test:\n\n   >python testHealpix.py\n\nto plot the corresponding results:\n\n   >python testHplot.py\n\nNote: If mpi is available you can run testHealpix_mpi.py that uses 3 nodes to do the same computation than testHealpix.py.',
    long_description_content_type='text/markdown',
    license='MIT',
    author='Jean-Marc DELOUIS',
    author_email='jean.marc.delouis@ifremer.fr',
    maintainer='Theo Foulquier',
    maintainer_email='theo.foulquier@ifremer.fr',
    packages=['foscat'],
    package_dir={'': 'src'},
    url='https://gitlab.ifremer.fr/deepsee/foscat',
    keywords=['Scattering transform','Component separation', 'denoising'],
    install_requires=[
          'imageio',
          'imagecodecs',
          'matplotlib',
          'numpy',
          'tensorflow-gpu',
          'healpy',
      ],

)
