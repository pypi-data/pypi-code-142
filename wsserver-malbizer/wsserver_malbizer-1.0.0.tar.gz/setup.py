from setuptools import setup

VERSION = '1.0.0' 
DESCRIPTION = 'Websocket Server for python'
LONG_DESCRIPTION = 'Package for generate websocket server on python!'

# Setting up
setup(
       # 'name' deve corresponder ao nome da pasta 'verysimplemodule'
        name="wsserver_malbizer", 
        version=VERSION,
        author="Anderson Souza",
        author_email="anderson@malbizer.com.br",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=['wsservermalbizer'],
        scripts=['bin/wsserver-malbizer.py'],
        zip_safe=False,
        install_requires=["websockets==9.1"], # adicione outros pacotes que 
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