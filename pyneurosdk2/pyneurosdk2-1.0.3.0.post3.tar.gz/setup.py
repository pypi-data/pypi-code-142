from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyneurosdk2',
    version='1.0.3.0.post3',
    py_modules=['neurosdk.scanner', 'neurosdk.sensor', 'neurosdk.cmn_types', 'neurosdk.__cmn_types', 'neurosdk.__utils'],
    packages=['neurosdk'],
    url='https://gitlab.com/brainbit-inc/brainbit-sdk',
    license='MIT',
    author='Brainbit Inc.',
    author_email='support@brainbit.com',
    description='Python wrapper for NeuroSDK2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={"neurosdk": ['libs\\neurosdk2-x32.dll', 'libs\\neurosdk2-x64.dll']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.7',
)
