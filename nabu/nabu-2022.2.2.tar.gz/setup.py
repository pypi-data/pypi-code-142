# coding: utf-8

from setuptools import setup, find_packages
import os
from nabu import version

def setup_package():
    doc_requires = [
        'sphinx',
        'cloud_sptheme',
        'myst-parser',
        'nbsphinx',
    ]
    setup(
        name='nabu',
        author='Pierre Paleo',
        version=version,
        author_email = "pierre.paleo@esrf.fr",
        maintainer = "Pierre Paleo",
        maintainer_email = "pierre.paleo@esrf.fr",

        packages=find_packages(),
        package_data = {
            'nabu.cuda': [
                'src/*.cu',
                'src/*.h',
            ],
            'nabu.resources': [
                'templates/*.conf',
            ],
        },
        include_package_data=True,

        install_requires = [
            'psutil',
            'pytest',
            'numpy > 1.9.0',
            'scipy',
            'silx >= 0.15.0',
            'tomoscan >= 1.0.6',
            'h5py',
            'tifffile',
        ],
        extras_require = {
            "full": [
                "pyfftw",
                "scikit-image",
                "PyWavelets",
                "glymur",
                "pycuda",
                "scikit-cuda",
                "pycudwt",
            ],
            "doc": doc_requires,
        },
        description = "Nabu - Tomography software",

        entry_points = {
            'console_scripts': [
                "nabu-test=nabu.tests:nabu_test",
                "nabu-cast=nabu.app.cast_volume:main",
                "nabu-config=nabu.app.bootstrap:bootstrap",
                "nabu-zsplit=nabu.app.nx_z_splitter:zsplit",
                "nabu-histogram=nabu.app.histogram:histogram_cli",
                "nabu-rotate=nabu.app.rotate:rotate_cli",
                "nabu-double-flatfield=nabu.app.double_flatfield:dff_cli",
                "nabu-generate-info=nabu.app.generate_header:generate_merged_info_file",
                "nabu-validator=nabu.app.validator:main",
                "nabu=nabu.app.reconstruct:main",
                "nabu-compare-volumes=nabu.app.compare_volumes:compare_volumes_cli",

            ],
        },

        zip_safe=True
    )


if __name__ == "__main__":
    setup_package()
