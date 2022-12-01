from .FileSystem import openFile
import os

def cat(fileLoc):
    print(openFile(fileLoc, splitLines = False))

# Better to use linecache
# Optimize later
def tail(fileLoc, numLines):
    data = openFile(fileLoc)
    if numLines > len(data):
        return data
    else:
        return data[-numLines:]

def head(fileLoc, numLines):
    data = openFile(fileLoc)
    if numLines > len(data):
        return data
    else:
        return data[:numLines]

# Recursive and -l options later
def ls(loc):
    try:
        return os.listdir(loc)
    except:
        raise Exception(f"{loc} does not exist, or you don't have permissions!")

# Recursive option later
def rm(loc):
    try:
        os.remove(loc)
    except:
        raise Exception(f"Something happened when trying to remove {loc}")

def pwd():
    return os.getcwd()

# Recursive option later
def cp(fileLoc, fileLoc2):
    if os.path.exists(fileLoc) != True:
        raise Exception("{fileLoc} doesnt exist!")

    try:
        openFile(fileLoc2, newText = openFile(fileLoc, splitLines = False), option = "w")
    except:
        raise Exception("{fileLoc2} could not be made!")

def mv(fileLoc, fileLoc2, override = False):
    if os.path.exists(fileLoc) != True:
        raise Exception("{fileLoc} doesnt exist!")
    
    pathExists = os.path.exists(fileLoc2)

    if pathExists and not override:
        raise Exception("{fileLoc2} will be overwritten, this needs override permissions!")

    try:
        if pathExists:
            cp(fileLoc, fileLoc2)
            os.remove(fileLoc)
        else:
            os.rename(fileLoc, fileLoc2)
    except:
        raise Exception("Something went wrong with moving {fileLoc} to {fileLoc2}")

def history(historyLoc = "~/.bash_history", numLines = -1):
    try:
        data = openFile(historyLoc)
    except:
        raise Exception("Your history file is located somewhere besides {historyLoc}")

    if numLines != -1 and numLines < len(data):
        return data[-numLines:]
    else:
        return data

"""
security labels later
https://docs.python.org/3/library/os.html
os.listxattr()
os.removexattr()
os.setxattr()
"""
