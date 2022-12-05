from setuptools import setup

with open('README.md', 'r') as reader:
    readme = reader.read()

setup(
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    name='mathiz',
    description='Mathiz, a complete web framework',
    long_description=readme,
    long_description_content_type='text/markdown',
    version='0.3.0',
    url='https://github.com/firlast/mathiz',
    packages=['mathiz'],
    install_requires=['wsblib==1.1.3', 'cryptography==38.0.4'],
    keywords=['www', 'web', 'server', 'http', 'framework', 'wsblib'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: WSGI'
    ],
    project_urls={
        'License': 'https://github.com/firlast/mathiz/blob/master/LICENSE'
    }
)