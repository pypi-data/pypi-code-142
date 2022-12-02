import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent.resolve()

README = (HERE / "README.md").read_text()

setup(
  name = 'Maxar_Portal_SDK',
  version = '1.1.2',
  license='MIT',
  description = 'SDK for interacting with Maxar imagery platforms',
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'MDS Marianas Team',
  author_email = 'DL-GCS-Marianas@maxar.com',
  project_urls = {
        'Documentation': 'https://maxar-portal.readthedocs.io/en/latest/',
        'Source': 'https://github.com/Maxar-Corp/maxar-portal'
        },
  keywords = ['OGC', 'WMS', 'WFS', 'WMTS', 'WCS', 'MAXAR', 'IMAGERY', 'GIS'],
  python_requires= '>=3.6',
  install_requires=[
          #'gdal',
          'pyproj',
          'shapely',
          'requests',
          'ipython',
          'pillow',
          'click',
          #'rasterio',
          'beautifulsoup4',
          'lxml'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  entry_points='''
    [console_scripts]
    search=Maxar_Portal_SDK.ogc.cli_commands:search
    config=Maxar_Portal_SDK.ogc.cli_commands:config_file
    password=Maxar_Portal_SDK.ogc.cli_commands:reset_password
    download=Maxar_Portal_SDK.ogc.cli_commands:download
    bands=Maxar_Portal_SDK.ogc.cli_commands:band_manipulation
    area=Maxar_Portal_SDK.ogc.cli_commands:calculate_bbox_sqkm
    token=Maxar_Portal_SDK.token_service.cli_commands:create_token
    secret=Maxar_Portal_SDK.token_service.cli_commands:show_secret
    '''
)
