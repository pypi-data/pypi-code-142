from setuptools import find_packages, setup

setup(
    name="task_helper",
    version="0.0.3",
    author="Teguh Wijangkoro",
    long_description="When you lazy enough to do simple repetitive stuff with your project tasks.",
    packages=find_packages(include=["task_helper", "task_helper.*"]),
    entry_points={"console_scripts": ["task_helper=task_helper.main:main"]},
)
