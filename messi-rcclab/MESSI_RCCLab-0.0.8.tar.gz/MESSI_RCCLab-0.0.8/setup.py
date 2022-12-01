from setuptools import setup, find_packages
  
with open('README.md') as file:
    long_description = file.read()

short_description = 'MESSI: Multi Ensamble Strategy for Structural Elucidation'
requirements = ['tk', 
                'pandas', 
                'numpy', 
                'sklearn', 
                'scipy', 
                'openpyxl',
                'pathlib',
                'scikit-learn']
  

setup(
        name ='MESSI_RCCLab',
        version ='0.0.8',
        author='María M. Zanardi & Ariel M. Sarotti',
        author_email='zanardi@inv.rosario-conicet.gov.ar',
        
        #url='https://github.com/Sarotti-Lab/ML_J_DP4',
        
        description =short_description	,
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        
        packages=find_packages(where="MESSI"),
        package_dir={"": "MESSI"},
        package_data={"UserManual": ["*.pdf"]},
        
        entry_points = {'console_scripts': ['MESSI = MESSI.MESSI:main',],},
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"],
        keywords ='NMR structural elucidation',
        install_requires = requirements
)


