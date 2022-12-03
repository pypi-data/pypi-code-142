from setuptools import setup, find_packages

setup(
        # the name must match the folder name 'BeLrub'
        name="Belrub", 
        version='0.0.1',
        author="MaMaD BeLectron",
        author_email="",
        description='This is a library for robots in rubika',
        long_description='This is a library for Robots in RUBIKA\n\nfrom BeLrub.BeLrub import Token\n\nbot = Token("AUTH")\ntarget = "GUID"\nbot.sendMessage(target, "Hi BeLrub !"',
        packages=find_packages(),
        
        # add any additional packages that 
        # needs to be installed along with your package.
        install_requires=[], 
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
        ]
)
