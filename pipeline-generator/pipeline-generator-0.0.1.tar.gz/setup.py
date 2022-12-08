from setuptools import setup, find_packages
version_fn = 'src/pipeline/version.py'
with open(version_fn, 'r') as f:
    verstr = f.read()
version = verstr.split('=')[1]
version = version.replace("'", "").strip()


setup(
    name="pipeline-generator",
    version=version,
    author="wangziling100",
    author_email="wangziling100@163.com",
    description="A pipeline generator in python",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)