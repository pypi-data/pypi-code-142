from skbuild import setup
setup(
    packages=["pixpy"],
    package_dir={"": "python"},
    cmake_install_dir="python/pixpy",
    cmake_args=["-DPYTHON_MODULE=ON", "-DMACOSX_DEPLOYMENT_TARGET=10.15"],
    package_data={"pixpy": ["py.typed", "*.pyi", "**/*.pyi", "*/*/*.pyi"]},
    zip_safe=False,
)
