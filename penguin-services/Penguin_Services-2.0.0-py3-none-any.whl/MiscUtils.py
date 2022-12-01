import hashlib
import datetime

def fileHasher(filename, errorMsg = ""):
    if errorMsg == "":
        errorMsg = f"{filename} did not convert"
    
    try:
        with open(filename, 'rb') as f:
            sha = hashlib.sha256()
            buf = f.read()
            sha.update(buf)
            return sha.hexdigest()
    except:
        print(errorMsg)

def pad(item: str, padding: int = 2) -> str:
    while len(item) < padding:
        item = "0" + item
    return item

def getDate() -> str:
    date = datetime.datetime.now()
    return f'{pad(str(date.day))}_{pad(str(date.month))}_{pad(str(date.year))}'
