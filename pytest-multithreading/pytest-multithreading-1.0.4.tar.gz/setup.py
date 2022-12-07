from setuptools import setup

setup(
    name='pytest-multithreading',
    version="1.0.4",
    license='MIT',
    description='a pytest plugin for th and concurrent testing',

    long_description_content_type='text/markdown',
    url='https://github.com/zhujiahuan/pytest-multithreading',
    author='zhujiahuan',
    author_email='zhujiahuan@yfcloud.com',
    include_package_data=True,
    install_requires=['pytest==6.0.2'],
    packages=['pytest_th'],
    entry_points={
        'pytest11': [
            'th = pytest_th',
        ]
    }
)
