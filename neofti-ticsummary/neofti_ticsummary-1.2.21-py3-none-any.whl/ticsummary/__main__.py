from importlib.metadata import version,PackageNotFoundError
import subprocess
import requests
import os

name_package_os = "ticsummary_domain"
name_package_pypi = "neofti_ticsummary_domain"
#currentVersion = version(name_package_pypi)
needUpdate = False
#url = f"https://pypi.org/pypi/{name_package_pypi}/json"

def getJsonByModule(moduleName:str):
    url = f"https://pypi.org/pypi/{moduleName}/json"
    r = requests.get(url)
    return r.json()

def startApp():
    from sys import platform
    print("Start app")
    if platform == "win32":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.Popen(["python", "-m", name_package_os],startupinfo=startupinfo)
    else:
        subprocess.Popen(["python", "-m", name_package_os])

def __messageBoxClickedUpdate__(listDist:list):
    for dist in listDist:
        updateModule(dist)
    startApp()

def checkUpdate():
    updatableListDist = list()
    if checkVersionModule(name_package_pypi):
        updatableListDist.append(name_package_pypi)
    dataJson = getJsonByModule(name_package_pypi)
    for dist in dataJson['info']['requires_dist']:
        if 'neofti' in dist:
            if checkVersionModule(dist):
                updatableListDist.append(dist)
    return updatableListDist
def updateModule(moduleName:str):
    print(f"Updating {moduleName}")
    subprocess.run(["python", "-m", "pip","install","--upgrade",moduleName])

def checkVersionModule(moduleName:str):
    data = getJsonByModule(moduleName)
    listVersions = data["releases"].keys()
    try:
        currentVersion = version(moduleName)
    except PackageNotFoundError:
        return True
    file_path = os.path.realpath(__file__).rsplit(os.sep,1)[0]

    splitCurrentVersion = currentVersion.split('.')
    valueCurrentVersion = int(splitCurrentVersion[0])*100 + int(splitCurrentVersion[1])*10 + int(splitCurrentVersion[2])
    lastValueVersion = 0 
    for pypiVersion in listVersions:
        splitPypiVersion = pypiVersion.split('.')
        valuePypiVersion = int(splitPypiVersion[0])*100 + int(splitPypiVersion[1])*10 + int(splitPypiVersion[2]) 
        if lastValueVersion < valuePypiVersion:
            lastValueVersion = valuePypiVersion
            lastVersion = pypiVersion
    return lastValueVersion > valueCurrentVersion

def runApp():
    listDistForUpdate = checkUpdate()
    if listDistForUpdate:
        print("need Update")
        from PyQt6.QtWidgets import QMessageBox,QApplication
        import sys

        #comment = data["releases"][lastVersion][0]['comment_text']
        app = QApplication(sys.argv)
        messageBox = QMessageBox()#title="Exit new version. Update?",text=comment)
        messageBox.setWindowTitle("New version available. Update?")
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        messageBox.accepted.connect(lambda:__messageBoxClickedUpdate__(listDistForUpdate))
        messageBox.rejected.connect(lambda:startApp())
        comment = "List of modules to be updated:\n"
        for dist in listDistForUpdate:
            comment += f'{dist} \n'
        messageBox.setText(comment) 
        messageBox.show()
        sys.exit(app.exec())
    else:
        startApp()

if __name__ == "__main__":
    runApp()