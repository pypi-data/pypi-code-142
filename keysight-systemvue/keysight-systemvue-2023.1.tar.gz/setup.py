import setuptools

setuptools.setup(

    name="keysight-systemvue", # Replace with your own username

    description="Python package for SystemVue 2023",

    version="2023.1",

    include_package_data=True,

    package_data={'keysight/systemvue': ['*']},

    packages=setuptools.find_namespace_packages(include=['keysight.*']),

    classifiers=[

        "Programming Language :: Python :: 3",

    ],

    install_requires=["numpy", "pandas", "psutil", "matplotlib"],

    python_requires='==3.10.*',

)