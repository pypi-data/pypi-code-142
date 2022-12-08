from setuptools import setup

setup(
    name='pytorch_to_tensorflow',
    version='1.0.3',
    description='Convert PyTorch models to TensorFlow models',
	long_description = "Liabrary is attempting to convert a PyTorch model to a TensorFlow model by iterating over the layers in the PyTorch model and adding each layer to a TensorFlow Sequential model. The code includes cases for various layer types, including Linear, Conv2d, ReLU, MaxPool2d, and BatchNorm2d. One potential issue with this code is that it does not handle all possible layer types in PyTorch. For example, it does not include cases for Dropout layers, Flatten layers, or Activation layers. If a PyTorch model contains any of these layer types, the code will fail with an error when it encounters them. Another potential issue is that the code does not handle layers with multiple inputs or outputs. In TensorFlow, it is possible to define models with layers that have multiple inputs or outputs, but the code does not handle this case. If a PyTorch model contains any layers with multiple inputs or outputs, the code will fail with an error when it encounters them. Overall, while the code is a good starting point for converting a PyTorch model to a TensorFlow model, it will likely need to be extended and improved in order to support more complex models and handle all possible layer types in PyTorch. I would recommend carefully testing the code on a variety of PyTorch models to ensure that it works as expected and produces a valid TensorFlow model.",
    url='https://github.com/dnyanshwalwadkar/pytorch_to_tensorflow',
    author='Dnyanesh Walwadkar',
    author_email='dnyanshwalwadkar10@gmail.com',
    license='MIT',
    packages=['pytorch_to_tensorflow'],
    install_requires=['torch', 'tensorflow'],
    zip_safe=True
)
