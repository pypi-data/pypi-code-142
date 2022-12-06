# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['echaim']

package_data = \
{'': ['*'],
 'echaim': ['CMakeFiles/*',
            'CMakeFiles/3.22.1/*',
            'CMakeFiles/3.22.1/CompilerIdC/*',
            'CMakeFiles/3.22.1/CompilerIdCXX/*',
            'CMakeFiles/3.24.2/*',
            'CMakeFiles/3.24.2/CompilerIdC/*',
            'CMakeFiles/3.24.2/CompilerIdC/Debug/*',
            'CMakeFiles/3.24.2/CompilerIdC/Debug/CompilerIdC.tlog/*',
            'CMakeFiles/3.24.2/CompilerIdCXX/*',
            'CMakeFiles/3.24.2/CompilerIdCXX/Debug/*',
            'CMakeFiles/3.24.2/CompilerIdCXX/Debug/CompilerIdCXX.tlog/*',
            'CMakeFiles/3.24.2/x64/Debug/*',
            'CMakeFiles/3.24.2/x64/Debug/VCTargetsPath.tlog/*',
            'CMakeFiles/7e97d2cf9e912ad5c9cd3e42a871d55a/*',
            'CMakeFiles/ECHAIM.dir/*',
            'CMakeFiles/ECHAIM.dir/source_c/lib/*',
            'CMakeFiles/ECHAIM_bug_report.dir/*',
            'CMakeFiles/ECHAIM_bug_report.dir/source_c/lib/*',
            'cmake-build-debug/CMakeFiles/*',
            'model_data/*',
            'model_data/AACGM_coeffs/*',
            'source_c/*',
            'source_c/cmake-build-debug/*',
            'source_c/cmake-build-debug/.cmake/api/v1/query/*',
            'source_c/cmake-build-debug/.cmake/api/v1/reply/*',
            'source_c/cmake-build-debug/CMakeFiles/*',
            'source_c/cmake-build-debug/CMakeFiles/3.24.2/*',
            'source_c/cmake-build-debug/CMakeFiles/3.24.2/CompilerIdC/*',
            'source_c/cmake-build-debug/CMakeFiles/3.24.2/CompilerIdCXX/*',
            'source_c/cmake-build-debug/Testing/Temporary/*',
            'source_c/etc/AACGM_coeffs/*',
            'source_c/etc/COEFS_DB.db',
            'source_c/etc/COEFS_DB.db',
            'source_c/etc/COEFS_DB.db',
            'source_c/etc/COEFS_DB.db',
            'source_c/etc/ECHAIMInputs.dat',
            'source_c/etc/ECHAIMInputs.dat',
            'source_c/etc/ECHAIMInputs.dat',
            'source_c/etc/ECHAIMInputs.dat',
            'source_c/etc/ECHAIM_FIRI.db',
            'source_c/etc/ECHAIM_FIRI.db',
            'source_c/etc/ECHAIM_FIRI.db',
            'source_c/etc/ECHAIM_FIRI.db',
            'source_c/etc/PRECIP_DB.db',
            'source_c/etc/PRECIP_DB.db',
            'source_c/etc/PRECIP_DB.db',
            'source_c/etc/PRECIP_DB.db',
            'source_c/examples/*',
            'source_c/lib/*',
            'source_c/licenses/*',
            'source_c/source_docs/*',
            'source_c/test_app/*']}

install_requires = \
['numpy>=1.22,<2.0',
 'sphinx-autodoc-typehints>=1.19.5,<2.0.0',
 'sphinx-rtd-theme>=1.1.1,<2.0.0',
 'sphinx>=5.3.0,<6.0.0',
 'sphinxcontrib-bibtex>=2.5.0,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'echaim',
    'version': '1.0.8',
    'description': 'A Python wrapper to the E-CHAIM C source code.',
    'long_description': '# echaim\nA Python interface to ECHAIM model. Documentation is available at [RTD website](https://echaim.readthedocs.io/en/latest/index.html).\n',
    'author': 'lap1dem',
    'author_email': 'vadym.bidula@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
