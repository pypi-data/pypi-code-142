from setuptools import setup, find_packages

setup(
    name             = 'pygifconvt_oy',
    version          = '1.0.0',
    description      = 'Test package for distribution',
    author           = 'OyKang',
    author_email     = 'oykang64@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'],
	include_package_data=True,
	packages=find_packages(), # pygifconvt_oy를 의미
    keywords         = ['GIFCONVERTER', 'gifconverter'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 