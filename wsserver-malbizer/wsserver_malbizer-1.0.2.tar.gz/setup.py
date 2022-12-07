from setuptools import setup

VERSION = '1.0.2' 
DESCRIPTION = 'Websocket Server for python'
LONG_DESCRIPTION = '''
@section{Python Package for Websocket Server Live}

1. WebsocketServer built in python.

2. For active server on command line:

- Install package with PIP;
- Run command wsserver-malbizer '<port>'
- Send JSON string for serve on model:

    {
        "subject": "subject for your message",
        "sender": "id_sender",
        "topic": [], //List of topics to inscribe message
        "payload": "Value for your message (JSON string)",
        "persist": false //indicate if message is persisted and send for new clients
    }



3. For using on python file:

- Import wsservermalbizer with WebsocketServer and use the code:

    WebSocketServer(port=port).start()
'''


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