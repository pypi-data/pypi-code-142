import logging
import setuptools
from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError
from setuptools import Extension

try:
    from Cython.Distutils import build_ext
except ImportError as e:
    warnings.warn(e.args[0])
    from setuptools.command.build_ext import build_ext
    cython_is_installed = False
    
    
with open("README.rst", 'r') as f:
    long_description = f.read()


class CustomBuildExtCommand(build_ext):
    """build_ext command for use when numpy headers are needed."""

    def run(self):
        import numpy
        self.include_dirs.append(numpy.get_include())
        build_ext.run(self)
        
        
logging.basicConfig()
log = logging.getLogger(__file__)
ext_errors = (CCompilerError,
              DistutilsExecError, 
              DistutilsPlatformError,
              IOError, 
              SystemExit)

cython_is_installed = True 

compmem = Extension('jsax.compmem',
                        sources=['jsax/compmem.pyx'])

aggmem = Extension('jsax.aggmem',
                        sources=['jsax/aggmem.pyx'])

inversetc = Extension('jsax.inversetc',
                        sources=['jsax/inversetc.pyx'])

        
        
setup_args = {'name':"jsax",
        'version':"0.2.2",
        'cmdclass': {'build_ext': CustomBuildExtCommand},
        'install_requires':["numpy>=1.17.3", "scipy>=1.2.1",
                            "joblib>=1.1.1",
                            "requests",
                            "pandas", 
                            "scikit-learn",
                            "matplotlib"],
        'package_data':{"jsax": ["data/*.npy"]},
        'packages': ['jsax', 'jsax.data'],
        'long_description':long_description,
        'author':"Xinye Chen, Stefan Güttel",
        'author_email':"xinye.chen@manchester.ac.uk, stefan.guettel@manchester.ac.uk",
        'classifiers':["Intended Audience :: Science/Research",
                    "Intended Audience :: Developers",
                    "Programming Language :: Python",
                    "Topic :: Software Development",
                    "Topic :: Scientific/Engineering",
                    "Operating System :: Microsoft :: Windows",
                    "Operating System :: Unix",
                    "Programming Language :: Python :: 3",
                    "Programming Language :: Python :: 3.6",
                    "Programming Language :: Python :: 3.7",
                    "Programming Language :: Python :: 3.8",
                    "Programming Language :: Python :: 3.9",
                    "Programming Language :: Python :: 3.10"
                    ],
        'description':"jsax: A joint time series symbolic approximation method.",
        'long_description_content_type':'text/x-rst',
        'url':"https://github.com/nla-group/jsax",
        'license':'BSD 3-Clause'
    }

if cython_is_installed:
    try:
        from Cython.Build import cythonize
        setuptools.setup(
            setup_requires=["cython", "numpy>=1.17.3"],

            ext_modules=[
                 compmem,
                 aggmem,
                 inversetc
                ],
            **setup_args
        )

    except ext_errors as ext_reason:
        log.warning(ext_reason)
        log.warning("The C extension could not be compiled.")
        if 'build_ext' in setup_args['cmdclass']:
            del setup_args['cmdclass']['build_ext']
        setuptools.setup(setup_requires=["numpy>=1.17.3"], **setup_args)
else:
    log.warning(ext_reason)
    log.warning("The C extension could not be compiled.")
    if 'build_ext' in setup_args['cmdclass']:
        del setup_args['cmdclass']['build_ext']
    setuptools.setup(setup_requires=["numpy>=1.17.3"], **setup_args)
