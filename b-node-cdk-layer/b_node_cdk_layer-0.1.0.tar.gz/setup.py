from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

with open('VERSION') as file:
    VERSION = file.read()
    VERSION = ''.join(VERSION.split())

setup(
    name='b_node_cdk_layer',
    version=VERSION,
    license='Apache License 2.0',
    packages=find_packages(exclude=[
        # Exclude virtual environment.
        'venv',
        # Exclude test b_node_cdk_layer files.
        'b_node_cdk_layer_test'
    ]),
    description='AWS CDK lambda layer resource that contains node and aws cdk cli packages.',
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "aws_cdk.core>=1.100.0",
        "aws_cdk.aws_lambda>=1.100.0"
    ],
    keywords='AWS CDK Lambda Layer Node',
    url='https://github.com/biomapas/B.NodeCdkLayer.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
