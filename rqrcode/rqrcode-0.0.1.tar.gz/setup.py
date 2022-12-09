from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    # 包名称
    name="rqrcode", 
    # 包版本 
    version="0.0.1",
    # 须要创立一个文件夹 rqrcode
    packages=["rqrcode"],
    # rust扩大 其中"rqrcode.rqrcode"中
    # 第一个rqrcode 指的是以后的包
    # 第二个指的是
    #[pymodule]
    # fn rqrcode(_py: Python, m: &PyModule) -> PyResult<()> {
    #     m.add_function(wrap_pyfunction!(qrcode_img, m)?)?;
    #     m.add_function(wrap_pyfunction!(qrcode_svg, m)?)?;
    #     m.add_function(wrap_pyfunction!(qrcode_unicode, m)?)?;
    #     Ok(())
    # }
    # 中的rqrcode
    rust_extensions=[
        RustExtension(
            "rqrcode.rqrcode", 
            binding=Binding.PyO3,
            debug=False,
            py_limited_api="auto"
            )
    ],

    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    # 标注
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: Windows",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",

    ],

    include_package_data=True
)