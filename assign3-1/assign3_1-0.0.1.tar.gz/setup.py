from setuptools import setup, setuptools

setup(
    name="assign3_1",
    version="0.0.1",
    # list folders, not files
    scripts=[
        "assign3_1/ingest_data.py",
        "assign3_1/mlflowrun.py",
        "assign3_1/score.py",
        "assign3_1/train.py",
    ],
    description="assignement 3-1",
    author="Sudheer T",
    package_dir={"": "assign3_1"},
    packages=setuptools.find_packages(
        where="/home/home/sudheer/mle-training/assignment3.1/assign3_1"
    ),
    install_requires=["env"],
)
