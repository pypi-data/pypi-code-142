import setuptools
from setuptools import setup, find_packages
from functools import partial
from os.path import join, abspath, split


with open("README.md", "r") as fh:
    long_description = fh.read()
templates_join = partial(join, abspath(split(__file__)[0]), 'algorithmLib', 'DLLs')
setup(
    name='AlgorithmLib',
    version='3.7.3',
    packages=setuptools.find_packages(),
    include_package_data=True,
    url='https://github.com/pypa/sampleproject',
    license='MIT',
    author=' MA JIANLI',
    author_email='majianli@corp.netease.com',
    description='audio algorithms to compute and test audio quality of speech enhencement',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
    'numpy',
    'wave',
    'matplotlib',
    'datetime',
    'scipy',
    'pystoi',
    'paramiko',
    'moviepy',
    'torch',
    'librosa',
    'requests',
    'pandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
                ('', [templates_join('p563.dll')]),
                ('', [templates_join('p563.dylib')]),
                ('', [templates_join('resample.dll')]),
                ('', [templates_join('resample.dylib')]),
                ('', [templates_join('g160.dll')]),
                ('', [templates_join('g160.dylib')]),
                ('', [templates_join('cygwin1.dll')]),
                ('', [templates_join('peaqb.exe')]),
                ('', [templates_join('PY_PESQ.dll')]),
                ('', [templates_join('PY_PESQ.dylib')]),
                ('', [templates_join('matchsig.dll')]),
                ('', [templates_join('matchsig.dylib')]),
                ('', [templates_join('snr_music.dll')]),
                ('', [templates_join('snr_music.dylib')]),
                ('', [templates_join('snr_transient.dll')]),
                ('', [templates_join('snr_transient.dylib')]),
                ('', [templates_join('time_align.dll')]),
                ('', [templates_join('time_align.dylib')]),
                ('', [templates_join('agcDelay.dll')]),
                ('', [templates_join('agcDelay.dylib')]),
                ('', [templates_join('attackrelease.dll')]),
                ('', [templates_join('attackrelease.dylib')]),
                ('', [templates_join('gaintable.dll')]),
                ('', [templates_join('gaintable.dylib')]),
                ('', [templates_join('musicStability.dll')]),
                ('', [templates_join('musicStability.dylib')]),
                ('', [templates_join('matchsig_aec.dll')]),
                ('', [templates_join('matchsig_aec.dylib')]),
                ('', [templates_join('ERLE_estimation.dll')]),
                ('', [templates_join('ERLE_estimation.dylib')]),
                ('', [templates_join('pcc.dll')]),
                ('', [templates_join('pcc.dylib')]),
                ('', [templates_join('SC_res_retrain_220316_185754125621__ep_007.tar')]),
                ],

    python_requires='>=3.7',
)



