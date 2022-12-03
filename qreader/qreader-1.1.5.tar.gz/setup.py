from setuptools import setup, find_namespace_packages

setup(
    name='qreader',
    version='1.1.5',
    packages=find_namespace_packages(),
    package_dir={'qreader': 'qreader'},
    url='https://github.com/Eric-Canas/qreader',
    license='MIT',
    author='Eric Canas',
    author_email='elcorreodeharu@gmail.com',
    description='QReader is a very simple and robust QR code detector-decoder for Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'numpy',
        'opencv-python',
        'pyzbar',
    ],
    # To include the yolo_v3 weights in the package, we need to add the following line:
    include_package_data=True,
    # To include the yolo_v3 weights in the package, we need to add the following line:
    data_files=[('yolo_v3', ['yolo_v3/qrcode-yolov3-tiny.cfg', 'yolo_v3/qrcode-yolov3-tiny_last.weights'])],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
