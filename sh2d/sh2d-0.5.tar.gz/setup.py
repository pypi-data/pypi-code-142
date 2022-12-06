import setuptools

with open("README.md", "r",encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="sh2d",
    version="0.5",
    author="sh2d",
    author_email="xx@qq.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    install_requires=['requests','dnspython','paramiko','pymysql','xlrd==1.2.0','xlsxwriter','zmail','xlwt','openpyxl','python-docx','docxtpl','pycryptodome','ddddocr'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
