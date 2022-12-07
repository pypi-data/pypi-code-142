from setuptools import setup

VERSION = '1.0.6' 
DESCRIPTION = 'Websocket Server for python'
LONG_DESCRIPTION = open("README.md",'r').read()


# Setting up
setup(
       # 'name' deve corresponder ao nome da pasta 'verysimplemodule'
        name="wsserver_malbizer", 
        version=VERSION,
        author="Anderson Souza",
        author_email="anderson@malbizer.com.br",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=LONG_DESCRIPTION,
        packages=['wsservermalbizer'],
        scripts=['bin/wsserver-malbizer.py','bin/wsclient-malbizer.py','bin/wssend-malbizer.py'],
        zip_safe=False,
        install_requires=["websockets==9.1","websocket-client==1.1.0"], # adicione outros pacotes que 
        # precisem ser instalados com o seu pacote. Ex: 'caer'
        
        keywords=['python', 'websocket', 'server'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)