# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openpy_fx_tools_dss',
 'openpy_fx_tools_dss.IMEX_to_DSS',
 'openpy_fx_tools_dss.IMEX_to_DSS.GIS_info_DSS',
 'openpy_fx_tools_dss.IMEX_to_DSS.cim_DSS_cim',
 'openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx',
 'openpy_fx_tools_dss.IMEX_to_DSS.xlsx_DSS_xlsx.Types_elem_DSS_to_xlxs',
 'openpy_fx_tools_dss.IMEX_to_DSS.xml_DSS_xml',
 'openpy_fx_tools_dss.Plots_DSS',
 'openpy_fx_tools_dss.data_from_DSS',
 'openpy_fx_tools_dss.data_from_DSS.parameters',
 'openpy_fx_tools_dss.data_from_DSS.results',
 'openpy_fx_tools_dss.logg_print_alert']

package_data = \
{'': ['*'],
 'openpy_fx_tools_dss': ['Examples/123Bus/DSS_files/*',
                         'Examples/123Bus/xlsx_files/*',
                         'Examples/123Bus/xlsx_files/DSS_files_from_xlsx/*',
                         'Examples/13Bus/DSS_files/*',
                         'Examples/13Bus/xlsx_files/*',
                         'Examples/13Bus/xlsx_files/DSS_files_from_xlsx/*',
                         'Examples/37Bus/DSS_files/*',
                         'Examples/37Bus/xlsx_files/*',
                         'Examples/37Bus/xlsx_files/DSS_files_from_xlsx/*',
                         'Examples/Base_Empty/*'],
 'openpy_fx_tools_dss.data_from_DSS': ['help_DSS/*']}

install_requires = \
['colorama==0.4.6',
 'numpy==1.23.5',
 'opendssdirect-py==0.7.0',
 'openpyxl==3.0.10',
 'pandas==1.5.2',
 'py-dss-interface==1.0.2']

setup_kwargs = {
    'name': 'openpy-fx-tools-dss',
    'version': '0.1.5',
    'description': 'Python functions for extracting, executing routines, etc. from projects modeled in OpenDSS',
    'long_description': '# OpenPy-fx-tools-DSS\nPython functions for extracting, executing routines, etc. from projects modeled in OpenDSS\n# Install\nWith pip\n\n``pip install openpy-fx-tools-dss``\n\n# How to use\nFirst, in the IDE (Integrated Development Environment) of preference, we import the library:\n\n```Python\nimport openpy_fx_tools_dss as fx_dss\n```\n## Examples\nThe library has IEEE example circuits (Table 1), which can be found in the OpenDSS installation files.\nFor the example files the class ``examples_lib()`` is called: \n\n**Table 1.** Sample tests\n\n| **Name**   | **Option** | **DSS files** | **xlsx file** |\n|------------|------------|---------------|---------------|\n| 13BusIEEE  | 1          | x             | x             |\n| 37BusIEEE  | 2          | x             | x             |\n| 123BusIEEE | 3          | x             | x             |\n\n\n```Python\ntest = fx_dss.examples_lib()\n```\n\nTo use the .DSS files:\n\n``DSS_path = test.load_examples_DSS()``\n\nTo use .xlsx file:\n\n``xlsx_path = test.load_examples_xlsx()``\n\n## OpenDSS to xlsx and vice versa \nThe functions that generate OpenDSS scripts to a .xlsx file and vice versa are inside the ``xlsx_DSS_xlsx()`` class and are called in the following way:\n\n``xlsx = fx_dss.xlsx_DSS_xlsx()``\n### Template xlsx\n\nAn .xlsx template with the OpenDSS elements is created by calling the ``create_template_xlsx`` function as follows:\n\n```Python\nxlsx.create_template_xlsx(\n    path_save: str = None, \n    prj_name: str = \'default\', \n    elem_list: list = [], \n    all_elem: bool = True\n)\n```\n### xlsx to OpenDSS\nThe circuit data is entered in the .xlsx template. Each sheet of the template corresponds to the elements that are modeled in OpenDSS. When generating the OpenDSS scripts, only the cells that are not empty are considered.\nFor this purpose, the ``xlsx_to_OpenDSS`` function is called as follows:\n\n```Python\nxlsx.xlsx_to_OpenDSS(\n    xlsx_path=xlsx_path[\'xlsx_path\'],\n    path_save=xlsx_path[\'path_save\'],\n    prj_name=DSS_path[\'prj_name\']\n)\n```\n\n**Important:**\n\n* Do not alter the names of the sheets, and columns, since the element will not be taken into account. \n* The form of data entry must coincide with the OpenDSS specifications.\n\n\n\n\n### OpenDSS to xlsx\nFrom an OpenDSS file, the xlsx template can be generated. For this purpose, the ``OpenDSS_to_xlsx`` function is used as follows:\n\n```Python\nxlsx.OpenDSS_to_xlsx(\n    DSS_path=DSS_path[\'DSS_path\'],\n    path_save=DSS_path[\'path_save\'],\n    prj_name=DSS_path[\'prj_name\']\n)\n```\n\n# License\nLicense: CC BY-NC-SA 4.0\n\n<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />\n\nThis work has a license <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.\n',
    'author': 'Jorge A. Lara S.',
    'author_email': 'jlara@iee.unsj.edu.ar',
    'maintainer': 'Jorge A. Lara S.',
    'maintainer_email': 'jlara@iee.unsj.edu.ar',
    'url': 'https://github.com/jlara6/OpenPy-fx-tools-DSS',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
