from setuptools import setup, find_packages

setup(
    name='SelfPack',
    author='Guo Zhizhou',
    description="  Self used Pkd\n\
             Part of GNSS-R data deal pack\n\
                ************************\n\
                    Version 0.0.1\n\
                Add Bufeng-1 Data Reader\n\
                    Version 0.0.2\n\
                Renew BuFeng-1 Reader\n\
               Add GNOS-R Data Reader\n\
               Add ACCcalculator Method\n\
                  Add LSClub Method\n",
    version='0.0.2',
    packages= find_packages(),
    include_package_data=True,
    package_data={'SelfPack': ['data/*.npy','data/*.txt','data/*.xlsx']})