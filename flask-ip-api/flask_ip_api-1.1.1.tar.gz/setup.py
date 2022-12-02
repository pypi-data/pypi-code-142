import setuptools

setuptools.setup(
  name="flask_ip_api",
  version="1.1.1",
  author="EpicCodeWizard",
  author_email="epiccodewizard@gmail.com",
  description="Gives access to client IP information.",
  long_description=open("README.md", "r").read(),
  long_description_content_type="text/markdown",
  url="https://github.com/EpicCodeWizard/Flask-IP-Info-Extension",
  packages=setuptools.find_packages(),
  install_requires=[
    "werkzeug",
    "flask",
    "requests"
  ],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ]
)