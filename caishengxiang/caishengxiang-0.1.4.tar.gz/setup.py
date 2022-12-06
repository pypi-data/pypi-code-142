from setuptools import setup, find_packages

requirements = []
with open('README.rst') as f:
    readme = f.read()
test_requirements = ['pytest>=3']

with open('requirements.txt') as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith('#') or '://' in req:
            continue
        requirements.append(req)

setup(
    author='caishengxiang',
    author_email='wancheng3833@163.com',
    python_requires='>=3.7',
    description='tools for caishengxiang',
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='caishengxiang',
    name='caishengxiang',
    package_data={'': ['*conf', '*.ini', '*.mako', '*.yaml']},
    entry_points={

    },
    packages=find_packages(include=['caishengxiang', 'caishengxiang.*']),
    test_sutie='test',
    test_require=test_requirements,
    url='https://github.com/caishengxiang/caishengxiang',
    version='0.1.4',
    zip_safe=False
)
