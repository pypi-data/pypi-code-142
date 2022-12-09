import setuptools

setuptools.setup(
    name="easy_chrome",
    version="1.1.19",
    author="VanCuong",
    author_email="vuvancuong94@gmail.com",
    description="Easy selenium chrome",
    long_description="Easy selenium chrome",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
        'requests',
        'webdriver_manager'
    ],
    python_requires=">=3.7",
)
