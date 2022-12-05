from setuptools import setup
import os

# Colour Checking
if os.name != 'nt':
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        SLANT = '\x1B[3m'
else:
    class bcolors:
        HEADER = ''
        OKBLUE = ''
        OKCYAN = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''
        SLANT = ''
        print("USEREFUZZ | Colouring is disable as Windows OS is detected")


# Banner
banner=f""" 
{bcolors.FAIL}               (        (               
{bcolors.WARNING}               )\ {bcolors.FAIL})     ){bcolors.WARNING}\ )            
    (       ({bcolors.FAIL} (()/(  ( ({bcolors.WARNING}(){bcolors.FAIL}/(  {bcolors.WARNING}(         
    )\ (   ){bcolors.FAIL})\ /(_))){bcolors.WARNING})\ /(_)){bcolors.FAIL}))\ ({bcolors.WARNING}  (   
 _ ((_))\ /{bcolors.FAIL}((_|_)) /{bcolors.WARNING}((_|_{bcolors.FAIL}))_/((_{bcolors.WARNING}))\ )\ {bcolors.OKBLUE} 
| | | ((_|_)) | _ (_)) | |_(_))(((_|(_) 
| |_| (_-< -_)|   / -_)| __| || |_ /_ / 
 \___//__|___||_|_\___||_|  \_,_/__/__| {bcolors.SLANT}{bcolors.UNDERLINE}Tanishq Rathore{bcolors.ENDC}
                                        
{bcolors.OKBLUE}
 [ 💉💉💉 {bcolors.ENDC}{bcolors.BOLD} UseReFuzz Installation -> use # {bcolors.OKBLUE} python3 setup.py install 💉💉💉 ]{bcolors.ENDC}
 """

print(banner)

def readme():
    with open('pypi.md') as f:
        return f.read()


setup(
    name='userefuzz',
    version='2.0.1',
    long_description=readme(),
    long_description_content_type="text/markdown",
    description='User-Agent, X-Forwarded-For and Referer Header SQLI Fuzzer',
    url='https://github.com/root-tanishq/userefuzz',
    author='Tanishq Rathore',
    license='MIT',
    packages=['userefuzz'],
    console_scripts=['userefuzz=userefuzz/userefuzz.py'],
    install_requires=['requests'],
    classifiers=[
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
    ],
)