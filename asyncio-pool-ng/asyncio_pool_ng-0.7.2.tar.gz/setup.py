# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asyncio_pool']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.6']

entry_points = \
{'console_scripts': ['pytest = pytest:main']}

setup_kwargs = {
    'name': 'asyncio-pool-ng',
    'version': '0.7.2',
    'description': 'A pool of coroutine functions.',
    'long_description': '# asyncio-pool-ng\n\n[![PyPI version](https://img.shields.io/pypi/v/asyncio-pool-ng)](https://pypi.org/project/asyncio-pool-ng/)\n[![Python Versions](https://img.shields.io/pypi/pyversions/asyncio-pool-ng)](https://pypi.org/project/asyncio-pool-ng/)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n[![](https://github.com/smithk86/asyncio-pool-ng/workflows/ci/badge.svg)](https://github.com/smithk86/asyncio-pool-ng/actions?query=workflow%3Aci)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## About\n\n**AsyncioPoolNG** takes the ideas used in [asyncio-pool](https://github.com/gistart/asyncio-pool) and wraps them around a [TaskGroup](https://anyio.readthedocs.io/en/stable/tasks.html) from [anyio](https://anyio.readthedocs.io/en/stable/index.html).\n\n`AsyncioPool` has three main functions `spawn`, `map`, and `itermap`.\n\n1. `spawn`: Schedule an async function on the pool and get a future back which will eventually have either the result or the exception from the function.\n2. `map`: Spawn an async function for each item in an iterable object, and return a set containing a future for each item.\n\n- `asyncio.wait()` can be used to wait for the set of futures to complete.\n- When the `AsyncioPool` closes, it will wait for all tasks to complete. All pending futures will be complete once it is closed.\n\n3. `itermap`: Works similarly to `map` but returns an [Async Generator](https://docs.python.org/3/library/typing.html#typing.AsyncGenerator "Async Generator") which yields each future as it completes.\n\n## Differences from asyncio-pool\n\n1. `asyncio-pool-ng` implements [Python typing](https://typing.readthedocs.io/en/latest/) and passes validation checks with [mypy](http://mypy-lang.org/)\'s strict mode. This helps IDEs and static type checkers know what type of result to expect when getting data from a completed future.\n2. `asyncio-pool` uses callbacks to process data before returning it; `asyncio-pool-ng` only returns [Future](https://docs.python.org/3.10/library/asyncio-future.html#asyncio.Future) instances directly. The future will contain either a result or an exception which can then be handled as needed.\n3. While `asyncio-pool` schedules [Coroutine](https://docs.python.org/3/library/typing.html#typing.Coroutine) instances directly, `asyncio-pool-ng` takes the callable and arguments, and creates the Coroutine instance at execution time.\n\n## Example\n\n```python title="example.py"\nimport asyncio\nimport logging\nfrom random import random\n\nfrom asyncio_pool import AsyncioPool\n\n\nlogging.basicConfig(level=logging.INFO)\n\n\nasync def worker(number: int) -> int:\n    await asyncio.sleep(random() / 2)\n    return number * 2\n\n\nasync def main() -> None:\n    result: int = 0\n    results: list[int] = []\n\n    async with AsyncioPool(2) as pool:\n        """spawn task and wait for the results"""\n        result = await pool.spawn(worker, 5)\n        assert result == 10\n        logging.info(f"results for pool.spawn(worker, 5): {result}")\n\n        """spawn task and get results later"""\n        future: asyncio.Future[int] = pool.spawn(worker, 5)\n\n        # do other stuff\n\n        result = await future\n        assert result == 10\n\n        """map an async function to a set of values"""\n        futures: set[asyncio.Future[int]] = pool.map(worker, range(10))\n        await asyncio.wait(futures)\n        results = [x.result() for x in futures]\n        logging.info(f"results for pool.map(worker, range(10)): {results}")\n        results.sort()\n        assert results == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n\n        """iterate futures as they complete"""\n        logging.info("results for pool.itermap(worker, range(10)):")\n        results = []\n        async for future in pool.itermap(worker, range(10)):\n            results.append(future.result())\n            logging.info(f"> {future.result()}")\n\n        results.sort()\n        assert results == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]\n\n\nasyncio.run(main())\n```\n',
    'author': 'Kyle Smith',
    'author_email': 'smithk86@smc3.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/smithk86/asyncio-pool-ng',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4',
}


setup(**setup_kwargs)
