# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xerparser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xerparser',
    'version': '0.1.2',
    'description': 'Parse a P6 .xer file to a Python dictionary object.',
    'long_description': '# `xerparser`\n\n`xerparser` reads a P6 .xer file and converts it into a Python dictionary object containing key, value pairs:\n1. ***"version"***: Version of P6 the .xer file was exported as.\n2. ***"export_date"***: Date the .xer file was exported from P6 (datetime object).\n3. ***"errors"***: A list of potential errors in the .xer file based on common issues encountered when analyzing .xer files:  \n    - Minimum required tables for a valid P6 schedule are:\n      - CALENDAR\n      - PROJECT\n      - PROJWBS\n      - TASK\n      - TASKPRED\n    - Required table pairs are:\n      - TASKFIN <> FINDATES : (*Financial Period Data*)\n      - TRSRCFIN <> FINDATES (*Financial Period Data*)\n      - TASKRSRC <> RSRC (*Resource Data*)\n      - TASKMEMO <> MEMOTYPE (*Notebook Data*)\n      - ACTVCODE <> ACTVTYPE (*Activity Code Data*)\n      - TASKACTV <> ACTVCODE (*Activity Code Data*)\n    - Non-existent calendars assigned to activities.  \n    <br>\n4. ***"tables"***: Dictionay of each table included in the .xer file.  \n    Examples: *PROJECT, PROJWBS, CALENDAR, TASK, TASKPRED*, etc... [See Oracle Documentation]( https://docs.oracle.com/cd/F25600_01/English/Mapping_and_Schema/xer_import_export_data_map_project/index.htm) for mapping and schema of P6 database tables.  \n    The table name (e.g *TASK*) is the key, and the value is a list of the table entries, which can be accessed the same as any Python dictionary object:  \n    \n    >xer["tables"]["TASK"]  \n    >or  \n    >xer["tables"].get("TASK")  \n\n   Each table entry is a dictionary object where the key is the field name (e.g. *task_id, task_code, and task_name*) from the table schema.\n\n   >for task in xer["tables"].get["TASK", []]:  \n   >&nbsp;&nbsp;&nbsp;&nbsp; print(task["task_code"], task["task_name"])\n\nExample Code\n>from xerparser import xer_to_dict  \n>\n>xer = xer_to_dict("*path to file.xer*")  \n>xer["version"]  # -> *15.2*  \n>xer["export_date"]  # -> *datetime.datetime(2022, 11, 30, 0, 0)*  \n>xer["errors"]  # -> *[ ]*  \n>\n>xer["tables"].get("TASK")  # -> *[{"task_id": 12345, ...}, {"task_id": 12346,...}]*  \n>len(xer["tables"].get("TASK",[]))  # -> *950* ',
    'author': 'Jesse',
    'author_email': 'code@seqmanagement.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jjCode01/xerparser',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
