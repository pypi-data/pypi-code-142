# from distutils.core import setup
# from Cython.Build import cythonize

# python3.7生成的,只能python3.7调用
# setup(ext_modules=cythonize(
#     ['inference_ncnn_face_detection.py', 'inference_onnx_face_detection.py', 'inference_openvino_face_detection.py']))
# 运行： python setup.py build_ext --inplace


# setup(
#     name="face_detection_module",
#     version="1.0",
#     author="wang zs",
#     author_email="scholar_zswang@163.com",
#     py_modules=['inference_onnx_face_detection','inference_ncnn_face_detection','inference_openvino_face_detection']
# )
#
# # 运行： python setup.py sdist
# # python setup.py install


import os
import setuptools

setuptools.setup(
    name='zs_face_detection',
    version='1.0',
    description='A demo for face detection',
    long_description=open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )
    ).read(),
    packages=setuptools.find_packages(),
    include_package_data=True,
    author='wang zs',
    author_email='scholar_zswang@163.com',
)

# 运行： python setup.py sdist
# 运行： python setup.py bdist_wheel
