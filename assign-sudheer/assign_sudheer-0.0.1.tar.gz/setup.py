from setuptools import setup, setuptools

setup(
    name="assign_sudheer",
    version="0.0.1",
    # list folders, not files
    scripts=[
        "assign_sudheer/ingest_data.py",
        "assign_sudheer/mlflowrun.py",
        "assign_sudheer/score.py",
        "assign_sudheer/train.py",
    ],
    description="assignement 3-1",
    author="Sudheer T",
    package_dir={"": "assign_sudheer"},
    packages=setuptools.find_packages(
        where="/home/home/sudheer/mle-training/assignment3.1/assign_sudheer"
    ),
    install_requires=["env"],
)
