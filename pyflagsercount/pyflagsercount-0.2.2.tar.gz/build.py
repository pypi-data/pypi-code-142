from pybind11.setup_helpers import Pybind11Extension, build_ext

def build(setup_kwargs):
    ext_modules = [
        Pybind11Extension("pycount", ["pyflagsercount/src/flagser_count_bindings.cpp"]),
    ]
    setup_kwargs.update({
        "ext_modules": ext_modules,
        "cmdclass": {"build_ext": build_ext},
        "zip_safe": False,
    })
