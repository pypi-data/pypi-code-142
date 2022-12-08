from setuptools import setup


setup(
    name='videpy',
    version='0.0.10',
    license='MIT License',
    author='Rodolpho Macedo dos Santos',
    long_description='Useful Bayesian tools to analysis and visualization of the samples. ',
    long_description_content_type='text/markdown',
    url='https://github.com/rodolpho-progmatica/videpy',
    author_email='rodolpho.ime@gmail.com',
    keywords=['videpy', 'vide', 'bayesian', 'stan', 'pystan', 'rethinking'],
    description=u'Tools to handle samples posteriori from Stan (pystan)',
    packages=['videpy'],
    install_requiments=['numpy', 'pandas', 'matplotlib'],
)
