import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="BB_Chen_Weilin",
    version="0.0.2",
    author="Chen Weilin",
    author_email="2735378542@qq.com",
    packages=["bb"],
    description="write for bb",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChenWeilinx/Fun_old_b",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)