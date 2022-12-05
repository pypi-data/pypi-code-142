from distutils.core import setup

setup(
    name='MFAC',
    packages=['MFAC'],
    version='0.1',
    license='GPLv3',
    description='Model Free Adaptive Control',
    author='Shahin Darvishpoor',
    author_email='Shahindarvishpoor@gmail.com',
    url='https://Shahindarvishpoor.ir',
    download_url='https://github.com/shahind/MFAC/archive/v_01.tar.gz',
    keywords=['MFAC', 'Control', 'Dynamic'],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
