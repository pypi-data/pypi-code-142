# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xerparser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xerparser',
    'version': '0.2.11',
    'description': 'Parse a P6 .xer file to a Python dictionary object.',
    'long_description': '# xerparser\n\nA simple Python package that reads a P6 .xer file and converts it into a Python dictionary object.  \n<br>\n*Disclaimer: this package is only usefull if you are already familiar with the mapping and schemas used by P6 during the export process. \nRefer to the [Oracle Documentation]( https://docs.oracle.com/cd/F25600_01/English/Mapping_and_Schema/xer_import_export_data_map_project/index.htm) for more information regarding how data is mapped to the XER format.*  \n<br>\n## Install\n**Windows**: pip install xerparser  \n**Linux/Mac**: pip3 install xerparser  \n<br>\n## Usage\n```python\nxer_to_dict(file: str | bytes) -> dict\n```  \nImport the ***xer_to_dict*** function from **xerparser**  and pass a .xer file as an argument.  \n```python\nfrom xerparser import xer_to_dict\n\nfile = r"/path/to/file.xer"\nxer = xer_to_dict(file)\n```\nThe xer_to_dict function accepts .xer file passed as type **str** or type **bytes**.  \nThe file and table data will be parsed and returned as a Python dictionary object contining the file and table data from the .xer.  \n<br>\n## Keys / Attributes \n**\\["version"]** -> Version of P6 the .xer file was exported as.  <br>\n**\\["export_date"]** -> Date the .xer file was exported from P6 (datetime object).  \n**\\["errors"]** -> A list of potential errors in the .xer file based on common issues encountered when analyzing .xer files:  \n- Minimum required tables - an error is recorded if one of the following tables is missing:\n  - CALENDAR\n  - PROJECT\n  - PROJWBS\n  - TASK\n  - TASKPRED  \n- Required table pairs - an error is recorded if Table 1 is included but not Table 2:  \n  \n  | P6 Table 1       | P6 Table 2       | Notes    |\n  | :-----------: |:-------------:|----------|\n  | TASKFIN | FINDATES | *Financial Period Data for Task* |\n  | TRSRCFIN | FINDATES | *Financial Period Data for Task Resource* |\n  | TASKRSRC | RSRC | *Resource Data* |\n  | TASKMEMO | MEMOTYPE | *Notebook Data* |\n  | ACTVCODE | ACTVTYPE | *Activity Code Data* |\n  | TASKACTV | ACTVCODE | *Activity Code Data* |\n\n- Non-existent calendars assigned to activities.\n<br>  \n  \n**\\["tables"]**: Dictionay of each table included in the .xer file.  \nExamples: *PROJECT, PROJWBS, CALENDAR, TASK, TASKPRED*, etc...  \nThe table name (e.g *TASK*) is the key, and the value is a list of the table entries, which can be accessed the same as any Python dictionary object:  \n    \n```python\nxer["tables"]["TASK"]\n# or\nxer["tables"].get("TASK")\n```  \n\nEach table entry is a dictionary object where the key is the field name (e.g. *task_id, task_code, and task_name*) from the table schema.\n\n```python\nfor task in xer["tables"].get["TASK", []]:  \n    print(task["task_code"], task["task_name"])  # -> A1000 Install Widget\n```  \n<br>  \n\n## Example Code\n```python\nfrom xerparser import xer_to_dict  \n\nfile = r"/path/to/file.xer"\nxer = xer_to_dict(file)  \nxer["version"]  # -> 15.2  \nxer["export_date"]  # -> datetime.datetime(2022, 11, 30, 0, 0)  \nxer["errors"]  # -> []  \n\nxer["tables"].get("TASK")  # -> [{"task_id": 12345, ...}, {"task_id": 12346,...}]  \nlen(xer["tables"].get("TASK",[]))  # -> 950\n```',
    'author': 'Jesse',
    'author_email': 'code@seqmanagement.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jjCode01/xerparser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
