from setuptools import setup, find_packages

setup(
    name="get_folder_file",
    version="0.4.0",
    author="Greg He",
    license='MIT',
    author_email="greg.he@expeditors.com",
    description="This is a python wrapper library for the get file list in a folder",
    url="https://gitlab.chq.ei/north-asia/getfilelistfromfolder.git",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=["requests"],
)
