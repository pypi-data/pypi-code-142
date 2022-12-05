# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pytest_line_profiler_apn']
install_requires = \
['line-profiler', 'pytest>=3.5.0']

entry_points = \
{'pytest11': ['line-profiler = pytest_line_profiler_apn']}

setup_kwargs = {
    'name': 'pytest-line-profiler-apn',
    'version': '0.1.5',
    'description': 'Profile code executed by pytest',
    'long_description': '# pytest-line-profiler-apn\n\n[![PyPI version][]][1] [![Python versions][]][1]\n\nline-by-line profiling for code executed by pytest, using [line-profiler](https://github.com/pyutils/line_profiler).\n\n## Why?\n\nLine profiler is a wonderful tool to easily identify bottlenecks inside specific functions of your code, and quantify the improvements after a refactor. \n\nUsing it is straightforward but required to instrument the functions you want to profile with a "virtual" `@profile` decorator\nand then execute "a trigger script" (code that calls the decorated functions somehow) via `kernprof.py` which works as a python wrapper that understands the decorator, register the functions to be profiled, and print the stats when the script finishes.   \n\nAltought it does its job, is a bit invasive: you need to have an special "instrumented" version of your code, \nand execute it in a way that potentially clashes with the way you do normally (for instance, through a shortcut command from your editor, a test runner, another script, etc.)   \n\nMoreover, frequently in real case scenarios, "a trigger script" isn\'t just a simple function call. \nYou need to prepare input data, connect to external resources, etc. And that\'s exactly what a test can do, right?    \n\n## Installation \n\nYou can install "pytest-line-profiler" via [pip][] from [PyPI][]:\n\n```\n$ pip install pytest-line-profiler\n```\n\n## Usage\n\n\nMark your test passing the functions you wants to profile as positional arguments, \nlike `@pytest.mark.line_profile.with_args(function1, function2, [...])`\n\nIf your test exercises any of those functions, you\'ll get the profile result as a report.  \n\nFor example:\n\n```python\nimport pytest\n\ndef f(i):\n    return i * 10\n\ndef g(n=10):\n    return sum(f(i) for i in range(10))\n\n\n@pytest.mark.line_profile.with_args(f, g)\ndef test_as_mark():\n    assert g() == 450\n\n```\n\n\nAfter that test is executed, you\'ll get the stats from the line profiler instance. \n\n```\n============ Line Profile result for tests/test_line_profiler.py::test_as_mark ============\nTimer unit: 1e-06 s\n\nTotal time: 4e-06 s\nFile: /home/tin/lab/pytest-line-profiler/tests/test_line_profiler.py\nFunction: f at line 4\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n==============================================================\n     4                                           def f(i):\n     5        10          4.0      0.4    100.0      return i * 10\n\nTotal time: 3e-05 s\nFile: /home/tin/lab/pytest-line-profiler/tests/test_line_profiler.py\nFunction: g at line 7\n\nLine #      Hits         Time  Per Hit   % Time  Line Contents\n==============================================================\n     7                                           def g(n=10):\n     8         1         30.0     30.0    100.0      return sum(f(i) for i in range(10))\n```\n\n\nAlternatively, you can run any test passing the function/s to profile from the command line\n\n```\n$ pytest --line-profile path.to.function_to_be profiled [...] \n```\n\n\n## Contributing\n\nContributions are very welcome. Tests can be run with [pytest][], please\nensure the coverage at least stays the same before you submit a pull\nrequest.\n\n## License\n\nDistributed under the terms of the [MIT][] license,\n"pytest-line-profiler" is free and open source software\n\n## Issues\n\nIf you encounter any problems, please [file an issue][] along with a\ndetailed description.\n\n  [PyPI version]: https://img.shields.io/pypi/v/pytest-line-profiler-apn.svg\n  [1]: https://pypi.org/project/pytest-line-profiler-apn\n  [Python versions]: https://img.shields.io/pypi/pyversions/pytest-line-profiler-apn.svg\n  [pip]: https://pypi.org/project/pip/\n  [PyPI]: https://pypi.org/project\n  [pytest]: https://github.com/pytest-dev/pytest\n  [MIT]: http://opensource.org/licenses/MIT\n  [file an issue]: https://github.com/APN-Pucky/pytest-line-profiler-apn/issues\n',
    'author': 'Martín Gaitán',
    'author_email': 'gaitan@gmail.com',
    'maintainer': 'Alexander Puck Neuwirth',
    'maintainer_email': 'alexander@neuwirth-informatik.de',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
