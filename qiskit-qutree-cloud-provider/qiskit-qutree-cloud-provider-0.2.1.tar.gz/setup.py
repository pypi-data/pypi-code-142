import setuptools

exec(open("qiskit_qutree_cloud_provider/_version.py").read())

setuptools.setup(
    name="qiskit-qutree-cloud-provider",
    version=__version__,
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "qiskit",
        "qiskit-terra>=0.22",
        "grpcio",
        "protobuf",
        "numpy",
    ],
    extras_require={
        "dev": [
            "grpcio-tools",
            "black",
            "pre-commit",
        ],
    },
    tests_require=[],
)
