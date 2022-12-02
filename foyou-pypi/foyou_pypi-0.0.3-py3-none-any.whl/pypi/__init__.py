import os
from pathlib import Path

__version__ = '0.0.3'


class PyPI:
    GITHUB_WORKFLOWS = '.github/workflows'
    PYTHON_PUBLISH_YML = f'{GITHUB_WORKFLOWS}/python-publish.yml'
    STARTED_NOTIFY_YML = f'{GITHUB_WORKFLOWS}/started-notify.yml'
    UPDATE_VERSION_PY = f'{GITHUB_WORKFLOWS}/update_version.py'
    SRC = 'src'
    INIT_PY = '__init__.py'
    PYPROJECT_TOML = 'pyproject.toml'
    REQUIREMENTS_TXT = 'requirements.txt'
    SETUP_CFG = 'setup.cfg'
    README_MD = 'README.md'

    def __init__(self, pypi_name, pkg_name, project):
        self.pypi_name = pypi_name
        self.pkg_name = pkg_name
        self.project = project

    @staticmethod
    def gen_file_by_text(text, file):
        print(f'generate {file}')
        Path(file).write_text(text)

    def gen_github(self):
        """生成 .github - 用作 github action 自动发布"""
        os.makedirs(os.path.join(self.project, self.GITHUB_WORKFLOWS), exist_ok=True)
        self.gen_file_by_text(
            """name: upload python package

on:
  workflow_dispatch:
  release:
    types: [ published ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: set up python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      - name: install depends
        run: |
          python -m pip install --upgrade pip
          pip install build wheel
          python .github/workflows/update_version.py
      - name: build package
        run: python -m build --no-isolation
      - name: publish package
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          user: __token__
          password: ${{ secrets.PYPI_API_TOKEN }}
""", os.path.join(self.project, self.PYTHON_PUBLISH_YML))
        self.gen_file_by_text(
            """name: star notify
on:
  watch:
    types: [started]
jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: download scripts
        run: |
          wget https://raw.githubusercontent.com/foyoux/started-notify/main/.github/workflows/started_notify.py#${{github.run_id}}
      - name: send email
        run: |
          python started_notify.py ${{github.token}} ${{secrets.NOTIFY_EMAIL}}
""", os.path.join(self.project, self.STARTED_NOTIFY_YML))
        self.gen_file_by_text(
            fr"""import os
import re


def get_latest_tag():
    return max(
        {{tag.name: tag.stat().st_mtime_ns for tag in os.scandir('.git/refs/tags')}}.items(),
        key=lambda item: item[1]
    )[0]


if __name__ == '__main__':
    latest_tag = get_latest_tag()
    init_py = 'src/{self.pkg_name}/__init__.py'

    with open(init_py, encoding='utf8') as f:
        txt = f.read()

    txt = re.sub(r"__version__ = '\d+.\d+.\d+'", f"__version__ = '{{latest_tag[1:]}}'", txt)

    with open(init_py, 'w', encoding='utf8') as f:
        f.write(txt)
""", os.path.join(self.project, self.UPDATE_VERSION_PY))

    def gen_src(self):
        """生成源代码目录"""
        os.makedirs(os.path.join(self.project, self.SRC, self.pkg_name), exist_ok=True)
        self.gen_file_by_text(
            '\n'.join([
                '"""generate by foyou-pypi"""',
                '__version__ = \'0.0.1\'',
                '',
                '',
                'def main():',
                f'    print(\'hello from {self.pypi_name}\', __version__)',
                '',
            ]),
            os.path.join(self.project, self.SRC, self.pkg_name, self.INIT_PY)
        )

    def gen_pypi_config(self):
        """生成一些 pypi 包需要的一些配置文件"""
        self.gen_file_by_text(
            """[build-system]
requires = [
    "setuptools>=50",
    "wheel"
]
build-backend = "setuptools.build_meta"
""", os.path.join(self.project, self.PYPROJECT_TOML))
        self.gen_file_by_text('', os.path.join(self.project, self.REQUIREMENTS_TXT))
        self.gen_file_by_text(
            f"""[metadata]
name = {self.pypi_name}
version = attr: {self.pkg_name}.__version__
author = foyou
author_email = yimi.0822@qq.com
description = python pypi package example
long_description = file: README.md
long_description_content_type = text/markdown
license = GPL-3.0
url = https://github.com/foyoux/{self.pypi_name}
project_urls =
    Source = https://github.com/foyoux/{self.pypi_name}
    Bug Tracker = https://github.com/foyoux/{self.pypi_name}/issues
classifiers =
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: 3.10
    Programming Language :: Python :: 3.11
    License :: OSI Approved :: GNU General Public License v3 (GPLv3)
    Environment :: Console
    Natural Language :: Chinese (Simplified)
    Development Status :: 4 - Beta
keywords = python pypi package example
[options]
package_dir =
    = src
packages = find:
python_requires = >=3.7.*
install_requires =


[options.packages.find]
where = src

[options.entry_points]
console_scripts =
    # command-name = {self.pkg_name}:main
""", os.path.join(self.project, self.SETUP_CFG))

    def gen_readme(self):
        self.gen_file_by_text(
            f"""# {self.pypi_name}

description for {self.pypi_name}

[![python version](https://img.shields.io/pypi/pyversions/{self.pypi_name})](https://pypi.org/project/{self.pypi_name}/)  [![Downloads](https://static.pepy.tech/personalized-badge/{self.pypi_name}?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/{self.pypi_name})
""", os.path.join(self.project, self.README_MD)
        )


def main():
    print('hello from pypi', __version__)

    import argparse
    parser = argparse.ArgumentParser(
        description='生成 PyPI Project 的小工具',
        epilog=f'pypi({__version__}) by foyou(https://github.com/foyoux)'
    )
    parser.add_argument('-v', '--version', dest='version', help='show pypi version', action="store_true")
    parser.add_argument('-n', '--name', dest='pypi_name', type=str, required=True,
                        help='package name -> pip install name')
    parser.add_argument('-p', '--package', dest='pkg_name', type=str, required=True,
                        help='main python package name in pypi package')
    parser.add_argument('-o', '--output', dest='output', type=str, default='.',
                        help='optional, pypi project output path')
    args = parser.parse_args()

    if args.version:
        print('pypi version', __version__)
        return

    project = os.path.abspath(args.pypi_name)
    print(f'generate the pypi package project on {project}')
    if not os.path.exists(project):
        print(f'{project} not exists.')
        os.makedirs(project)
        print(f'{project} create success.')
    else:
        print(f'{project} exists.')

    pypi = PyPI(args.pypi_name, args.pkg_name, project)
    pypi.gen_github()
    pypi.gen_src()
    pypi.gen_pypi_config()
    pypi.gen_readme()
