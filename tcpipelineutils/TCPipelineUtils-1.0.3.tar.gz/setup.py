from setuptools import setup

setup(
    name = 'TCPipelineUtils',
    version = '1.0.3',
    author = 'Matheus Tramontini Lopes',
    author_email = 'matheus.lopes@tc.com.br',
    packages = ['TCPipelineUtils'],
    install_requires = [
        "TCGCSUtils==1.0.*",
        "numpy==1.23.*",
        "pandas==1.4.*"
    ],
    description='A lib to make easy to create a pipeline in TC',
)
