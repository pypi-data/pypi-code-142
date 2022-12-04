import base64
import uuid

def getMyId(me):
    f = open(me)
    for line in f:
        pass
    last_line = line
    line = line.replace('#', '')
    return line
def CreateId(me):
    line = str(uuid.uuid4())
    f = open(me, 'a')
    f.write("\n#" + str(line))
    f.close()
    return line