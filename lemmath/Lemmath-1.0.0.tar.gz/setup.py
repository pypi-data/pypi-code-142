from setuptools import setup, find_packages

#Preparamos nuestro paquete para distribuirlo
setup(
    name="Lemmath", #Nombre del paquete
    version="1.0.0", #Versión del paquete
    description="Un pedazo paquete para matemática", #Descripción del paquete
    long_description=open("README.md").read(), #Descripcion larga proporcionada por README
    long_description_content_type="text/markdown", #Tipo de archivo de descripción
    author="Lemmgua", #Autor del paquete
    author_email="lemmgua@gmail.com", #Email del autor
    url="https://lemmgua.dev", #URL de la Web del autor
    license_files=["LICENSE"], #Licencias del paquete. 
    #Aquí deberiamos importar cada licencia
    packages=find_packages(), #Paquetes totales. find_packages() añade todos los subpaquetes
    #de forma automática
    scripts=["Principal.py"], #Scripts que forman parte del paquete
    #install_requires=["numpy"] #Dependencias que el paquete necesita para funcionar
    #Estas se instalarán automáticamente
    #También podemos especificarlas deste un archivo externo llamado "requirements"
    install_requires = [paquete.strip() for paquete in open("requirements.txt").readlines()],
    #Para que lo incluya dentro del paquete, hay que especificarlo en "MANIFEST.in"
    #test_suite="tests" #Carpeta que contiene los archivos de testing
    classifiers=[ #Clasificadores para identificar nuestro paquete 
    #https://pypi.org/classifiers/
        "Environment :: Console",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities"
    ]
)