from setuptools import setup

setup(
    name='pytorch_to_tensorflow',
    version='1.0.2',
    description='Convert PyTorch models to TensorFlow models',
    url='https://github.com/dnyanshwalwadkar/pytorch_to_tensorflow',
    author='Dnyanesh Walwadkar',
    author_email='dnyanshwalwadkar10@gmail.com',
    license='MIT',
    packages=['pytorch_to_tensorflow'],
    install_requires=['torch', 'tensorflow'],
    zip_safe=True
)
