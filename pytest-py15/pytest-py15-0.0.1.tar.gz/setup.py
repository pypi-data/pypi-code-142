from setuptools import setup

setup(
    name="pytest-py15",
    version='0.0.1',
    packages=["pytestpy15"],
    # 指定插件文件
    entry_points={
        'pytest11': [
            "pytestpy15 = pytestpy15.pytest_py15"
        ],
    },
    # pypi插件分类器
    classifiers=["Framework :: Pytest"],
)
