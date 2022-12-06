from setuptools import setup

VERSION = '1.0.0' 
DESCRIPTION = 'Pacote SSH para EC2'
LONG_DESCRIPTION = 'Pacote para enviar arquivos e comandos para EC2 por SSH'

# Setting up
setup(
       # 'name' deve corresponder ao nome da pasta 'verysimplemodule'
        name="sshclient_malbizer", 
        version=VERSION,
        author="Anderson Souza",
        author_email="anderson@malbizer.com.br",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=['sshclient'],
        scripts=['bin/sshclient-send.py'],
        zip_safe=False,
        install_requires=["paramiko==2.9.2","six==1.16.0"], # adicione outros pacotes que 
        # precisem ser instalados com o seu pacote. Ex: 'caer'
        
        keywords=['python', 'ssh', 'clientssh', 'ec2'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)