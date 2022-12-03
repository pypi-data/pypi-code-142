"""分发安装的配置文件"""

from setuptools import setup
setup(
    name="pytest_py125",
    version="1.0.1",
    # 包名
    packages=['src'],
    # 指定插件文件
    entry_points={"pytest11":["pytest_py125=src.pytest_py125"]},
    # pipy插件分类器
    classifiers=["Framework :: Pytest"]
)